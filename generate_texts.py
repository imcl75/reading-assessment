"""
generate_texts.py
Generates A4 reading assessment booklet PDFs for Wallscourt Farm Academy.
Uses ReportLab canvas only (no Platypus/flowables).
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
import os

# ── Constants ────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4           # 595.28 × 841.89
MARGIN_L = 50
MARGIN_R = 50
MARGIN_TOP = 50
MARGIN_BOT = 40
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R   # 495.28
CONTENT_X = MARGIN_L                        # 50
CONTENT_RIGHT = PAGE_W - MARGIN_R          # 545.28

BRAND = (0.09, 0.596, 0.827)   # #1798d3
DARK  = (0.2, 0.2, 0.2)
GREY  = (0.5, 0.5, 0.5)
LGREY = (0.85, 0.85, 0.85)
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)

HEADER_H = 36      # blue header rectangle height
FOOTER_Y  = 40     # bottom of footer area
SCHOOL_NAME = "Wallscourt Farm Academy"
OUTPUT_DIR = "/Users/innes/Desktop/claude_code/reading-assessment/texts"


# ── Low-level helpers ─────────────────────────────────────────────────────────

def set_fill(c, rgb):
    c.setFillColorRGB(*rgb)

def set_stroke(c, rgb):
    c.setStrokeColorRGB(*rgb)

def string_width(c, text, font, size):
    return c.stringWidth(text, font, size)


# ── Header & Footer ───────────────────────────────────────────────────────────

def draw_header(c, title, page_num=1):
    """Draw blue header bar with school name and title."""
    # Blue rectangle: top at PAGE_H - MARGIN_TOP, height 36
    hx = MARGIN_L
    hy_bottom = PAGE_H - MARGIN_TOP - HEADER_H   # bottom of header rect
    set_fill(c, BRAND)
    c.rect(hx, hy_bottom, CONTENT_W, HEADER_H, fill=1, stroke=0)

    # White text in header
    set_fill(c, WHITE)
    c.setFont("Helvetica", 9)
    # Baseline at centre of header: hy_bottom + HEADER_H/2 - 9*0.5*0.72
    text_baseline = hy_bottom + HEADER_H / 2 - 9 * 0.72 / 2
    c.drawString(hx + 8, text_baseline, SCHOOL_NAME)
    tw = string_width(c, title, "Helvetica", 9)
    c.drawRightString(hx + CONTENT_W - 8, text_baseline, title)


def draw_title_block(c, title, genre, author=None):
    """Draw big centred title + genre badge below header. Returns y below badge."""
    # Title text: 18pt bold, brand colour, centred
    # Baseline: HEADER_BOTTOM - 8pt gap - ascender
    header_bottom = PAGE_H - MARGIN_TOP - HEADER_H
    title_baseline = header_bottom - 8 - 18 * 0.72
    set_fill(c, BRAND)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(PAGE_W / 2, title_baseline, title)
    title_bottom = title_baseline - 18 * 0.12   # descender clearance

    # Author line (poems)
    if author:
        author_baseline = title_bottom - 4 - 10 * 0.72
        set_fill(c, GREY)
        c.setFont("Helvetica-Oblique", 10)
        c.drawCentredString(PAGE_W / 2, author_baseline, author)
        title_bottom = author_baseline - 10 * 0.12

    # Genre badge: pill shape below title
    badge_text = genre
    c.setFont("Helvetica", 9)
    btw = string_width(c, badge_text, "Helvetica", 9)
    badge_w = btw + 20
    badge_h = 16
    badge_x = PAGE_W / 2 - badge_w / 2
    badge_y_bottom = title_bottom - 6 - badge_h
    # Draw pill (rounded rect)
    set_fill(c, WHITE)
    set_stroke(c, BRAND)
    c.setLineWidth(1)
    c.roundRect(badge_x, badge_y_bottom, badge_w, badge_h, radius=8, fill=1, stroke=1)
    set_fill(c, BRAND)
    badge_text_baseline = badge_y_bottom + badge_h / 2 - 9 * 0.72 / 2
    c.drawCentredString(PAGE_W / 2, badge_text_baseline, badge_text)

    return badge_y_bottom - 10   # 10pt gap below badge


def draw_footer(c, page_num):
    """Draw grey footer line + text."""
    set_stroke(c, GREY)
    c.setLineWidth(0.5)
    c.line(MARGIN_L, FOOTER_Y + 12, CONTENT_RIGHT, FOOTER_Y + 12)
    set_fill(c, GREY)
    c.setFont("Helvetica", 8)
    footer_baseline = FOOTER_Y
    c.drawString(MARGIN_L, footer_baseline, "Year 4 Reading Assessment")
    c.drawRightString(CONTENT_RIGHT, footer_baseline, f"Page {page_num}")


def start_page(c, title, genre, page_num, author=None):
    """Begin a page: draw header, footer, title block. Return content_top y."""
    draw_header(c, title, page_num)
    draw_footer(c, page_num)
    content_top = draw_title_block(c, title, genre, author=author)
    return content_top


# ── Text wrapping helpers ─────────────────────────────────────────────────────

def wrap_words(c, text, font, size, max_width):
    """Split text into lines that fit within max_width. Returns list of (line_str, words)."""
    words = text.split()
    lines = []
    current = []
    current_w = 0
    space_w = string_width(c, " ", font, size)
    for word in words:
        ww = string_width(c, word, font, size)
        if current and current_w + space_w + ww > max_width:
            lines.append(current)
            current = [word]
            current_w = ww
        else:
            current.append(word)
            current_w = current_w + (space_w if current_w else 0) + ww
    if current:
        lines.append(current)
    return lines


def draw_justified_line(c, words, x, y, max_width, font, size, is_last=False):
    """Draw a line of text, justified unless it's the last line."""
    if not words:
        return
    if is_last or len(words) == 1:
        c.setFont(font, size)
        c.drawString(x, y, " ".join(words))
        return
    total_text_w = sum(string_width(c, w, font, size) for w in words)
    total_space = max_width - total_text_w
    gap = total_space / (len(words) - 1)
    cx = x
    for i, word in enumerate(words):
        c.setFont(font, size)
        c.drawString(cx, y, word)
        cx += string_width(c, word, font, size) + gap


def draw_paragraph(c, text, x, y_top, max_width, font="Helvetica", size=12,
                    leading=18, justify=True, colour=BLACK):
    """
    Draw a paragraph of wrapped text.
    y_top = top of first line (ascender will be at y_top, baseline = y_top - ascender).
    Returns y_bottom (baseline of last line minus descender).
    """
    lines = wrap_words(c, text, font, size, max_width)
    ascender = size * 0.72
    baseline = y_top - ascender
    set_fill(c, colour)
    for i, words in enumerate(lines):
        is_last = (i == len(lines) - 1)
        if justify:
            draw_justified_line(c, words, x, baseline, max_width, font, size, is_last)
        else:
            c.setFont(font, size)
            c.drawString(x, baseline, " ".join(words))
        baseline -= leading
    # After loop baseline has moved one extra leading past last line
    last_baseline = baseline + leading
    return last_baseline - size * 0.12   # bottom including descender


def draw_heading(c, text, x, y_top, size=11, colour=BRAND, font="Helvetica-Bold",
                 gap_above=10, gap_below=4):
    """Draw a section heading. y_top is where content above ended (bottom of prev element).
    Returns y below heading (after gap_below)."""
    y_top_with_gap = y_top - gap_above
    ascender = size * 0.72
    baseline = y_top_with_gap - ascender
    set_fill(c, colour)
    c.setFont(font, size)
    c.drawString(x, baseline, text)
    return baseline - size * 0.12 - gap_below


def draw_bullet(c, text, x, y_top, size=11, leading=14, max_width=None, colour=BLACK):
    """Draw a bullet point. Returns y_bottom."""
    if max_width is None:
        max_width = CONTENT_W - 16
    indent = 16
    ascender = size * 0.72
    baseline = y_top - ascender
    set_fill(c, colour)
    c.setFont("Helvetica", size)
    bullet_x = x + 4
    text_x = x + indent
    c.drawString(bullet_x, baseline, "•")
    # Wrap text
    lines = wrap_words(c, text, "Helvetica", size, max_width - indent)
    for i, words in enumerate(lines):
        c.drawString(text_x, baseline, " ".join(words))
        baseline -= leading
    last_baseline = baseline + leading
    return last_baseline - size * 0.12


# ── Page manager ──────────────────────────────────────────────────────────────

class PageManager:
    """Tracks current y position and handles page breaks."""

    def __init__(self, c, title, genre, author=None, body_size=12, body_leading=18):
        self.c = c
        self.title = title
        self.genre = genre
        self.author = author
        self.body_size = body_size
        self.body_leading = body_leading
        self.page_num = 1
        self.y = None   # current top-of-available-space y
        self._new_page()

    def _new_page(self):
        if self.page_num > 1:
            self.c.showPage()
        self.y = start_page(self.c, self.title, self.genre, self.page_num,
                            author=self.author if self.page_num == 1 else None)
        self.page_num += 1

    def min_y(self):
        return FOOTER_Y + 20   # minimum y before we need a new page

    def ensure_space(self, needed):
        """If we don't have `needed` pt of vertical space, start a new page."""
        if self.y - needed < self.min_y():
            self._new_page()

    def add_space(self, pts):
        self.y -= pts

    def draw_para(self, text, justify=True, font=None, size=None, leading=None,
                  colour=BLACK, indent=0):
        if not text.strip():
            return
        f = font or "Helvetica"
        s = size or self.body_size
        l = leading or self.body_leading
        mw = CONTENT_W - indent
        # Estimate lines needed
        lines_est = max(1, len(wrap_words(self.c, text, f, s, mw)))
        needed = lines_est * l + s * 0.72 + 4
        self.ensure_space(needed)
        bottom = draw_paragraph(self.c, text, CONTENT_X + indent, self.y, mw,
                                font=f, size=s, leading=l, justify=justify, colour=colour)
        self.y = bottom
        self.add_space(4)   # gap after paragraph

    def draw_h3(self, text):
        self.ensure_space(30)
        self.y = draw_heading(self.c, text, CONTENT_X, self.y, size=11,
                              colour=BRAND, font="Helvetica-Bold",
                              gap_above=10, gap_below=4)

    def draw_h4(self, text):
        self.ensure_space(25)
        self.y = draw_heading(self.c, text, CONTENT_X, self.y, size=10,
                              colour=(0.2, 0.2, 0.2), font="Helvetica-Bold",
                              gap_above=8, gap_below=3)

    def draw_bullet(self, text):
        self.ensure_space(20)
        bottom = draw_bullet(self.c, text, CONTENT_X, self.y,
                             size=11, leading=14,
                             max_width=CONTENT_W, colour=BLACK)
        self.y = bottom
        self.add_space(2)

    def draw_poetry_stanza(self, lines):
        """Draw a poetry stanza (list of strings). Left-aligned, italic."""
        needed = len(lines) * self.body_leading + self.body_size * 0.72 + 4
        self.ensure_space(needed)
        ascender = self.body_size * 0.72
        baseline = self.y - ascender
        set_fill(self.c, BLACK)
        for line in lines:
            self.c.setFont("Helvetica-Oblique", self.body_size)
            self.c.drawString(CONTENT_X, baseline, line)
            baseline -= self.body_leading
        self.y = baseline + self.body_leading - self.body_size * 0.12
        self.add_space(self.body_leading)   # stanza gap — one full blank line

    def draw_contact_block(self, lines):
        """Draw a contact info block in a light grey tinted box."""
        box_pad = 10
        # Estimate height
        total_h = box_pad * 2 + len(lines) * 14 + 4
        self.ensure_space(total_h + 10)
        self.add_space(8)
        box_x = CONTENT_X
        box_y_top = self.y
        box_y_bottom = box_y_top - total_h
        # Draw box
        set_fill(self.c, (0.95, 0.95, 0.95))
        set_stroke(self.c, (0.8, 0.8, 0.8))
        self.c.setLineWidth(0.5)
        self.c.rect(box_x, box_y_bottom, CONTENT_W, total_h, fill=1, stroke=1)
        # Draw text
        set_fill(self.c, DARK)
        self.c.setFont("Helvetica", 10)
        ty = box_y_top - box_pad - 10 * 0.72
        for line in lines:
            self.c.drawString(box_x + box_pad, ty, line)
            ty -= 14
        self.y = box_y_bottom - 4

    def draw_table(self, rows, col_widths=None):
        """Draw a simple two-column table with alternating row shading."""
        if col_widths is None:
            col_widths = [CONTENT_W * 0.45, CONTENT_W * 0.55]
        row_h = 20
        total_h = row_h * len(rows) + 4
        self.ensure_space(total_h + 12)
        self.add_space(8)
        tx = CONTENT_X
        ty_top = self.y
        for i, row in enumerate(rows):
            row_y_bottom = ty_top - (i + 1) * row_h
            # Alternating shading
            if i % 2 == 0:
                set_fill(self.c, (0.93, 0.93, 0.93))
            else:
                set_fill(self.c, WHITE)
            self.c.rect(tx, row_y_bottom, CONTENT_W, row_h, fill=1, stroke=0)
            # Cell borders
            set_stroke(self.c, (0.75, 0.75, 0.75))
            self.c.setLineWidth(0.3)
            self.c.rect(tx, row_y_bottom, CONTENT_W, row_h, fill=0, stroke=1)
            # Text
            set_fill(self.c, DARK)
            self.c.setFont("Helvetica", 11)
            text_baseline = row_y_bottom + row_h / 2 - 11 * 0.72 / 2
            cx = tx + 6
            for j, cell in enumerate(row):
                self.c.drawString(cx, text_baseline, str(cell))
                cx += col_widths[j]
        self.y = ty_top - total_h - 4

    def save(self):
        self.c.save()


# ── PDF generators ────────────────────────────────────────────────────────────

def gen_making_waves():
    path = os.path.join(OUTPUT_DIR, "summer-making-waves.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "Making Waves", "Non-fiction")

    pm.draw_para(
        "It's finally here! The new pool is now open at the Ranchester Leisure Centre. "
        "Why not dip your toe in this fantastic new facility and see how much fun swimming can be?"
    )

    pm.draw_h3("Laughter ahoy!")
    pm.draw_para(
        "The Blue Lagoon is a pirate-themed pleasure pool that whisks you off to a tropical paradise, "
        "complete with a wave machine and scramble slide. While toddlers paddle in the relaxing baby pool, "
        "the more adventurous can risk a soaking from tipping buckets as they are swept around Parrot Creek, "
        "our indoor river feature."
    )
    pm.draw_para(
        "Are you brave enough to try our high-speed flumes, Redbeard and Blackbeard, as they whoosh around "
        "the many twists and turns before splashing down into the plunge pool?"
    )

    pm.draw_h3("Opening Times")
    pm.draw_table([
        ["Monday – Friday", "9.00am to 11am and 3pm to 5.00pm"],
        ["Saturdays, Sundays and School Holidays", "8.30am to 6.00pm"],
    ])

    pm.draw_h4("Parties that go swimmingly")
    pm.draw_para(
        "Want a birthday to remember? Then why not hire the Lagoon for your own private party after "
        "everyone else has gone home? As well as letting you have the pleasure pool to yourselves, "
        "we'll throw in a selection of floats and other water toys."
    )
    pm.draw_para(
        "Once you're all dried and dressed, we'll lay on a delicious party tea in our café, including "
        "a mouth-watering spread of sandwiches, snacks and nibbles (birthday cake is an additional cost)."
    )

    pm.draw_h3("Booking Information")
    pm.draw_para(
        "We will provide pool-side lifeguards for your party. However, responsible adults are expected "
        "to supervise party guests at all times and everyone will need to follow the pool rules or they "
        "may be asked to exit the water for safety reasons."
    )
    pm.draw_para(
        "Prices start at £8 per child for parties of 30 or more up to a maximum of 60; smaller parties "
        "cost £12 per child. Bookings require a £50 deposit and should be made at least a month in advance. "
        "Please contact us for more information."
    )

    pm.draw_contact_block([
        "Email: customerservices@ranchesterleisure.org",
        "Tel: 01433 2828289",
        "(8.30am – 5.00pm, Monday to Saturday)",
    ])

    pm.save()
    print(f"  ✓ {path}")


def gen_field_mouse():
    path = os.path.join(OUTPUT_DIR, "summer-field-mouse.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "The Field Mouse", "Poetry",
                     author="Cecil Frances Alexander")

    stanzas = [
        [
            "Where the acorn tumbles down,",
            "Where the ash tree sheds its berry,",
            "With your fur so soft and brown,",
            "With your eye so round and merry,",
            "Scarcely moving the long grass,",
            "Fieldmouse, I can see you pass.",
        ],
        [
            "Little thing, in what dark den,",
            "Lie you all winter sleeping?",
            "Till warm weather comes again,",
            "Then once more I see you peeping",
            "Round about the tall tree roots,",
            "Nibbling at their fallen fruits.",
        ],
        [
            "Fieldmouse, fieldmouse, do not go,",
            "Where the farmer stacks his treasure,",
            "Find the nut that falls below,",
            "Eat the acorn at your pleasure,",
            "But you must not steal the grain",
            "He has stacked with so much pain.",
        ],
        [
            "Make your hole where mosses spring,",
            "Underneath the tall oak's shadow,",
            "Pretty, quiet harmless thing,",
            "Play about the sunny meadow.",
            "Keep away from corn and house,",
            "None will harm you, little mouse.",
        ],
    ]
    for stanza in stanzas:
        pm.draw_poetry_stanza(stanza)

    pm.save()
    print(f"  ✓ {path}")


def gen_food_chain():
    path = os.path.join(OUTPUT_DIR, "summer-food-chain.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "The Top of the Food Chain", "Fiction", body_size=11, body_leading=16)

    paragraphs = [
        "The pigeon landed in a flurry of feathers and tucked in his wings. Bobbing his head, he strutted "
        "around looking for crumbs – this was not a difficult task as humans often passed this way and often "
        "littered the floor with the remains of their food.",

        "He was not alone. A golden eagle was eyeing him hungrily from a post just a few metres away. As her "
        "two yellow eyes glared down on him, her talons tightened their grip on her perch. Her vicious beak "
        "opened briefly, then closed as if tasting the flavour of her next meal.",

        "The pigeon only noticed the bird of prey when she lazily stretched and flapped her wings, like she "
        "was warming up for take-off. At first, he was alarmed and fluttered upwards in a clumsy panic before "
        "settling back on the ground.",

        "'Keep your feathers on – I've already eaten today,' she lied, as she neatly folded her enormous, "
        "brown wings.",

        "'Me too,' he replied. 'Still, there's plenty of grub just lying around here. Shame to waste it.'",

        "The eagle looked on with contempt as the pigeon continued to peck at the ground.",

        "'Where do you put it all?' she sneered. 'You're so greedy!'",

        "'No need to get personal,' said the pigeon.",

        "'Take a look at me,' continued the eagle, ignoring his reply. 'Here at the top of the food chain, "
        "we have to take care of ourselves. We eagles are built for power and speed. Observe my sleek "
        "feathers; marvel at the span of my wings; tremble at the power of my deadly talons.' With that, "
        "she spread her wings again and gave a more forceful flap in order to prove her point.",

        "'You are indeed a very fine specimen, madam,' agreed the pigeon, humbly. 'Nevertheless, there is "
        "more than one way to judge success. No doubt, I wouldn't last a few seconds if I had to take you on. "
        "But brute strength isn't everything. Look around you: how many eagles do you see? That's right, "
        "just the one.'",

        "'Your point is … ?' asked the eagle, a little impatiently.",

        "'Well, take a peek up there on the roof. I can see three of my friends, but no eagles. Up in that "
        "oak tree, there are another four pigeons, yet none of your kind. Over there by the bench, you'll "
        "find still more of us but not an eagle in sight. What's more, this is the land of the humans – "
        "too dangerous for eagles, but we pigeons are thriving. You see, it's not about sheer, brute "
        "strength; it's about sticking together, being smart and finding new ways to get on. That's how "
        "the weaker ones can show their true worth.'",

        "'Well, clever-claws, all your fine talk won't save you now,' snarled the eagle, spreading her "
        "wings once more and readying herself to snatch the pigeon. 'I'll make you eat your words while I "
        "prove who's the strongest.' But before she could get more than a metre into the air, she was "
        "brought back to her perch with a bump, a rattle and a clinking of metal.",

        "'Oh, and another thing,' continued the pigeon, not in the slightest bit flustered. 'I'm free, "
        "not tied to a post in a zoo. You might be top of the food chain, but I can see another chain. "
        "It's a man-made chain; it's attached to your leg and it's holding you back.'",
    ]

    for para in paragraphs:
        pm.draw_para(para)

    pm.save()
    print(f"  ✓ {path}")


def gen_taking_to_the_stage():
    path = os.path.join(OUTPUT_DIR, "autumn-taking-to-the-stage.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "Taking to the Stage", "Non-fiction")

    pm.draw_para(
        "Have you ever wanted to be someone different? If so, why not have a go at acting? There are lots "
        "of reasons to give it a try. As well as being lots of fun, it can be a great way to meet new "
        "friends and learn some very useful skills."
    )

    pm.draw_h3("Early performers")
    pm.draw_para(
        "Taking to the stage is something that people have been doing for thousands of years. The ancient "
        "Greeks were the earliest actors. One player, Thespis, is thought to have been the first ever person "
        "to have played a part as someone else – not as himself. That is why actors are sometimes called "
        "'thespians', even now."
    )
    pm.draw_para(
        "These days, top actors enjoy great fame and wealth. For some actors, they love performing as "
        "someone else. Others are tempted by the idea of the money and glamorous lifestyle. Most actors "
        "will tell you that it is not an easy job though!"
    )

    pm.draw_h3("Bad reputation")
    pm.draw_para(
        "People haven't always respected actors as we do nowadays. Before the days of Queen Elizabeth I, "
        "they were widely seen as being little better than tramps and crooks. In England, only men and boys "
        "were allowed to act because it was not thought to be a decent job."
    )
    pm.draw_para(
        "Acting changed a great deal for the better when the famous writer, William Shakespeare, arrived "
        "on the scene. Being an actor became much more acceptable and people even started to build permanent "
        "theatres in towns and cities for people to visit."
    )

    pm.draw_h3("Screen actors")
    pm.draw_para(
        "For the last hundred years or so, theatres have had to compete with film and TV. These inventions "
        "meant that it was easier for people to see the world's greatest stars without having to travel "
        "farther than their local cinema. It did mean, however, that actors had to adapt their skills. "
        "After all, on a stage your actions and voice must be louder than life so that they can be seen "
        "and heard by the people at the back. On screen, on the other hand, the camera can be so close "
        "that even the smallest movement will be clearly noticed."
    )

    pm.draw_h4("What you need:")
    pm.draw_para("Acting might have changed over the centuries, but the basic skills you need remain the same:")
    for item in [
        "A good imagination",
        "The confidence to perform in front of crowds",
        "The ability to remember lots of lines",
        "A clear, interesting voice",
    ]:
        pm.draw_bullet(item)

    pm.draw_h4("Advice for getting started:")
    pm.draw_para(
        "When your school is putting on a show, make sure that you audition for a part. If you don't have "
        "any luck, try to find out if there are any drama groups in your area. Alternatively, you could "
        "search the internet for local acting clubs for young people."
    )

    pm.save()
    print(f"  ✓ {path}")


def gen_lead_on():
    path = os.path.join(OUTPUT_DIR, "autumn-lead-on.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "Lead On", "Poetry")

    stanzas = [
        [
            '"Sit!" my gentle giant barks.',
            "A forest of legs above my head:",
            "Like shifting trees, marching by.",
            "Bursts of yellow, green and red,",
            "Switch and shimmer in the air,",
            "A restless rainbow, just hanging there.",
        ],
        [
            "Pause as metal beasts roll by",
            "Until, at last, the traffic slows.",
            "A shining being, dressed in green",
            "Commands the human pack to go.",
            "We surge across the road as one",
            "While shining eyes keep looking on.",
        ],
        [
            "The people herd along the path,",
            "My stumpy legs begin to tire.",
            "If only I could soar and fly",
            "Above the trees, or even higher.",
            "Sounds and smells help me revive,",
            "I sense, at home, we'll soon arrive.",
        ],
        [
            "I've exercised enough today,",
            "The length and vastness of my world.",
            "So now I head straight for my bed.",
            "And follow my tail until I'm curled.",
            "My eyes look sad, but I feel no sorrow:",
            "I'll have another walk tomorrow.",
        ],
    ]
    for stanza in stanzas:
        pm.draw_poetry_stanza(stanza)

    pm.save()
    print(f"  ✓ {path}")


def gen_russian_figurine():
    path = os.path.join(OUTPUT_DIR, "autumn-russian-figurine.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "The Russian Figurine", "Fiction")

    paragraphs = [
        "Mum wouldn't be back from work for another couple of hours. Anita had been left in charge, "
        "but she might as well have been on a different planet – she only had eyes for her phone. She "
        "certainly wasn't interested in talking to her brother.",

        "If only he hadn't said what he'd said to her yesterday, at least he wouldn't have been grounded. "
        "Apparently, there were some words that everyone knew, but no one was allowed to mention, unless "
        "they were sixteen and going through 'a difficult time'. Difficult time? Raul couldn't see what "
        "was so difficult for Anita about lying around on your bed, chatting to your friends all day, every day.",

        "For a moment, he thought about his own mates down there, practising their tricks at the skate park. "
        "But it just made him more fed up. Turning his back on the window, he gazed around the room for "
        "something, anything, to do. There was nothing. They didn't even have a telly now.",

        "He looked around again. Were the boxes by the door full of things to sell or give to charity? "
        "Not that he really cared.",

        "Lacking anything else to do, he looked inside the nearest box. Raul was saddened to find various "
        "little china figures wrapped up in tissue paper. He had given these to mum as a present over the years.",

        "He picked one of them out and turned it over in his hands. As he did so, memories came flooding "
        "back of happier times when Dad was still around. The four of them used to go to the playground "
        "in the park, then have lunch in a burger bar. After that, they would wander through the market, "
        "looking for things that you couldn't find in normal shops. Mum's favourite stall sold antiques "
        "and 'knick-knacks' ('junk' as Dad called it).",

        "One year, a week or two before Mum's birthday, Dad had taken Raul and Anita to the market on "
        "their own to choose a birthday present for Mum. The figure Raul was now holding was the one he "
        "had chosen for her. It was a pretty shepherd girl with a blue bonnet and white, floor-length "
        "dress. He hated it, but Mum adored it.",

        "On the base, he discovered a small hole. For no particular reason, he peered inside. The middle "
        "was smooth and white, and not very interesting. But then something caught his eye. Just where it "
        "narrowed to the neck, he noticed a scrap of paper stuffed into the hollow of the head. But how "
        "could he get it out?",

        "A pair of tweezers provided the answer. After a couple of frustrating fails, he managed to tug it free.",

        "Carefully, he unrolled the scrap to find a hand-written message in a language he didn't understand. "
        "But if he was right, it was a brief letter that looked like it had been written by someone called "
        "'Nicholas' to 'Anastasia'. This was an exciting discovery and not one he was willing to share...",
    ]

    for para in paragraphs:
        pm.draw_para(para)

    pm.save()
    print(f"  ✓ {path}")


def gen_ice_cream():
    path = os.path.join(OUTPUT_DIR, "ks1-history-of-ice-cream.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "The History of Ice Cream", "Non-fiction",
                     body_size=13, body_leading=20)

    pm.draw_h3("How ice cream began")
    pm.draw_para(
        "Long ago, people in ancient China mixed milk and rice together and packed it in snow to make "
        "a cold pudding. People in ancient Rome also mixed snow with honey and fruit."
    )
    pm.draw_para(
        "About 350 years ago, the King of England was given a recipe for a cold, creamy pudding. The "
        "recipe was so precious that the King paid the cook to keep it a secret."
    )
    pm.draw_para("Today, ice cream is usually made from milk, cream and sugar.")

    pm.draw_h3("Keeping ice cream cold")
    pm.draw_para(
        "Before freezers were invented, people had to use blocks of ice to keep things cold. The ice "
        "was brought over from Norway, where there was plenty of it. This was a tricky task as the ice "
        "had to be transported before it melted."
    )

    pm.draw_h3("Ice cream cones")
    pm.draw_para(
        "About 100 years ago, at a big fair in the United States of America, an ice cream seller ran out "
        "of the bowls he used to serve ice cream. Luckily, another man at the fair was selling waffles. "
        "He rolled his waffles into the shape of a cone so that they could hold the ice cream. People loved it!"
    )

    pm.draw_h3("Exciting flavours")
    pm.draw_para(
        "Ice cream is sold in ice cream parlours. You can buy many exciting flavours there – some unusual "
        "ones include lime, cheese and curry! However, chocolate and vanilla are still the most popular flavours."
    )

    pm.draw_h3("Interesting ice cream facts")
    for item in [
        "The United States of America holds a national Ice Cream Day.",
        "In the past, people used to buy a 'penny lick' – a small amount of ice cream served in a glass cup.",
        "New Zealand is the country where people eat the most ice cream.",
        "Norway holds the record for the tallest ice cream cone, which was 3 metres tall!",
    ]:
        pm.draw_bullet(item)

    pm.save()
    print(f"  ✓ {path}")


def gen_new_room_for_william():
    path = os.path.join(OUTPUT_DIR, "ks1-new-room-for-william.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    pm = PageManager(c, "A New Room for William", "Fiction",
                     body_size=13, body_leading=20)

    paragraphs = [
        "William stood in the middle of his new bedroom. The bare walls stared back at him. In his old "
        "room, the walls were covered in pictures. He turned to look out of the window. He could see a "
        "big tree at the end of the garden. In his old garden, there had been a climbing frame. A boy "
        "appeared at the window of the house next door. He waved at William. William ducked down below "
        "the windowsill.",

        "The next day, Mum and William went shopping for wallpaper. William wanted the same as he had in "
        "his old room, but they didn't have it. William walked around the shop slowly. Suddenly, he stopped. "
        "There, on the shelf, was the most amazing wallpaper he had ever seen. It was covered in dinosaurs. "
        '"That one, Mum!" he said. "Can we have that one?"',

        "When they went home, William put the wallpaper roll in the corner of his empty room. Then he "
        "started to unpack the boxes in his room. He found his model dinosaurs and placed them carefully "
        "on the windowsill. The boy next door appeared again. This time, William gave a small wave back.",

        "The next morning, William woke up early. Today was the day the decorating would begin. He was "
        "too excited to stay in bed, so he went downstairs and out into the garden. He stomped along the "
        "path. \"GRRR, I'm a fierce dinosaur!\" he growled.",

        '"RARRR! I\'m an even fiercer dinosaur!" came a voice from the tree.',

        "William looked up. The boy from next door was sitting in the branches. \"I'm Tom,\" said the boy. "
        '"I live next door. This is our tree – it goes from your garden into mine."',

        '"I\'m William," said William. He looked at Tom\'s garden. There was a climbing frame.',

        "They played together all morning. When Mum called William in for lunch, he raced inside. \"Come "
        'and see your room!" said Mum. William ran upstairs. The walls were covered in dinosaurs. '
        '"It\'s brilliant!" he said.',

        "That night, William lay in bed, looking at his wallpaper. The moonlight shone through the curtains "
        "and made the T-rex look like it was chasing the Stegosaurus right across the wall. William smiled "
        "and closed his eyes.",
    ]

    for para in paragraphs:
        pm.draw_para(para)

    pm.save()
    print(f"  ✓ {path}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating reading assessment PDFs...")
    gen_making_waves()
    gen_field_mouse()
    gen_food_chain()
    gen_taking_to_the_stage()
    gen_lead_on()
    gen_russian_figurine()
    gen_ice_cream()
    gen_new_room_for_william()
    print("Done.")
