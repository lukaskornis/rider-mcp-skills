import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python execute_run_configuration.py <config_name> [project_path]")
    params = {"configurationName": sys.argv[1], "timeout": 120000}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    print(json.dumps(command("execute_run_configuration", params, timeout=130), indent=2))

if __name__ == "__main__":
    main()
