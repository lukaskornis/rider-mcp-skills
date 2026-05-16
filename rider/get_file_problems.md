# slow — runs Rider inspections, allow 60s+
python get_file_problems.py <file_path> [errors_only] [project_path]
file_path:str    project-relative path
errors_only:bool true=errors only, false=errors+warnings (default false)
→ problems[{severity description line column}]
