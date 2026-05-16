import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python open_file_in_editor.py <file_path> [project_path]")
    params = {"filePath": sys.argv[1]}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    command("open_file_in_editor", params)
    print("ok")

if __name__ == "__main__":
    main()
