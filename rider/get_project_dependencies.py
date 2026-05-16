import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def _print_dep(dep):
    if isinstance(dep, dict):
        name = dep.get("name", dep.get("id", dep.get("packageId", "?")))
        ver = dep.get("version", dep.get("versionRange", ""))
        print(f"{name} {ver}".rstrip())
    else:
        print(dep)

def main():
    require(2, "python get_project_dependencies.py <module_name> [project_path]")
    params = {"moduleName": sys.argv[1]}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    d = command("get_project_dependencies", params)
    if isinstance(d, str):
        print(d)
    elif isinstance(d, list):
        for dep in d: _print_dep(dep)
    elif isinstance(d, dict):
        for dep in d.get("dependencies", d.get("packages", d.get("results", []))):
            _print_dep(dep)

if __name__ == "__main__":
    main()
