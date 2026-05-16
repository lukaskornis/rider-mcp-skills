import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python execute_terminal_command.py <command> [project_path]")
    params = {"command": sys.argv[1], "executeInShell": True, "reuseExistingTerminalWindow": True}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    d = command("execute_terminal_command", params, timeout=60)
    if isinstance(d, dict):
        print(d.get("output", d.get("stdout", d.get("result", str(d)))))
    elif d is not None:
        print(d)

if __name__ == "__main__":
    main()
