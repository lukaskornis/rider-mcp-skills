import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def _print_matches(d):
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

def main():
    require(2, "python search_in_files_by_text.py <search_text> [file_mask] [dir] [limit] [project_path]")
    params = {"searchText": sys.argv[1]}
    if len(sys.argv) > 2: params["fileMask"] = sys.argv[2]
    if len(sys.argv) > 3: params["directoryToSearch"] = sys.argv[3]
    if len(sys.argv) > 4: params["maxUsageCount"] = coerce(sys.argv[4])
    if len(sys.argv) > 5: params["projectPath"] = sys.argv[5]
    d = command("search_in_files_by_text", params)
    if isinstance(d, str):
        print(d)
    else:
        _print_matches(d)

if __name__ == "__main__":
    main()
