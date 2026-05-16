# searches filename only, not full path — faster than glob for name lookups
python find_files_by_name_keyword.py <keyword> [limit] [project_path]
keyword:str  case-insensitive substring to find in file names
limit:int    max results
→ files[]
