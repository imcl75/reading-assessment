# Gender review, set 3 (24 tests, levels 28-31)

## Patterns found
- Mum as the default kitchen/tea-towel figure (28-3) and as the worrier (30-1).
- Mother-as-seamstress with thread, father-as-shepherd (31-1).
- Mothers alone named as the meerkat pups' carers (30-3).
- Male bus driver with a woman carrying a shopping trolley (30-1).
- "Girl's voice" and "as deeply as she could" (a gendered voice joke); neat-handwriting girl (Amira) with a boy who struggles to read (30-4).

## Changes made (qa_patches_s3.py)
- 28-3: Dad, not Mum, comes in from the kitchen drying his hands. Mum still appears (phone message). Q5 item, Q6 and Q10 option updated to Dad.
- 30-1: driver is now a woman (text, "her glasses", Q8 wording); passenger carries a guitar case; "Her dad had warned her".
- 30-3: "the mothers" now "the parents".
- 30-4: "girl's voice" now "an impression of Amira"; "deeply" now "gruffly" (Q6 wording matched); the praised handwriting is now Callum's (as "Amira"), so the boy who stumbles over reading is also the neat writer.
- 31-1: her mother was a shepherd and her father a tailor (reels of thread now her father's). Questions still correct (Q4 shopkeeper item still false; Q13 distractor unaffected).
- All word counts within 3 words; check_patches.py passes.

## Who does what (named or clearly gendered characters with a role)
| Test | Before F / M | After F / M |
|---|---|---|
| 28-3 | Mrs Okafor, Mum, Auntie Grace / Marcus, Grandad, Jin (3/3) | Okafor, Mum, Grace / Marcus, Grandad, Jin, Dad (3/4); Dad now does kitchen and the reminder, Mum still present |
| 30-1 | Nadia, grandmother, Mum, woman passenger / driver, man passenger (4/2) | Nadia, grandmother, driver, woman passenger / Dad (mentioned), man passenger (4/2); Dad now the worrier |
| 30-4 | Miss Baker, Amira, Priya / Mr A-C, Dev, Callum, Tobias (3/4) | unchanged counts; trait split fixed |
| 31-1 | Agnes, mother / father, postman, shopkeeper (2/3) | Agnes, mother / father, postman, shopkeeper; mother now shepherd, father tailor |
Other stories were already balanced: 28-1 (Mika leads, Mr Adeyemi mentors), 28-5 (Amara / Uncle Femi), 29-2 (Efua and Aunt Yaa, a river ranger, calm the impatient Kofi), 30-2 (Zara solves the mystery; Mr Hendry gardens tenderly, his wife is the original gardener), 31-6 (Ines, Mrs Bhatt), 31-2 (Yasmin Farooqui writes). 29-4 and 29-5 have unspecified narrators.

## Left alone, and why
- 28-6 (Wright brothers, all male), 30-5 (Eiffel), 30-6 (Dewar), 29-1 (Newton): real people, facts cannot change. These four historical/scientific texts have only male named people; 29-6 has Rowland Hill and Queen Victoria. Worth adding female-led historical texts in a later set.
- 31-1: "postwoman" and "a young woman could not possibly manage it" stay: the story is about her breaking that expectation and the title/questions use them. "The valley's postman" stays for the same reason.
- 28-1 "a tall man", 30-2 "old man": Mr Adeyemi and Mr Hendry are already male by name; the nouns add no stereotype.
- 28-3 Marcus (chess), 29-2 Kofi (rushing), 30-4 Dev (schemer): each has a capable or equally-flawed character of the other gender beside them; no trait is assigned by gender alone.
- 30-1 "Where to, love?" is ordinary speech from a woman driver and a woman passenger; left.
