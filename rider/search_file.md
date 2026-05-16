# q is a glob pattern, not text — use search_text for content search
python search_file.py <q> [limit] [project_path]
q:str     glob pattern (e.g. "**/*.cs", "Foo*.cs" treated as "**/Foo*.cs")
limit:int max results (default: all)
→ items[{filePath}] more:bool
