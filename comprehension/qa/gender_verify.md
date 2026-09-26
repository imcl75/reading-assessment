# Gender-edit consistency check (24 tests)

Tests read in full: 18-1, 18-2, 18-3, 19-1, 21-5, 22-1, 22-3, 22-5, 23-3, 24-6, 25-1, 25-4, 26-2, 26-3, 28-3, 30-1, 30-3, 30-4, 31-1, 32-1, 32-5, 33-6, 34-3, 34-5.

## What was checked
For every test: names, pronouns, roles and relationships in the text and in every question, option, item, model answer and guidance; multiple-choice options for a wrong or doubly-right answer; order and true/false keys against the text; paragraph references in questions; leftover wrong pronouns; any new stereotype.

## Fixed (qa_patches_t1.py)
- 18-2 Q5: model answer still said "She ... she could not cross" (Tomasz is now a boy). Now "He ... he".
- 18-3 Q3: order item "Kofi made a cup of tea" was wrong (Dad now makes it). Now "Dad made a cup of tea." Key unchanged.
- 24-6 text: "Grandad ... she announced" changed to "he announced".
- 30-1 text: bus driver is a woman but "he asked" changed to "she asked".
- 32-5 text: "ruined, he said" (Haru is a girl) changed to "she said". Q5 items, Q7 and Q14 said "his" for Haru; now "her".
- 22-5 Q11: distractor "A girl wins every race" implied a gender for the neutral narrator. Now "A child".
- 31-1 Q13: with mother now the shepherd, "A shepherd's daughter builds a sledge and a library" was arguably true (nearly doubly right). Now "loses her flock in the snow". Answer D unchanged.

## Checked and fine
All other tests: pronouns, roles, keys and paragraph references consistent. No new stereotype found (roles are now mixed: Dad calls children in and makes tea, mum is a shepherd and builds shelves, a boy is the nervous one in 18-2, a girl apprentice, women drivers and coaches).

## Unsure
- 18-3: Dad appears mid-story and makes the tea while "the house was quiet"; reads acceptably but slightly abrupt.
- 22-3: "the one that you gave me" (Ellie gave Ravi a biscuit) is plausible but unstated elsewhere.
- 28-3 Q9 guidance says Mrs Okafor "quickly arranged" for Jin; the text just says "We shall ask Jin". Pre-existing looseness, left alone.
