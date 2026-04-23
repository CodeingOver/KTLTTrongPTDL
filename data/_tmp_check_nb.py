import json
from pathlib import Path

nb_path = Path(r"d:\CodePython\KTLTTrongPTDL\01_Crawl_Data.ipynb")
nb = json.loads(nb_path.read_text(encoding="utf-8"))
errors = []
for idx, cell in enumerate(nb.get("cells", []), start=1):
    if cell.get("cell_type") != "code":
        continue
    src = "\n".join(cell.get("source", []))
    try:
        compile(src, f"cell_{idx}", "exec")
    except Exception as e:
        errors.append((idx, str(e)))

if errors:
    print("SYNTAX_ERRORS")
    for idx, err in errors:
        print(idx, err)
else:
    print("SYNTAX_OK")
