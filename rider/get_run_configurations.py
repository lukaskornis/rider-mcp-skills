import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command

def main():
    params = {}
    if len(sys.argv) > 1: params["projectPath"] = sys.argv[1]
    d = command("get_run_configurations", params)
    if isinstance(d, str):
        print(d)
        return
    configs = d if isinstance(d, list) else d.get("configurations", d.get("runConfigurations", d.get("results", []))) if isinstance(d, dict) else []
    for c in configs:
        print(c.get("name", c.get("configurationName", str(c))) if isinstance(c, dict) else c)

if __name__ == "__main__":
    main()
