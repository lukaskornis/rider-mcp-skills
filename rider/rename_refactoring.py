import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(4, "python rename_refactoring.py <path_in_project> <symbol_name> <new_name> [project_path]")
    params = {
        "pathInProject": sys.argv[1],
        "symbolName": sys.argv[2],
        "newName": sys.argv[3],
    }
    if len(sys.argv) > 4: params["projectPath"] = sys.argv[4]
    print(json.dumps(command("rename_refactoring", params, timeout=30), indent=2))

if __name__ == "__main__":
    main()
