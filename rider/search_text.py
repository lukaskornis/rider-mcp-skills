import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python search_text.py <q> [limit] [project_path]")
    params = {"q": sys.argv[1]}
    if len(sys.argv) > 2: params["limit"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("search_text", params)
    if isinstance(d, str):
        print(d)
        return
    items = d if isinstance(d, list) else d.get("results", d.get("usages", d.get("matches", []))) if isinstance(d, dict) else []
    print(f"total={len(items)}")
    for item in items:
        if isinstance(item, dict):
            path = item.get("filePath", item.get("file", "?"))
            line = item.get("lineNumber", item.get("line", "?"))
            text = (item.get("lineText", item.get("text", item.get("match", "")))).strip()
            print(f"{path}:{line}: {text}")
        else:
            print(item)

if __name__ == "__main__":
    main()
