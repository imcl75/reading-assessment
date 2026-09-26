"""Builds index.html from template.html + texts.json (single self-contained file)."""
import json, pathlib
here = pathlib.Path(__file__).parent
texts = json.loads((here / "texts.json").read_text())
for t in texts:
    assert len(t["text"].split()) == 100, (t["level"], len(t["text"].split()))
html = (here / "template.html").read_text().replace("/*TEXTS*/", json.dumps(texts, ensure_ascii=False)).replace("/*SAVE_RESULTS*/", (here.parent / "shared" / "save_results.js").read_text())
(here / "index.html").write_text(html)
print("built index.html,", len(texts), "texts")
