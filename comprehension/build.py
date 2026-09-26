"""Validates every test, then builds a single self-contained index.html."""
import json, pathlib, sys, importlib.util, glob
from validate import validate, fk, TARGET, fk_warnings
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
import tests_src
from tests_src import TESTS
for f in sorted(glob.glob(str(here/"tests_batch_*.py"))):     # each batch file registers tests via tests_src.T
    spec = importlib.util.spec_from_file_location(pathlib.Path(f).stem, f); spec.loader.exec_module(importlib.util.module_from_spec(spec))
# a later batch file may replace a test by reusing its id (the last definition wins)
_last = {t["id"]: t for t in TESTS}
TESTS[:] = list(_last.values())
from patches import apply_patches
apply_patches(_last, sorted(glob.glob(str(here/"qa_patches_*.py"))))
TESTS.sort(key=lambda t:(t["level"], int(t["id"].split("-")[1])))
err = validate(TESTS)
by={}
for t in TESTS:
    x=" ".join(t["text"]); by.setdefault(t["level"],[]).append(t)
    print(f'{t["id"]:6} {len(x.split()):3}w  {len(t["qs"])}Q {sum(q["m"] for q in t["qs"]):2}m  FK {fk(x):4.1f}  {t["type"]}')
for w in fk_warnings(TESTS): print("  note:", w)
if err: sys.exit("not built:\n"+"\n".join(err))
data=[dict(level=l,texts=v) for l,v in sorted(by.items())]
(here/"index.html").write_text((here/"template.html").read_text().replace("/*DATA*/",json.dumps(data,ensure_ascii=False)).replace("/*SAVE_RESULTS*/",(here.parent/"shared"/"save_results.js").read_text()))
print("built index.html:",len(TESTS),"tests across",len(by),"levels")
