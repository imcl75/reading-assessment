"""
generate_texts_batch2.py
Generates the Y3 and Y5 reading-assessment print PDFs that home.html has linked to since the
on-screen Y3/Y5 papers were added, but whose PDFs were never built (home.html's links 404).

Passage text is pulled straight from the same TEXTS objects the on-screen pages (y3/autumn,
y3/summer, y5/autumn, y5/summer) already show pupils, so the print version matches the screen
version exactly. Reuses generate_texts.py's house style (PageManager, header/footer/title-block,
draw_para/draw_h3/draw_bullet/draw_poetry_stanza) rather than duplicating it — only adds what's
missing: a wrapped-cell table (one passage, "Inside? Outside?", has three data tables) and a
year-group footer label. generate_texts.py itself is untouched.
"""
import html
import os
import re

import generate_texts as gt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

TAG_RE = re.compile(r"<[^>]+>")


def clean_text(s: str) -> str:
    s = TAG_RE.sub("", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def draw_footer_year(c, page_num, year_label):
    gt.set_stroke(c, gt.GREY)
    c.setLineWidth(0.5)
    c.line(gt.MARGIN_L, gt.FOOTER_Y + 12, gt.CONTENT_RIGHT, gt.FOOTER_Y + 12)
    gt.set_fill(c, gt.GREY)
    c.setFont("Helvetica", 8)
    c.drawString(gt.MARGIN_L, gt.FOOTER_Y, year_label)
    c.drawRightString(gt.CONTENT_RIGHT, gt.FOOTER_Y, f"Page {page_num}")


class PageManagerY(gt.PageManager):
    """Same as PageManager, but the footer says 'Year 3/5 Reading Assessment' and it can draw
    a table whose cells wrap onto several lines (generate_texts.py's own draw_table only ever
    draws one line per cell, which is fine for its own short label/value rows but not here)."""

    def __init__(self, c, title, genre, year_label, author=None):
        self.year_label = year_label
        super().__init__(c, title, genre, author=author)

    def _new_page(self):
        if self.page_num > 1:
            self.c.showPage()
        gt.draw_header(self.c, self.title, self.page_num)
        draw_footer_year(self.c, self.page_num, self.year_label)
        self.y = gt.draw_title_block(self.c, self.title, self.genre,
                                     author=self.author if self.page_num == 1 else None)
        self.page_num += 1

    def draw_wrapped_table(self, headers, rows, col_widths=None):
        """A table whose cells wrap (unlike PageManager.draw_table's single-line cells).
        headers: list[str] or None. rows: list[list[str]]. Kept together on one page."""
        n_cols = len(rows[0]) if rows else len(headers or [])
        if col_widths is None:
            col_widths = [gt.CONTENT_W / n_cols] * n_cols
        cell_pad = 6
        font_size, leading = 10, 13

        def cell_lines(text, col_w):
            return gt.wrap_words(self.c, text, "Helvetica", font_size, col_w - 2 * cell_pad) or [[]]

        def row_height(cells):
            n = max(len(cell_lines(c, col_widths[i])) for i, c in enumerate(cells))
            return n * leading + 2 * cell_pad

        all_rows = ([headers] if headers else []) + rows
        heights = [row_height(r) for r in all_rows]
        total_h = sum(heights) + 4
        self.ensure_space(total_h + 12)
        self.add_space(8)
        tx = gt.CONTENT_X
        y_top = self.y
        for ri, (row, h) in enumerate(zip(all_rows, heights)):
            is_header = headers is not None and ri == 0
            y_bottom = y_top - h
            gt.set_fill(self.c, gt.BRAND if is_header else (gt.WHITE if ri % 2 == 0 else (0.95, 0.95, 0.95)))
            self.c.rect(tx, y_bottom, gt.CONTENT_W, h, fill=1, stroke=0)
            gt.set_stroke(self.c, (0.75, 0.75, 0.75))
            self.c.setLineWidth(0.3)
            self.c.rect(tx, y_bottom, gt.CONTENT_W, h, fill=0, stroke=1)
            cx = tx
            for ci, cell in enumerate(row):
                col_w = col_widths[ci]
                lines = cell_lines(cell, col_w)
                gt.set_fill(self.c, gt.WHITE if is_header else gt.DARK)
                self.c.setFont("Helvetica-Bold" if is_header else "Helvetica", font_size)
                by = y_top - cell_pad - font_size * 0.72
                for words in lines:
                    self.c.drawString(cx + cell_pad, by, " ".join(words))
                    by -= leading
                cx += col_w
            y_top = y_bottom
        self.y = y_top - 4


BLOCK_RE = re.compile(
    r'<h2>.*?</h2>'
    r'|<h3>(?P<h3>.*?)</h3>'
    r'|<ul>(?P<ul>.*?)</ul>'
    r'|<table>(?P<table>.*?)</table>'
    r'|<div class="poem-stanza">(?P<stanza>.*?)</div>'
    r'|<p(?P<pattrs>[^>]*)>(?P<p>.*?)</p>',
    re.S,
)
LI_RE = re.compile(r'<li>(.*?)</li>', re.S)
LINE_RE = re.compile(r'<p class="poem-line">(.*?)</p>', re.S)
ROW_RE = re.compile(r'<tr>(.*?)</tr>', re.S)
CELL_RE = re.compile(r'<t[hd]>(.*?)</t[hd]>', re.S)


def render(pm: PageManagerY, html_src: str):
    for m in BLOCK_RE.finditer(html_src):
        if m.group("h3") is not None:
            pm.draw_h3(clean_text(m.group("h3")))
        elif m.group("ul") is not None:
            for li in LI_RE.findall(m.group("ul")):
                pm.draw_bullet(clean_text(li))
        elif m.group("table") is not None:
            rows = [[clean_text(c) for c in CELL_RE.findall(r)] for r in ROW_RE.findall(m.group("table"))]
            has_header = "<th>" in m.group("table")
            pm.draw_wrapped_table(rows[0] if has_header else None, rows[1:] if has_header else rows)
        elif m.group("stanza") is not None:
            pm.draw_poetry_stanza([clean_text(l) for l in LINE_RE.findall(m.group("stanza"))])
        elif m.group("p") is not None:
            if "font-size:13px" in (m.group("pattrs") or ""):
                continue  # the poem author line — passed to PageManagerY separately, not drawn as a paragraph
            pm.draw_para(clean_text(m.group("p")))


def author_of(html_src: str):
    m = re.search(r'<p style="font-size:13px[^"]*">\s*(?:adapted from a poem by|by)\s+(.*?)</p>', html_src, re.S)
    return clean_text(m.group(1)) if m else None


# (filename, year_label, source file, TEXTS index, genre)
PASSAGES = [
    ("y3-autumn-fireworks.pdf",              "Year 3 Reading Assessment", "y3/autumn/index.html", 0, "Non-fiction"),
    ("y3-autumn-beached-dreams.pdf",          "Year 3 Reading Assessment", "y3/autumn/index.html", 1, "Poetry"),
    ("y3-autumn-monkeys-and-trunks.pdf",      "Year 3 Reading Assessment", "y3/autumn/index.html", 2, "Fiction"),
    ("y3-summer-inside-outside.pdf",         "Year 3 Reading Assessment", "y3/summer/index.html", 0, "Non-fiction"),
    ("y3-summer-two-little-kittens.pdf",      "Year 3 Reading Assessment", "y3/summer/index.html", 1, "Poetry"),
    ("y3-summer-sit-down-meal.pdf",           "Year 3 Reading Assessment", "y3/summer/index.html", 2, "Fiction"),
    ("y5-autumn-creature-eating-plants.pdf",  "Year 5 Reading Assessment", "y5/autumn/index.html", 0, "Non-fiction"),
    ("y5-autumn-mysterious-pond.pdf",         "Year 5 Reading Assessment", "y5/autumn/index.html", 1, "Fiction"),
    ("y5-autumn-heart-soup.pdf",              "Year 5 Reading Assessment", "y5/autumn/index.html", 2, "Fiction"),
    ("y5-summer-smart-farmers.pdf",           "Year 5 Reading Assessment", "y5/summer/index.html", 0, "Non-fiction"),
    ("y5-summer-the-squall.pdf",              "Year 5 Reading Assessment", "y5/summer/index.html", 1, "Poetry"),
    ("y5-summer-times-table.pdf",             "Year 5 Reading Assessment", "y5/summer/index.html", 2, "Fiction"),
]

TITLE_RE_CACHE = {}


def texts_for(src_file):
    if src_file not in TITLE_RE_CACHE:
        s = open(src_file).read()
        body = re.search(r"const TEXTS\s*=\s*\{(.*?)\n\};", s, re.S).group(1)
        entries = re.findall(r"(\d+):\s*\{\s*title:\s*(['\"])(.*?)\2.*?html:\s*`(.*?)`\s*\}", body, re.S)
        TITLE_RE_CACHE[src_file] = {int(idx): (title, h) for idx, _, title, h in entries}
    return TITLE_RE_CACHE[src_file]


def main():
    os.makedirs(gt.OUTPUT_DIR, exist_ok=True)
    for filename, year_label, src_file, idx, genre in PASSAGES:
        title, html_src = texts_for(src_file)[idx]
        author = author_of(html_src)
        path = os.path.join(gt.OUTPUT_DIR, filename)
        c = canvas.Canvas(path, pagesize=A4)
        pm = PageManagerY(c, title, genre, year_label, author=author)
        render(pm, html_src)
        pm.save()
        print(f"  ✓ {path}")


if __name__ == "__main__":
    main()
