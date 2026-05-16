import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command

def main():
    params = {"timeout": 120000}
    if len(sys.argv) > 1: params["projectPath"] = sys.argv[1]
    d = command("build_project", params, timeout=130)
    if isinstance(d, dict):
        ok = d.get("success", d.get("succeeded", not (d.get("buildErrors") or d.get("errors"))))
        errors = d.get("buildErrors", d.get("errors", []))
        warnings = d.get("buildWarnings", d.get("warnings", []))
        print(f"{'ok' if ok else 'FAILED'} errors={len(errors)} warnings={len(warnings)}")
        for e in (errors if isinstance(errors, list) else []):
            msg = e.get("message", str(e)) if isinstance(e, dict) else str(e)
            loc = f"{e.get('file','?')}:{e.get('line','?')} " if isinstance(e, dict) and "file" in e else ""
            print(f"  E {loc}{msg}")
    elif isinstance(d, str):
        print(d)

if __name__ == "__main__":
    main()
