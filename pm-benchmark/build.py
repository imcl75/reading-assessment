"""Builds the self-contained index.html for the PM Benchmark running-records tool.

Source data lives in pm_benchmark_levels_18_30.json (52 texts: levels 18-30, two Blue + two
Red per level, licensed PM Benchmark content). This script assigns each text a stable id
(level-colour-index, e.g. "pmb-18-blue-1"), drops the source_file field (irrelevant at
runtime, just the original scan filename), and embeds the result as DATA, same pattern as
the other three tools' build.py."""
import json
import pathlib

here = pathlib.Path(__file__).parent
texts = json.loads((here / "pm_benchmark_levels_18_30.json").read_text())

by_level = {}
for t in texts:
    by_level.setdefault(t["level"], {"Blue": [], "Red": []})[t["colour"]].append(t)

DATA = []
for level in sorted(by_level):
    texts_out = []
    for colour in ("Blue", "Red"):
        for i, t in enumerate(by_level[level][colour]):
            t = dict(t)
            t.pop("source_file", None)
            t["id"] = f"pmb-{level}-{colour.lower()}-{i + 1}"
            texts_out.append(t)
    DATA.append({"level": level, "texts": texts_out})

html = (here / "template.html").read_text()
html = html.replace("/*DATA*/", json.dumps(DATA, ensure_ascii=False))
html = html.replace("/*SAVE_RESULTS*/", "".join((here.parent / "shared" / f).read_text() for f in ("names-file.js", "pupil_labels.js", "save_results.js")))
(here / "index.html").write_text(html)
print(f"built index.html: {sum(len(l['texts']) for l in DATA)} texts across {len(DATA)} levels, "
      f"{sum(len(t['questions']) for l in DATA for t in l['texts'])} questions")
