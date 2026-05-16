import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python get_file_problems.py <file_path> [errors_only] [project_path]")
    params = {"filePath": sys.argv[1]}
    if len(sys.argv) > 2: params["errorsOnly"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    print(json.dumps(command("get_file_problems", params, timeout=90), indent=2))

if __name__ == "__main__":
    main()
