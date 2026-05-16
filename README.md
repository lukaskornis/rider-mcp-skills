# rider-mcp-skills

Lightweight CLI wrappers around JetBrains Rider's built-in MCP server, designed for use with Claude Code.

Instead of loading full MCP tool schemas into context on every task, Claude reads a small `skill.md` file and runs a Python script. The script speaks MCP over SSE directly to Rider and prints JSON to stdout.

## Why

MCP tool schemas are large. Loading all Rider MCP schemas at once consumes significant context. This system lets Claude:

1. Read `rider/_index.md` — a one-liner list of available skills (~20 tokens per skill)
2. Read `rider/<skill>.md` — a terse 5-line spec only when needed
3. Run `python rider/<skill>.py <args>` — the script handles the MCP call

## Requirements

- JetBrains Rider open with MCP server enabled (built-in since Rider 2025.1)
- Rider configured in `~/.claude/claude_desktop_config.json` with `IJ_MCP_SERVER_PORT`
- Python 3 (stdlib only — no extra packages needed)

## How it connects

Unlike Unity MCP (which has a simple HTTP bridge), Rider's MCP server uses the standard MCP SSE transport:

1. `GET http://localhost:64342/sse` — opens a server-sent events stream, receives a session endpoint
2. `POST http://localhost:64342/message?sessionId=<id>` — sends JSON-RPC 2.0 MCP messages
3. Results arrive back on the SSE stream

`rider/_lib.py` handles this transparently — skill scripts just call `command(tool, params)`.

## Usage

```bash
python rider/<skill>.py <args>
```

All scripts print JSON to stdout on success. Errors are prefixed with `ERROR:` and exit with code 1.

## Available Skills

See `rider/_index.md` for the full list with usage signatures.

## Skill file format

**`rider/<skill>.md`** — terse spec read by Claude before calling the script:
```
# optional note for non-obvious constraints
python skill_name.py <required_arg> [optional_arg]
arg:type  description
→ return_field1 return_field2
! ErrorType
```

**`rider/<skill>.py`** — CLI wrapper, stdlib only, prints JSON to stdout.

## Shared library

`rider/_lib.py` provides:

- `command(tool, params)` — call a Rider MCP tool, return result data, exit on error
- `require(n, usage)` — exit with usage message if arg count is insufficient
- `coerce(v)` — convert CLI string to `bool`, `int`, `float`, or `str`

## Config

`config.json` at the repo root:
```json
{
  "rider_mcp_url": "http://localhost:64342"
}
```

Change the port here if your Rider uses a different `IJ_MCP_SERVER_PORT`.
