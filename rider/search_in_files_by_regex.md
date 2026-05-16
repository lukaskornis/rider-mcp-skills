python search_in_files_by_regex.py <pattern> [file_mask] [dir] [limit] [project_path]
pattern:str  regex pattern
file_mask:str  e.g. "*.cs" (optional)
dir:str        directory relative to project root (optional)
limit:int      max results
→ entries[{filePath lineNumber lineText}] (matches surrounded by ||)
