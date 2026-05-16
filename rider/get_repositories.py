import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command

def main():
    params = {}
    if len(sys.argv) > 1: params["projectPath"] = sys.argv[1]
    print(json.dumps(command("get_repositories", params), indent=2))

if __name__ == "__main__":
    main()
