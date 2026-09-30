"""Builds the self-contained index.html for the results (reporting) page."""
import pathlib
here = pathlib.Path(__file__).parent
html = (here/"template.html").read_text().replace(
    "/*SAVE_RESULTS*/", (here.parent/"shared"/"save_results.js").read_text())
(here/"index.html").write_text(html)
print("built index.html")
