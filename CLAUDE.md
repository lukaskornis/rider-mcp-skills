# rider-mcp-skills

CLI wrappers for Rider's MCP server. Each skill = one `<name>.md` + one `<name>.py` in `rider/`.

## Transport

Rider exposes MCP via SSE at `http://localhost:64342` (port from `IJ_MCP_SERVER_PORT` in claude_desktop_config.json):
- `GET /sse` → SSE stream; first event is `endpoint: /message?sessionId=<uuid>`
- `POST /message?sessionId=<uuid>` → send JSON-RPC 2.0; returns 202; result arrives on SSE stream

`rider/_lib.py` handles the full protocol (SSE connect → initialize → initialized → tools/call).

## Response shape

```json
{
  "content": [{"text": "...", "type": "text"}],
  "isError": false,
  "structuredContent": { ... }
}
```

`command()` returns `structuredContent` when present, falls back to parsing `content[0].text`.

## Adding a skill

1. Load schema: `ToolSearch select:mcp__rider__<name>`
2. Test live: run the Python test pattern in _lib.py against the real tool
3. Write `rider/<name>.md` (5–8 lines, follow format in `rider/_index.md` header)
4. Write `rider/<name>.py` (import `_lib`, call `command`, print JSON)
5. Add one-liner to `rider/_index.md`
6. Test end-to-end, commit

## Skill.md format

```
# note only for real gotchas
python <skill>.py <req_arg> [opt_arg]
arg:type  description or enum values
→ return_field1 return_field2
! ErrorType
```

## Notes

- `projectPath` is optional on most tools but reduces ambiguity — always pass when known
- `read_file` requires `mode` param (slice/lines/line_columns/offsets/indentation)
- `replace_text_in_file` can do regex or plain text replacement
- `build_project` may be async — check if result has `job_id`
