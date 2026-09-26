# Gender-stereotype review, set 4 (levels 32-34).
TEXT_PATCHES = {
 "32-1": [
  ("the solemnity of a man handing over a crown", "the solemnity of a monarch handing over a crown"),
  ("Mrs Okafor", "Mr Okafor"),
 ],
 "32-5": [
  ("in all that time he had never once", "in all that time she had never once"),
  ("Instead he carried water", "Instead she carried water"),
  ("until his fingers cracked", "until her fingers cracked"),
  ("whether he would ever prove", "whether she would ever prove"),
  ("made his wrists ache", "made her wrists ache"),
  ("Haru’s heart leapt as he dipped", "Haru’s heart leapt as she dipped"),
  ("exactly as he had watched", "exactly as she had watched"),
  ("his arms trembling and the cold gnawing at his fingers", "her arms trembling and the cold gnawing at her fingers"),
  ("By afternoon his sheets", "By afternoon her sheets"),
  ("Haru frowned; he had assumed", "Haru frowned; she had assumed"),
 ],
 "33-6": [
  ("A groundsman knelt", "A groundskeeper knelt"),
  ("as gently as if he were tucking a child into bed. By morning, he explained,", "as gently as if tucking a child into bed. By morning, the groundskeeper explained,"),
 ],
 "34-3": [
  ("my mother, weary of finding me", "my dad, weary of finding me"),
 ],
 "34-5": [
  ("A man in a suit that looks slept in stands with his eyes closed, clutching a briefcase against his chest",
   "A woman in a suit that looks slept in stands with her eyes closed, clutching a briefcase against her chest"),
  ("The man with the briefcase steps aboard first", "The woman with the briefcase steps aboard first"),
  ("he tucking the flask into her bag, she straightening his collar", "she tucking the flask into his bag, he straightening her collar"),
 ],
}
PATCHES = {
 ("32-1", 8): {"a": "The narrator was thinking of neighbours who had been kind or were busy: Mr Okafor had left chutney; the couple with twins had no spare time.",
               "g": "1 mark for kindness / sharing / repaying kindness. 1 mark for evidence (Mr Okafor’s chutney or the busy couple with twins)."},
 ("32-5", 3): {"a": "so cold that it made her wrists ache", "g": "Accept “made her wrists ache”."},
 ("32-5", 7): {"a": "Her face burned; she said it was ruined and apologised."},
 ("32-5", 11): {"opts": ["It was gentle.", "It slowly and painfully wore at her fingers.", "It was gone.", "It came and went quickly."]},
 ("32-5", 14): {"a": "Keep it, because Master Sato taught her to remember what it feels like to be bad at something."},
 ("33-6", 8): {"items": ["The floodlights were dimmed before they were switched off.", "The groundskeeper repaired the pitch with a fork.", "The workers were silent.", "The scoreboard was switched off first."]},
 ("33-6", 9): {"q": "The groundskeeper presses the turf back “as gently as if tucking a child into bed”. What does this simile suggest about the groundskeeper, and how does it make the reader feel?",
               "a": "The groundskeeper is caring and gentle towards the pitch; it makes the reader feel warmth and see the pitch as something precious."},
 ("34-3", 13): {"opts": ["A child learns patience, skill and care from a teacher who values quiet work.", "A child dislikes their dad’s choice of Saturday activity.", "A woman asks a bookbinder to mend a Bible.", "A bookbinder decides to sell his workshop."]},
 ("34-5", 4): {"items": ["The cleaner helps the girl with her cello.", "The woman with the briefcase looks back as she boards.", "The pigeon is sitting on a girder in paragraph 2.", "The old couple travel on the train."]},
 ("34-5", 8): {"q": "The woman clutches her briefcase “against her chest as if it were a shield”. What does this suggest about how she feels? Explain your answer.",
               "a": "She feels nervous or defensive (1) because a shield protects someone, so the briefcase is something she uses to protect herself from worry (1)."},
}
