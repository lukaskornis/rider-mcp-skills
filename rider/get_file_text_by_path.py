import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python get_file_text_by_path.py <path_in_project> [max_lines] [project_path]")
    params = {"pathInProject": sys.argv[1]}
    if len(sys.argv) > 2: params["maxLinesCount"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    print(json.dumps(command("get_file_text_by_path", params), indent=2))

if __name__ == "__main__":
    main()
