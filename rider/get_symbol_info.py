import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(4, "python get_symbol_info.py <file_path> <line> <column> [project_path]")
    params = {
        "filePath": sys.argv[1],
        "line": coerce(sys.argv[2]),
        "column": coerce(sys.argv[3]),
    }
    if len(sys.argv) > 4: params["projectPath"] = sys.argv[4]
    print(json.dumps(command("get_symbol_info", params), indent=2))

if __name__ == "__main__":
    main()
