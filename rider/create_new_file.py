import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python create_new_file.py <path_in_project> [project_path]")
    params = {"pathInProject": sys.argv[1]}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    print(json.dumps(command("create_new_file", params), indent=2))

if __name__ == "__main__":
    main()
