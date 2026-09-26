"""Usage: python3 -B check_batch.py tests_batch_x.py   - validates only that batch file (does not write index.html)."""
import sys, pathlib, importlib.util
here = pathlib.Path(__file__).parent; sys.path.insert(0, str(here))
import tests_src
from validate import validate, fk, fk_warnings, fk_target
n0 = len(tests_src.TESTS)
f = pathlib.Path(sys.argv[1]); spec = importlib.util.spec_from_file_location(f.stem, f.resolve()); spec.loader.exec_module(importlib.util.module_from_spec(spec))
new = tests_src.TESTS[n0:]
for t in new:
    x=" ".join(t["text"]); print(f'{t["id"]:6} {len(x.split()):3}w  {len(t["qs"])}Q {sum(q["m"] for q in t["qs"]):2}m  FK {fk(x):4.1f} (target {fk_target(t):.1f})  {t["type"]:20} {t["title"]}')
err = validate(new) + fk_warnings(new)      # difficulty target is enforced for batches
print("\n".join(err) if err else f"OK: {len(new)} tests pass")
sys.exit(1 if err else 0)
