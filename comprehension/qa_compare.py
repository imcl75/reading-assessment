"""Usage: python3 -B qa_compare.py <slice letter> [--solved|--check]
  --solved : compare qa/solved_<k>.json (blind answers) with the answer keys
  --check  : apply qa_patches_<k>.py (if present) and validate that slice (does not write index.html)"""
import sys, glob, json, importlib.util, pathlib
here = pathlib.Path(__file__).parent; sys.path.insert(0, str(here))
import tests_src
from patches import apply_patches
from validate import validate
for f in sorted(glob.glob(str(here/"tests_batch_*.py"))):
    spec = importlib.util.spec_from_file_location(pathlib.Path(f).stem, f); spec.loader.exec_module(importlib.util.module_from_spec(spec))
last = {t["id"]: t for t in tests_src.TESTS}
k, mode = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "--solved"
if mode == "--check":
    pf = here/f"qa_patches_{k}.py"
    ids = [x["id"] for x in json.load(open(here/"qa"/f"keys_{k}.json"))]
    if pf.exists(): apply_patches(last, [str(pf)])
    err = validate([last[i] for i in ids])
    print("\n".join(err) if err else f"OK: slice {k} valid" + (" (patches applied)" if pf.exists() else " (no patches file yet)")); sys.exit(1 if err else 0)
solved = json.load(open(here/"qa"/f"solved_{k}.json")); ans = solved.get("answers", {})
bad = 0; checked = 0
for t in json.load(open(here/"qa"/f"keys_{k}.json")):
    for q in t["keys"]:
        kind = q["kind"]
        if kind == "short": continue
        got = ans.get(t["id"], {}).get(str(q["n"]))
        checked += 1
        if kind == "find": ok = isinstance(got, str) and got.strip().lower().strip(".") == str(q["answer"]).strip().lower().strip(".")
        else: ok = got == q["answer"]
        if not ok: bad += 1; print(f'MISMATCH {t["id"]} Q{q["n"]} ({kind}): key={q["answer"]!r} solver={got!r}')
print(f"{checked} objective answers compared, {bad} mismatches")
