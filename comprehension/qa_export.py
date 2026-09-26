"""Exports blind question files (no answers) and separate key files for QA checkers. Run: python3 -B qa_export.py"""
import sys, glob, json, importlib.util, pathlib
here = pathlib.Path(__file__).parent; sys.path.insert(0, str(here))
import tests_src
for f in sorted(glob.glob(str(here/"tests_batch_*.py"))):
    spec = importlib.util.spec_from_file_location(pathlib.Path(f).stem, f); spec.loader.exec_module(importlib.util.module_from_spec(spec))
last = {t["id"]: t for t in tests_src.TESTS}
T = sorted(last.values(), key=lambda t: (t["level"], int(t["id"].split("-")[1])))
SLICES = {"a":(18,20),"b":(21,23),"c":(24,26),"d":(27,29),"e":(30,31),"f":(32,34)}
for k,(lo,hi) in SLICES.items():
    sel = [t for t in T if lo <= t["level"] <= hi]
    blind = [dict(id=t["id"], level=t["level"], title=t["title"], type=t["type"], text=t["text"],
                  questions=[{kk:v for kk,v in dict(n=i, kind=q["k"], marks=q["m"], question=q["q"], options=q.get("opts"), items=q.get("items")).items() if v is not None} for i,q in enumerate(t["qs"],1)]) for t in sel]
    keys = [dict(id=t["id"], keys=[dict(n=i, kind=q["k"], domain=q["d"], marks=q["m"], answer=q["a"], guidance=q.get("g","")) for i,q in enumerate(t["qs"],1)]) for t in sel]
    (here/"qa"/f"blind_{k}.json").write_text(json.dumps(blind, ensure_ascii=False, indent=1))
    (here/"qa"/f"keys_{k}.json").write_text(json.dumps(keys, ensure_ascii=False, indent=1))
    print(k, lo, hi, len(sel), "tests")
