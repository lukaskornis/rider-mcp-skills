import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(2, "python search_in_files_by_text.py <search_text> [file_mask] [dir] [limit] [project_path]")
    params = {"searchText": sys.argv[1]}
    if len(sys.argv) > 2: params["fileMask"] = sys.argv[2]
    if len(sys.argv) > 3: params["directoryToSearch"] = sys.argv[3]
    if len(sys.argv) > 4: params["maxUsageCount"] = coerce(sys.argv[4])
    if len(sys.argv) > 5: params["projectPath"] = sys.argv[5]
    print(json.dumps(command("search_in_files_by_text", params), indent=2))

if __name__ == "__main__":
    main()
