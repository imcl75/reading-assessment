# Writing spec: reading comprehension tests by book level

You are writing original comprehension tests for a primary school (Wallscourt Farm Academy, UK; pupils aged 6-11).
A pupil takes the test for their **book level (18-34)**, whatever their year group. Teachers use the score to judge
whether a child is on track for reading. Every test is one text plus questions, printed on paper and marked by a teacher.

## Files
- Work only in `~/Desktop/claude_code/reading-assessment/comprehension/`.
- Look at `tests_src.py` first. It holds three finished pilot tests (levels 18, 24, 30). Copy its exact structure.
- Write your tests to the batch file named in your brief (`tests_batch_<x>.py`). Start it with:
  `from tests_src import T, Q2, TF`  then call `T(level, id, title, type, [paragraphs], [questions])` once per test.
- Check your work with `python3 -B check_batch.py tests_batch_<x>.py` and fix every problem it reports until it prints `OK`.
- Do NOT run `build.py`, and do NOT edit any other file. Other writers are working in the same folder.
- Ids look like `19-1`, `19-2` ... The id must start with the level number. Pilot tests already use 18-1, 24-1, 30-1,
  so for those three levels start at -2.
- Use Unicode escapes for curly quotes as the pilots do (`“ ” ’`), UK spelling, and double quotes for Python strings.

## Every level needs six tests (the three pilot levels need five more)
- Alternate genres: three fiction and three non-fiction per level (counting the pilot where one exists).
  Fiction types: Narrative, Recount (Fictional), Description. Non-fiction types: Information Report, Explanation,
  Exposition, Discussion, Recount (Historical), Procedural. Set `type` to one of those words.
- Use varied settings, characters and topics. Use a range of names that reflect a diverse UK school.
- Texts are **out of context** assessments: they test reading, not prior knowledge. Everything needed to answer must be in
  the text. Do not rely on background knowledge of a topic, a book or the curriculum.
- All content must be child-safe and calm in tone: no violence, death, frightening or upsetting themes.
- Non-fiction facts must be accurate and well established. If you are not certain of a fact, do not use it.
- Never reuse these topics (already used): snow/mittens, bats/echolocation, a night bus/grandmother/locket, kites, hedgehogs,
  swimming club, market day, fishing, volcanoes, talent show, recycling, lighthouse/storms, honeybees, scholarship letter,
  phones for children, odd socks, tides, violin auction, zoos.
- Within your own batch, every test must have a different topic.

## Text length (checked automatically, +/-8%)
Target words by level: 18: 250, 19: 275, 20: 300, 21: 325, 22: 350, 23: 375, 24: 400, 25: 425, 26: 450, 27: 475,
28-34: 500. Split the text into sensible paragraphs.

## Difficulty
The book level matches the PM Benchmark reading levels the school uses (Reading Recovery levels; book bands
Turquoise 17-18, Purple 19-20, Gold 21-22, White 23-24, Lime 25-26, Ruby 27-28, Sapphire 29-30, Star Reader 31+).
Calibrate vocabulary and sentence complexity by reading the real benchmark texts for your levels
(`pdftotext -layout` on the PDFs in `~/Downloads/Benchmarking/Blue/` and `.../Red/`, files named `<level>_*.pdf`).
Use them ONLY to judge difficulty. Never copy or closely imitate them. For levels 31-34 there are no benchmark texts:
go a clear step harder than level 30 (more abstract vocabulary, longer and more complex sentences, subtler inference,
more figurative language, less signposting). Difficulty must rise steadily from level to level.

## Questions (number per level is checked automatically)
Questions per test: 18-19: 10; 20-21: 11; 22-24: 12; 25-26: 13; 27 and above: 14.

Fields: `d` domain, `k` kind, `m` marks, `q` question, `a` model answer, `g` marking guidance, plus `opts` (mc) or `items` (order, tf).
- Domains: `2a` vocabulary, `2b` retrieval, `2c` summarise/sequence, `2d` inference, `2e` predict, `2g` language/word choice.
- Every test needs: at least one 2a, at least one 2c, at least three 2d, mostly 2b retrieval, and where the level allows it
  one 2g or 2e. Rough mix: 40% retrieval, 25-30% inference, 10-15% vocabulary, 10% summarise/sequence, rest language/predict.
- Kinds: `find` (find and copy a word or phrase: the answer must appear word for word in the text),
  `mc` (exactly four options, `a` is the letter A-D), `short` (written answer: always give `g` guidance listing accepted answers),
  `order` (number 4 events 1-4; `items` in a shuffled order and `a` is the list of numbers), `tf` (true/false table; `items` are
  statements and `a` a list of "T"/"F"). Use each of mc, short, order/tf, find across a test.
- Multiple choice: distractors must be plausible; vary the correct letter across a test (do not put it in the same slot each time).
- Language must be clear and child-friendly. Ask about the paragraph or line number when it helps ("In paragraph 2...").
- **Marks:** normally every question is 1 mark. `order` and `tf` are 1 mark, awarded only when the whole answer is correct.
  Levels 18-24: ALL questions are 1 mark. Levels 25-28: a question may be 2 marks only if it asks for two separate things and
  the word "two" appears in the question ("Give two reasons...", mark scheme 1 mark each). Levels 29 and above: 2-mark questions are allowed
  for a point plus supporting evidence, but use them sparingly (no more than 5 per test).
- Levels 18-22 use KS1-style question wording: simple who/what/where/why, retrieval, simple inference.
  From level 23 add KS2-style question types. Levels 29+ should include authorial choice and language effect questions.
- Write the model answer and `g` so a teacher can mark quickly and consistently. Say what to accept and, where useful, what not to.
- Inference questions must genuinely need the reader to combine clues; the answer must not be word for word in the text.

## Quality bar
Texts should read like good children's writing: a clear shape (beginning, development, ending or a logical structure), some
vivid detail, natural dialogue in fiction, and no padding. Read your own texts back before finishing. When the checker passes,
reply with a very short summary: the files written, the number of tests, and anything you were unsure about.

## Reading difficulty target (added after review) and replacement batches
- `check_batch.py` now checks each text's Flesch-Kincaid grade against a target for its level and type (fiction = Narrative /
  Recount (Fictional); non-fiction; Description sits midway). Your text must land within the range it prints. The main way to raise
  the grade is longer, more complex sentences (subordinate clauses, varied openers), richer and more precise vocabulary and less
  simple dialogue tagging. Do not just add long words: it must still read naturally.
- Levels 31-34 are shown to teachers as F1-F4 (Free Reader). F1 and F2 continue level 30 and are only slightly harder; F3 and F4 lean
  towards the reading tests children sit at the end of Key Stage 2 (SATs style).
- A rewrite or replacement batch reuses the id of the test it replaces (for example `25-4`): the later file wins. Keep the same level and id.
  The existing version of each test is in the earlier `tests_batch_*.py` files if you want to see it. `TITLES_IN_USE.txt` lists every title
  and topic already used: never reuse a topic, and never reuse a title.
