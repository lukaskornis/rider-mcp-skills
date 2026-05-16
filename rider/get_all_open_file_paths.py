import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command

def main():
    params = {}
    if len(sys.argv) > 1: params["projectPath"] = sys.argv[1]
    d = command("get_all_open_file_paths", params)
    if isinstance(d, str):
        print(d)
        return
    items = d if isinstance(d, list) else d.get("files", d.get("paths", d.get("openFiles", []))) if isinstance(d, dict) else []
    for f in items:
        print(f.get("path", str(f)) if isinstance(f, dict) else f)

if __name__ == "__main__":
    main()
