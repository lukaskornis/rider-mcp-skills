import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python get_file_text_by_path.py <path_in_project> [max_lines] [project_path]")
    params = {"pathInProject": sys.argv[1]}
    if len(sys.argv) > 2: params["maxLinesCount"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("get_file_text_by_path", params)
    if isinstance(d, dict):
        total = d.get("totalLinesCount", d.get("total_lines", ""))
        text = d.get("text", d.get("content", d.get("fileText", "")))
        if total:
            print(f"lines={total}")
        print(text)
    elif isinstance(d, str):
        print(d)

if __name__ == "__main__":
    main()
