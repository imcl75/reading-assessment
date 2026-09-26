"""Usage: python3 -B check_patches.py qa_patches_<x>.py
Applies every earlier patch file (alphabetically before this one), then this one, and validates the tests this file touches."""
import sys, glob, importlib.util, pathlib
here = pathlib.Path(__file__).parent; sys.path.insert(0, str(here))
import tests_src
from patches import apply_patches
from validate import validate
for f in sorted(glob.glob(str(here/"tests_batch_*.py"))):
    spec = importlib.util.spec_from_file_location(pathlib.Path(f).stem, f); spec.loader.exec_module(importlib.util.module_from_spec(spec))
last = {t["id"]: t for t in tests_src.TESTS}
mine = (here / sys.argv[1]).resolve() if not pathlib.Path(sys.argv[1]).is_absolute() else pathlib.Path(sys.argv[1])
files = [f for f in sorted(glob.glob(str(here/"qa_patches_*.py"))) if f <= str(mine)]
apply_patches(last, files)
ns = {}; exec(compile(open(mine).read(), str(mine), "exec"), ns)
ids = {tid for (tid, _) in ns.get("PATCHES", {})} | set(ns.get("TEXT_PATCHES", {}))
err = validate([last[i] for i in sorted(ids)])
print("\n".join(err) if err else f"OK: {len(ids)} tests touched, all valid")
sys.exit(1 if err else 0)
