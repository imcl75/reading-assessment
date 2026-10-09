"""Builds the self-contained index.html for the results (reporting) page."""
import pathlib
here = pathlib.Path(__file__).parent
html = (here/"template.html").read_text().replace(
    "/*TARGETS*/", (here.parent/"shared"/"reading_targets.js").read_text()).replace(
    "/*SAVE_RESULTS*/", "".join((here.parent / "shared" / f).read_text() for f in ("names-file.js", "pupil_labels.js", "save_results.js")))
(here/"index.html").write_text(html)
print("built index.html")
