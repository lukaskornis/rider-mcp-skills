import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python list_directory_tree.py <directory_path> [max_depth] [project_path]")
    params = {"directoryPath": sys.argv[1]}
    if len(sys.argv) > 2: params["maxDepth"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    print(json.dumps(command("list_directory_tree", params), indent=2))

if __name__ == "__main__":
    main()
