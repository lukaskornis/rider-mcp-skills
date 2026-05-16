import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python execute_run_configuration.py <config_name> [project_path]")
    params = {"configurationName": sys.argv[1], "timeout": 120000}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    d = command("execute_run_configuration", params, timeout=130)
    if isinstance(d, dict):
        ok = d.get("success", d.get("succeeded", True))
        code = d.get("exitCode", d.get("exit_code", ""))
        out = d.get("output", d.get("stdout", ""))
        print(f"{'ok' if ok else 'FAILED'}" + (f" exit={code}" if code != "" else ""))
        if out:
            print(out)
    elif isinstance(d, str):
        print(d)

if __name__ == "__main__":
    main()
