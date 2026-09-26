"""Usage: python3 -B mc_audit.py [level ...]   Lists (a) multiple-choice questions whose correct option is the longest or tied-longest,
and (b) every 2-mark question, after applying all tests_batch_* and qa_patches_* files. Levels 31-34 are ids 31-..34-."""
import sys, glob, importlib.util, pathlib
here = pathlib.Path(__file__).parent; sys.path.insert(0, str(here))
import tests_src
from patches import apply_patches
for f in sorted(glob.glob(str(here/"tests_batch_*.py"))):
    spec = importlib.util.spec_from_file_location(pathlib.Path(f).stem, f); spec.loader.exec_module(importlib.util.module_from_spec(spec))
last = {t["id"]: t for t in tests_src.TESTS}
apply_patches(last, sorted(glob.glob(str(here/"qa_patches_*.py"))))
lv = {int(a) for a in sys.argv[1:]}
mc = two = 0
for i, t in last.items():
    if lv and t["level"] not in lv: continue
    for n, q in enumerate(t["qs"], 1):
        if q["k"] == "mc":
            L = [len(o) for o in q["opts"]]; k = "ABCD".index(q["a"])
            if L[k] == max(L):
                mc += 1; print(f"MC-LONGEST {i} Q{n} key={q['a']} lens={L}")
        if q["m"] >= 2:
            two += 1; print(f"TWO-MARK   {i} Q{n}: {q['q']}")
print(f"\n{mc} MC problems, {two} two-mark questions")
