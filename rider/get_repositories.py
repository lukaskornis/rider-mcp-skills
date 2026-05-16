import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command

def main():
    params = {}
    if len(sys.argv) > 1: params["projectPath"] = sys.argv[1]
    d = command("get_repositories", params)
    if isinstance(d, str):
        print(d)
        return
    repos = d if isinstance(d, list) else d.get("repositories", d.get("results", [])) if isinstance(d, dict) else []
    for r in repos:
        if isinstance(r, dict):
            name = r.get("name", r.get("path", "?"))
            branch = r.get("branch", r.get("currentBranch", r.get("state", "")))
            print(f"{name}" + (f" [{branch}]" if branch else ""))
        else:
            print(r)

if __name__ == "__main__":
    main()
