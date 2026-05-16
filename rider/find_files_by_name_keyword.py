import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python find_files_by_name_keyword.py <keyword> [limit] [project_path]")
    params = {"nameKeyword": sys.argv[1]}
    if len(sys.argv) > 2: params["fileCountLimit"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    print(json.dumps(command("find_files_by_name_keyword", params), indent=2))

if __name__ == "__main__":
    main()
