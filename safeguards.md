# Rider MCP Safeguards

*Known error patterns. Each ## block is checked against every error by log_mcp.py.*
*Format: Pattern (regex), Applies to (tool name or *), Suggestion (fix)*

## rename_refactoring when code has errors

Pattern: symbol not found|cannot find symbol|symbol.*not.*found
Applies to: rename_refactoring
Suggestion: rename_refactoring fails when code doesn't compile. Use search_in_files_by_text + replace_text_in_file instead.

## read_file wrong param name

Pattern: missing required.*file_path|required.*pathInProject
Applies to: read_file
Suggestion: The param is "file_path" (not "pathInProject"). Use: {"file_path": "/absolute/path/to/file.cs"}

