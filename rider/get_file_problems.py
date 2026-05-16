import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python get_file_problems.py <file_path> [errors_only] [project_path]")
    params = {"filePath": sys.argv[1]}
    if len(sys.argv) > 2: params["errorsOnly"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("get_file_problems", params, timeout=90)
    if isinstance(d, str):
        print(d)
        return
    problems = d if isinstance(d, list) else d.get("problems", d.get("results", d.get("issues", []))) if isinstance(d, dict) else []
    print(f"total={len(problems)}")
    for p in problems:
        if isinstance(p, dict):
            sev = "E" if p.get("severity", "").lower() in ("error", "e") else "W"
            path = p.get("filePath", p.get("file", "?"))
            line = p.get("line", p.get("lineNumber", "?"))
            msg = p.get("message", p.get("description", str(p)))
            print(f"{sev} {path}:{line}: {msg}")
        else:
            print(p)

if __name__ == "__main__":
    main()
