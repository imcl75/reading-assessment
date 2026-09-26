# Child-friendly review, set u3 (24 tests, levels 28-31)

## Found
- Unneeded clock times, dates and old-money detail that make texts hard to picture: 28-3, 28-6, 29-4, 29-6, 30-1, 30-2, 30-4, 30-5.
- One adult term with no support in the text: "shareholders" (29-3).
- One piece of background knowledge the text never gives: "the French Revolution" (30-5).
- No Americanisms found. Vocabulary is UK throughout (torch, till, trainers, crocodile clips, carrier bag, squash).

## Changed (qa_patches_u3.py, 9 tests, all validated)
- 28-3: "at twelve" became "at lunchtime"; "began at ten ... after one o'clock" became "began in the morning ... until after lunchtime"; "At half past two" became "Later that afternoon". Q1 guidance and the Q4 item 1 no longer say ten o'clock. Answers unchanged.
- 28-6: "17 December 1903" became "a December morning in 1903"; "half past ten" became "Later that morning". The year stays.
- 29-3: "no shareholders" became "no tills".
- 29-4: "half past eight" and "ten o'clock" became "early" and "later that morning".
- 29-6: dropped "half an ounce", the day-of-month dates (1 and 6 May) and the "240 pennies in a pound" detail. The years 1837, 1839, 1840 stay.
- 30-1: "almost half past nine" became "late at night".
- 30-2: "half past five" became "first light".
- 30-4: "since five to nine" became "since before the register began".
- 30-5: "31 March 1889" became "the spring of 1889"; "January 1887" became "1887"; "to mark a hundred years since the French Revolution" became "to show off amazing new inventions from around the world".

## Left alone, and why
- Times, dates and numbers that questions test, or that are the point of the text: 30-1 Q3 (three months), 30-5 (1909, 1930, rivets), 30-6 Q4 (1892), 28-6 Q13 (fifty-nine seconds), 31-1 (ages, miles, years).
- Challenging vocabulary kept: perforated, petitions, decipher, serrated, meticulous, total internal reflection, lattice, vigil, forgoes.
- Morse code (31-4) is explained in the text as dots and dashes. Wigwam (30-2) and "taxpayers" (29-3) are widely known and do not stop the answer.
- Levels 28 and 31 others (28-1, 28-2, 28-4, 28-5, 29-1, 29-2, 29-5, 30-3, 30-6, 31-1 to 31-6): no clear problems. UK money and place references (pounds, Coldharbour Lane, council, food bank) are familiar to UK children.
- Gender-balance fixes untouched.
