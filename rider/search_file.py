import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python search_file.py <q> [limit] [project_path]")
    params = {"q": sys.argv[1]}
    if len(sys.argv) > 2: params["limit"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("search_file", params)
    if isinstance(d, str):
        print(d)
        return
    items = d if isinstance(d, list) else d.get("files", d.get("results", [])) if isinstance(d, dict) else []
    print(f"total={len(items)}")
    for f in items:
        print(f.get("path", f.get("filePath", f.get("relativePath", str(f)))) if isinstance(f, dict) else f)

if __name__ == "__main__":
    main()
