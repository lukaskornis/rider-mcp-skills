# <arg>=required  [arg]=optional  type after colon  →=returns  !=errors  #=note

## File operations
get_all_open_file_paths  — list active file and all open editor tabs
read_file                — read file lines by path (slice/lines/offsets modes)
get_file_text_by_path    — read full file text by project-relative path
replace_text_in_file     — replace text or regex match in a file
reformat_file            — reformat (auto-indent) a file

## Search
search_file              — find files matching a glob pattern (quick, indexed)
search_text              — search text across the entire project
search_in_files_by_text  — find files containing a text string
search_in_files_by_regex — find files matching a regex
search_symbol            — find a symbol (class/method/field) by name
find_files_by_name_keyword — find files whose name contains a keyword
find_files_by_glob       — find files matching a glob pattern

## Code intelligence
get_symbol_info          — type, docs, usages for a symbol at a file location
get_file_problems        — list errors/warnings in a file
rename_refactoring       — rename a symbol across the project

## Project
get_project_modules      — list solution modules/projects
get_project_dependencies — list NuGet/package dependencies
get_repositories         — list VCS repositories in the solution
get_run_configurations   — list run/debug configurations

## Directory
list_directory_tree      — tree listing of a project directory (like `tree`)

## Editor control
open_file_in_editor      — open a file in the Rider editor
create_new_file          — create a new file in the project
execute_terminal_command — run a shell command in Rider's terminal

## Build & run
build_project            — build the solution or a specific project
execute_run_configuration — launch a run configuration
