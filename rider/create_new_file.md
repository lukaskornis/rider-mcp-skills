# may timeout if Rider can't acquire a write lock (e.g. Unity is compiling)
python create_new_file.py <path_in_project> [project_path]
path_in_project:str  project-relative path; parent dirs created automatically
→ result string
