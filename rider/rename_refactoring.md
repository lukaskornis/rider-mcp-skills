# fails if code doesn't compile — use replace_text_in_file for bulk renames when compile is broken
python rename_refactoring.py <path_in_project> <symbol_name> <new_name> [project_path]
path_in_project:str  file containing the symbol declaration
symbol_name:str      exact current name (case-sensitive)
new_name:str         new name
→ success message string
! "symbol not found"  "rename failed"
