# Gender-stereotype review, set 2 (levels 23-27). See qa/gender_review_s2.md.
PATCHES = {
 ("23-3", 8): {"items": ["The orchid was purple.", "The lettuces looked like paper streamers.", "The glasshouse felt cold.", "The tomatoes were hanging in red clusters."]},
 ("24-6", 5): {"items": ["The twins went to the park with Grandad.", "The twins’ eyes were covered with scarves.", "Aaliyah wrote “MYSTERY SOLVED”.", "Aaliyah found a paintbrush behind the sofa."]},
 ("24-6", 6): {"q": "Why do you think Grandad took the twins to the park that morning?"},
 ("24-6", 7): {"items": ["Mum made the shelves at home in the garage.", "The window in the loft was round.", "Dad sat down on a beanbag first.", "Grandad took the twins swimming."]},
 ("25-1", 1): {"opts": ["Grace", "Omar", "Ms Bell", "Priya"]},
 ("25-1", 5): {"items": ["Kai overtook a runner on the final bend.", "Ms Bell told Kai to trust his legs.", "A runner from Hillcrest ran past Omar.", "Kai took the silver medal."]},
 ("25-1", 10): {"items": ["Kai was the first runner in the relay.", "Kai’s team won the race.", "Elm Park were third when Kai took the baton.", "Ms Bell was pleased with the changeovers."]},
 ("25-1", 13): {"opts": ["A runner wins a gold medal without any help.", "A nervous runner overcomes his fear and helps his team to second place.", "A coach decides to change the order of the team.", "A runner from Hillcrest wins the race."]},
 ("26-2", 4): {"q": "The stranger said, “You look like someone who shares whatever they have.” Why did the stranger give the mill to Anders?"},
}
TEXT_PATCHES = {
 "23-3": [("frilled like ballgowns", "frilled like paper streamers")],
 "24-6": [("Grandma arrived early", "Grandad arrived early")],
 "25-1": [("said Mr Bell, the coach", "said Ms Bell, the coach"),
          ("a tall boy from Hillcrest", "a tall runner from Hillcrest"),
          ("only one boy stood between him and the finish line, and the boy was tiring", "only one runner stood between him and the finish line, and that runner was tiring"),
          ("Mr Bell hurried over", "Ms Bell hurried over"),
          ("was perfect,” he said", "was perfect,” she said")],
 "25-4": [("A man in a yellow jacket strolls along the quay, jangling a bunch of keys. He unlocks", "A ferry worker in a yellow jacket strolls along the quay, jangling a bunch of keys. She unlocks")],
 "26-2": [("a long grey beard", "long grey braids"),
          ("a man who shares whatever he has", "someone who shares whatever they have"),
          ("From beneath his cloak he drew", "From beneath her cloak she drew"),
          ("he explained", "she explained"),
          ("thank him", "thank her")],
 "26-3": [("cried her aunt", "cried her uncle")],
}
