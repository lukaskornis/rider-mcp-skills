import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command

def main():
    params = {}
    if len(sys.argv) > 1: params["projectPath"] = sys.argv[1]
    d = command("get_project_modules", params)
    if isinstance(d, str):
        print(d)
        return
    mods = d if isinstance(d, list) else d.get("modules", d.get("results", [])) if isinstance(d, dict) else []
    for m in mods:
        print(m.get("name", m.get("moduleName", str(m))) if isinstance(m, dict) else m)

if __name__ == "__main__":
    main()
