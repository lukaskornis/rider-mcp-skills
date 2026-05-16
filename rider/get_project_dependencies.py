import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python get_project_dependencies.py <module_name> [project_path]")
    params = {"moduleName": sys.argv[1]}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    print(json.dumps(command("get_project_dependencies", params), indent=2))

if __name__ == "__main__":
    main()
