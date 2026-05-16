import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python read_file.py <file_path> [start_line] [max_lines] [project_path]")
    params = {"file_path": sys.argv[1], "mode": "slice"}
    if len(sys.argv) > 2: params["start_line"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["max_lines"] = coerce(sys.argv[3])
    if len(sys.argv) > 4: params["projectPath"] = sys.argv[4]
    print(json.dumps(command("read_file", params), indent=2))

if __name__ == "__main__":
    main()
