# Consistency fixes after the gender-stereotype review (set t1)
PATCHES = {
 ("18-2", 5): {"a": "He felt scared or embarrassed because he could not cross the bridge.",
               "g": "Accept any answer about feeling scared, upset or embarrassed, or not wanting to be asked to cross the bridge."},
 ("18-3", 3): {"items": ["Tea spilled on the tray.", "Kofi made the toast.", "Dad made a cup of tea.", "Kofi put a flower in a glass."]},
 ("22-5", 11): {"opts": ["A child wins every race at Sports Day.", "Being kind mattered more than winning at Sports Day.", "Team Yellow is the best team.", "Ben was too slow to finish."]},
 ("31-1", 13): {"opts": ["A young woman gets lost in the mountains and is rescued.", "A shopkeeper trains a girl to remember prices.", "A shepherd’s daughter loses her flock in the snow.", "A determined postwoman serves her valley for many years and finds new ways to help."]},
 ("32-5", 5): {"items": ["Haru made her tenth sheet.", "Master Sato held the first sheet up to the light.", "Haru made her first sheet.", "Master Sato handed Haru a frame."]},
 ("32-5", 7): {"q": "How do you know Haru felt embarrassed after her first sheet? Give one piece of evidence."},
 ("32-5", 14): {"q": "What do you think Haru will do with her own first sheet in the future? Give a reason."},
}
TEXT_PATCHES = {
 "24-6": [("she announced", "he announced")],
 "30-1": [("love?” he asked", "love?” she asked")],
 "32-5": [("ruined,” he said", "ruined,” she said")],
}
