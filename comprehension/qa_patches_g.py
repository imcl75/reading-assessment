# Safety: young children should not be shown handling a kettle of hot water on their own.
TEXT_PATCHES = {
 "18-3": [("Kofi filled the kettle, and he was very careful with the hot water. He made a cup of tea just the way Mum liked it,",
           "Dad filled the kettle for them and made a cup of tea just the way Mum liked it,")],
}

# Fact-check: avoid details that history does not record.
TEXT_PATCHES["28-6"] = [("The little group on the beach cheered.", "The small group on the beach had just watched history being made.")]
TEXT_PATCHES["26-6"] = [("He spent many hours at night in the workshop, pressing dots into paper with a sharp tool called an awl.", "He spent many hours working on the problem, pressing dots into paper with a sharp tool called an awl.")]
PATCHES = {
 ("26-6", 8): {"a": "He spent many hours working on the problem / he longed for a faster way to read / he found the answer at fifteen.",
               "g": "Accept any answer showing that he kept working hard until he had solved the problem."},
}

# 30-1 (pilot) was the easiest level-30 test; lift its complexity slightly without touching anything the questions quote.
TEXT_PATCHES["30-1"] = [
 ("She tugged her coat tighter and glanced at the small suitcase by her feet.", "She tugged her coat tighter around her shoulders and glanced anxiously at the small suitcase that rested against her feet."),
 ("She found a seat by the window and pressed her forehead against the cool glass.", "She found a seat by the window and pressed her forehead against the cool glass, watching her own faint reflection drift across the darkened shop fronts."),
 ("The village was silent except for the distant hoot of an owl.", "The village lay silent except for the distant, mournful hoot of an owl."),
 ("Nothing was going to spoil this surprise.", "Nothing, she had decided, was going to spoil this surprise, however long or lonely the journey might be."),
 ("Nadia hesitated. “My grandmother,” she said at last.", "Nadia hesitated, unsure how much to reveal to a stranger. “My grandmother,” she said at last."),
]
