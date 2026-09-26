"""QA patches. A qa_patches_<x>.py file defines
  PATCHES = {("26-1", 5): {"a": [...], "g": "..."}}     # fix fields of question 5 (1-based) of test 26-1
  TEXT_PATCHES = {"26-1": [("old words", "new words")]} # replace a substring inside one paragraph of the test text
"""
import glob, sys
def apply_patches(by_id, files):
    for f in files:
        ns = {}; exec(compile(open(f).read(), f, "exec"), ns)
        for (tid, qn), fields in ns.get("PATCHES", {}).items():
            if tid not in by_id: sys.exit(f"{f}: unknown test {tid}")
            by_id[tid]["qs"][qn-1].update(fields)
        for tid, reps in ns.get("TEXT_PATCHES", {}).items():
            if tid not in by_id: sys.exit(f"{f}: unknown test {tid}")
            for old, new in reps:
                hits = [i for i, p in enumerate(by_id[tid]["text"]) if old in p]
                if len(hits) != 1: sys.exit(f"{f}: {tid}: text to replace must appear in exactly one paragraph: {old[:50]!r}")
                by_id[tid]["text"][hits[0]] = by_id[tid]["text"][hits[0]].replace(old, new, 1)
