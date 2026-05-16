import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python find_files_by_name_keyword.py <keyword> [limit] [project_path]")
    params = {"nameKeyword": sys.argv[1]}
    if len(sys.argv) > 2: params["fileCountLimit"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("find_files_by_name_keyword", params)
    if isinstance(d, str):
        print(d)
        return
    items = d if isinstance(d, list) else d.get("files", d.get("results", [])) if isinstance(d, dict) else []
    print(f"total={len(items)}")
    for f in items:
        print(f.get("path", f.get("filePath", f.get("relativePath", str(f)))) if isinstance(f, dict) else f)

if __name__ == "__main__":
    main()
