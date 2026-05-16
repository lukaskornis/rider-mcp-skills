import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python read_file.py <file_path> [start_line] [max_lines] [project_path]")
    params = {"file_path": sys.argv[1], "mode": "slice"}
    if len(sys.argv) > 2: params["start_line"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["max_lines"] = coerce(sys.argv[3])
    if len(sys.argv) > 4: params["projectPath"] = sys.argv[4]
    d = command("read_file", params)
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
