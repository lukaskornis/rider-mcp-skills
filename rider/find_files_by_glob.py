import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def _print_files(d):
    items = d if isinstance(d, list) else d.get("files", d.get("results", [])) if isinstance(d, dict) else []
    print(f"total={len(items)}")
    for f in items:
        print(f.get("path", f.get("filePath", f.get("relativePath", str(f)))) if isinstance(f, dict) else f)

def main():
    require(2, "python find_files_by_glob.py <glob_pattern> [limit] [project_path]")
    params = {"globPattern": sys.argv[1]}
    if len(sys.argv) > 2: params["fileCountLimit"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("find_files_by_glob", params)
    if isinstance(d, str):
        print(d)
    else:
        _print_files(d)

if __name__ == "__main__":
    main()
