import json
import os
import queue
import sys
import threading
import urllib.error
import urllib.request

_root = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


def _load_config():
    with open(os.path.join(_root, "config.json")) as f:
        return json.load(f)


def _post(url, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        resp.read()


def coerce(v):
    if v.lower() == "true": return True
    if v.lower() == "false": return False
    try: return int(v)
    except ValueError: pass
    try: return float(v)
    except ValueError: pass
    return v


def require(n, usage):
    if len(sys.argv) < n:
        print(f"ERROR: Usage: {usage}")
        sys.exit(1)


def command(tool, params, timeout=15):
    config = _load_config()
    base = config["rider_mcp_url"]

    result_q = queue.Queue()
    endpoint_q = queue.Queue()
    err = []

    def read_sse():
        try:
            req = urllib.request.Request(f"{base}/sse")
            with urllib.request.urlopen(req, timeout=30) as resp:
                event_type = None
                for line in resp:
                    line = line.decode().rstrip("\n\r")
                    if line.startswith("event: "):
                        event_type = line[7:]
                    elif line.startswith("data: "):
                        data = line[6:]
                        if event_type == "endpoint":
                            endpoint_q.put(data)
                        elif event_type == "message":
                            try:
                                msg = json.loads(data)
                                if "id" in msg:
                                    result_q.put(msg)
                            except json.JSONDecodeError:
                                pass
                        event_type = None
        except Exception as e:
            err.append(e)
            endpoint_q.put(None)
            result_q.put(None)

    t = threading.Thread(target=read_sse, daemon=True)
    t.start()

    try:
        endpoint = endpoint_q.get(timeout=5)
    except queue.Empty:
        print(f"ERROR: Rider MCP server not reachable at {base}")
        sys.exit(1)

    if endpoint is None:
        reason = err[0] if err else "Unknown error"
        print(f"ERROR: Rider MCP server not reachable — {reason}")
        sys.exit(1)

    url = f"{base}{endpoint}"

    try:
        # initialize
        _post(url, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2024-11-05", "capabilities": {},
            "clientInfo": {"name": "rider-mcp-skills", "version": "1.0"}
        }})
        init = result_q.get(timeout=5)
        if init is None or "error" in init:
            print(f"ERROR: Initialize failed — {init}")
            sys.exit(1)

        # initialized notification (no response expected)
        _post(url, {"jsonrpc": "2.0", "method": "notifications/initialized"})

        # tool call
        _post(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                    "params": {"name": tool, "arguments": params}})
        resp = result_q.get(timeout=timeout)

        if resp is None or "error" in resp:
            msg = (resp or {}).get("error", {}).get("message", "Unknown error")
            print(f"ERROR: {msg}")
            sys.exit(1)

        result = resp.get("result", {})
        if result.get("isError"):
            content = result.get("content", [])
            msg = content[0].get("text", "Tool error") if content else "Tool error"
            print(f"ERROR: {msg}")
            sys.exit(1)

        # prefer structuredContent (already parsed), fall back to parsing content[0].text
        structured = result.get("structuredContent")
        if structured is not None:
            return structured
        content = result.get("content", [])
        if content:
            text = content[0].get("text", "")
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return text
        return result

    except queue.Empty:
        print("ERROR: Timed out waiting for Rider response")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Rider MCP server not reachable — {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
