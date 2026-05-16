# saves the file automatically after replacement
python replace_text_in_file.py <path_in_project> <old_text> <new_text> [project_path]
path_in_project:str  project-relative file path
old_text:str         exact text to find (or regex if --regex flag added)
new_text:str         replacement text
→ "ok"
! "no occurrences found"  "file not found"
