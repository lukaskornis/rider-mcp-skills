import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require

def main():
    require(2, "python reformat_file.py <path> [project_path]")
    params = {"path": sys.argv[1]}
    if len(sys.argv) > 2: params["projectPath"] = sys.argv[2]
    command("reformat_file", params)
    print("ok")

if __name__ == "__main__":
    main()
