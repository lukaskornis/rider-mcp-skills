import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def _print_node(node, indent=""):
    if isinstance(node, dict):
        name = node.get("name", node.get("path", "?"))
        ntype = node.get("type", node.get("kind", ""))
        print(f"{indent}{name}" + (f" [{ntype}]" if ntype else ""))
        for child in node.get("children", node.get("items", [])):
            _print_node(child, indent + "  ")
    else:
        print(f"{indent}{node}")

def main():
    require(2, "python list_directory_tree.py <directory_path> [max_depth] [project_path]")
    params = {"directoryPath": sys.argv[1]}
    if len(sys.argv) > 2: params["maxDepth"] = coerce(sys.argv[2])
    if len(sys.argv) > 3: params["projectPath"] = sys.argv[3]
    d = command("list_directory_tree", params)
    if isinstance(d, str):
        print(d)
    elif isinstance(d, list):
        for node in d: _print_node(node)
    elif isinstance(d, dict):
        _print_node(d)

if __name__ == "__main__":
    main()
