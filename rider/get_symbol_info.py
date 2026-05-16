import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import command, require, coerce

def main():
    require(4, "python get_symbol_info.py <file_path> <line> <column> [project_path]")
    params = {
        "filePath": sys.argv[1],
        "line": coerce(sys.argv[2]),
        "column": coerce(sys.argv[3]),
    }
    if len(sys.argv) > 4: params["projectPath"] = sys.argv[4]
    d = command("get_symbol_info", params)
    if isinstance(d, dict):
        kind = d.get("kind", d.get("symbolKind", ""))
        name = d.get("name", d.get("qualifiedName", "?"))
        sig = d.get("signature", d.get("fullSignature", d.get("presentableText", "")))
        doc = d.get("documentation", d.get("docComment", d.get("xmlDoc", "")))
        print(f"{kind} {name}".strip())
        if sig: print(f"  sig: {sig}")
        if doc: print(f"  doc: {str(doc)[:300]}")
    elif isinstance(d, str):
        print(d)

if __name__ == "__main__":
    main()
