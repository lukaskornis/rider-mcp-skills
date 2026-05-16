import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python create_new_file.py <path_in_project> [project_path]")
    params = {"pathInProject": sys.argv[1]}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    d = command("create_new_file", params)
    if isinstance(d, dict):
        path = d.get("path", d.get("filePath", d.get("pathInProject", "")))
        print(f"ok {path}" if path else "ok")
    elif isinstance(d, str):
        print(d if d.strip() else "ok")
    else:
        print("ok")

if __name__ == "__main__":
    main()
