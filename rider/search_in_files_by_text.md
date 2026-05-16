python search_in_files_by_text.py <search_text> [file_mask] [dir] [limit] [project_path]
search_text:str  substring to find across project files
file_mask:str    e.g. "*.cs" (optional)
dir:str          directory relative to project root (optional)
limit:int        max results
→ entries[{filePath lineNumber lineText}] (matches surrounded by ||)
