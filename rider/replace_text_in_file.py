import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(4, "python replace_text_in_file.py <path_in_project> <old_text> <new_text> [project_path]")
    params = {
        "pathInProject": sys.argv[1],
        "oldText": sys.argv[2],
        "newText": sys.argv[3],
        "replaceAll": True,
    }
    if len(sys.argv) > 4: params["projectPath"] = sys.argv[4]
    d = command("replace_text_in_file", params)
    if isinstance(d, dict):
        count = d.get("replacements", d.get("replacedCount", d.get("usagesCount", "")))
        print(f"replaced" + (f" {count} occurrences" if count else ""))
    elif isinstance(d, str):
        print(d if d.strip() else "ok")
    else:
        print("ok")

if __name__ == "__main__":
    main()
