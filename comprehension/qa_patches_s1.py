# Gender-stereotyping review, set 1 (levels 18-22)
TEXT_PATCHES = {
 # Mum was the default "call the children in" carer; Dad now does it.
 "18-1": [("Then Mum called from the back door.", "Then Dad called from the back door.")],
 # Fearful girl comforted by a brave boy: roles swapped so a boy is the nervous one and a girl the steady friend.
 "18-2": [
  ("Amara had never seen anything so exciting.", "Tomasz had never seen anything so exciting."),
  ("Amara climbed up the ladder, but she stopped at the top.", "Tomasz climbed up the ladder, but he stopped at the top."),
  ("Her legs felt shaky, and she looked down", "His legs felt shaky, and he looked down"),
  ("she whispered. She climbed back down and sat on a bench. She watched", "he whispered. He climbed back down and sat on a bench. He watched"),
  ("Her friend Tomasz waved from the top, but Amara pretended not to see him.", "His friend Amara waved from the top, but Tomasz pretended not to see her."),
  ("Soon Tomasz came and sat beside her.", "Soon Amara came and sat beside him."),
  ("at first,” he said.", "at first,” she said."),
  ("Amara took a deep breath. Slowly, she climbed the ladder again. Step by step, she crept", "Tomasz took a deep breath. Slowly, he climbed the ladder again. Step by step, he crept"),
  ("but Tomasz was right in front of her, and he kept saying", "but Amara was right in front of him, and she kept saying"),
  ("At the end, Amara jumped onto the platform and laughed. “I did it!” she shouted. Then she whooshed down the slide with her arms in the air. When the bell rang, she did not want to go in. “Can we do it again tomorrow?” she asked.",
   "At the end, Tomasz jumped onto the platform and laughed. “I did it!” he shouted. Then he whooshed down the slide with his arms in the air. When the bell rang, he did not want to go in. “Can we do it again tomorrow?” he asked."),
 ],
 # Flower-picking and tray-carrying spread more evenly between the two children.
 "18-3": [
  ("Abena picked a flower", "Kofi picked a flower"),
  ("flowers,” she said.", "flowers,” he said."),
  ("Kofi carried it up the stairs very slowly.", "Abena carried it up the stairs very slowly."),
  ("“Oh dear,” said Kofi. Abena quickly wiped", "“Oh dear,” said Abena. Kofi quickly wiped"),
 ],
 # Needlessly gendered nouns / all-male farm staff.
 "19-1": [
  ("a woman showed us", "a keeper showed us"),
  ("cool,” he told us", "cool,” she told us"),
 ],
 "21-5": [("A man beside the fountain played", "A musician beside the fountain played")],
 # Fearful girl / clever boy detective: Ellie is now the confident one.
 "22-3": [("whispered Ellie nervously.", "said Ellie, folding her arms.")],
 "22-1": [
  ("the two girls were laughing", "the two friends were laughing"),
  ("the dinner lady turned round", "the lunchtime supervisor turned round"),
 ],
}

PATCHES = {
 ("18-1", 10): {"q": "Dad said, “Your cheeks are as red as apples.” What does this tell you about Lily’s and Sam’s cheeks?"},

 ("18-2", 2): {"q": "Find and copy one word that tells you how Tomasz’s legs felt at the top of the ladder."},
 ("18-2", 3): {"q": "Who came and sat beside Tomasz on the bench?", "a": "Amara.", "g": "Accept Amara."},
 ("18-2", 4): {"items": ["Tomasz crossed the rope bridge.", "Amara said she would go first.", "Tomasz stopped at the top of the ladder.", "Tomasz sat on the bench."]},
 ("18-2", 5): {"q": "Why do you think Tomasz pretended not to see Amara wave?"},
 ("18-2", 7): {"q": "How can you tell that Amara is a kind friend? Give one piece of evidence.",
               "a": "She sat beside Tomasz / she said it was scary for her too / she went first / she kept saying “Nearly there!”."},
 ("18-2", 8): {"items": ["The new climbing frame had a tall slide.", "Tomasz crossed the bridge on his own.", "Amara said the bridge was scary for her too."]},
 ("18-2", 9): {"q": "How did Tomasz feel at the end of the story? How can you tell?",
               "a": "Happy / proud / excited, because he laughed, shouted “I did it!” and wanted to do it again."},
 ("18-2", 10): {"q": "What do you think Tomasz will do at playtime tomorrow?"},

 ("18-3", 3): {"items": ["Tea spilled on the tray.", "Kofi made the toast.", "Kofi made a cup of tea.", "Kofi put a flower in a glass."]},
 ("18-3", 7): {"q": "Why do you think Abena carried the tray up the stairs very slowly?",
               "a": "She did not want to spill the tea / drop the tray."},
 ("18-3", 10): {"items": ["Kofi picked a flower from the garden.", "Abena dropped the whole tray.", "The children made cereal for breakfast."]},

 ("21-5", 6): {"items": ["Mei made her lantern at school.", "A musician played a flute beside the fountain.", "Mei’s grandfather stood beside her at the lake."]},

 ("22-1", 8): {"items": ["Amara added ears and a tail to the circle.", "Maya was new to the school.", "The lunchtime supervisor laughed loudly.", "Maya said she would bring more paper."]},

 ("22-5", 4): {"g": "Accept: their cheeks felt hot / they felt their cheeks burn."},
}
