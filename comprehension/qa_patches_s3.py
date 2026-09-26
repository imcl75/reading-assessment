# Gender review, set 3 (levels 28-31).
TEXT_PATCHES = {
 # Mum defaulted to the kitchen and the tea towel.
 "28-3": [("Then Mum came in from the kitchen, drying her hands on a tea towel.", "Then Dad came in from the kitchen, drying his hands on a tea towel.")],
 # Mum as the worrier; male bus driver; woman with a shopping trolley.
 "30-1": [
  ("The driver, a stocky man with a bristling moustache, drummed his fingers on the steering wheel and peered at her over his glasses.",
   "The driver, a stocky woman with cropped grey hair, drummed her fingers on the steering wheel and peered at her over her glasses."),
  ("a woman with a shopping trolley", "a woman with a guitar case"),
  ("Her mum had warned her that the journey would be long and lonely", "Her dad had warned her that the journey would be long and lonely"),
 ],
 # Mothers alone named as the pups' carers.
 "30-3": [("While the mothers are away foraging,", "While the parents are away foraging,")],
 # Girl's voice / boy's deep voice; neat-handwriting girl and struggling-reader boy.
 "30-4": [
  ("in what he believed was a convincing girl’s voice", "in what he believed was a convincing impression of Amira"),
  ("as deeply as she could manage", "as gruffly as she could manage"),
  ("He praised “Callum’s” beautiful handwriting, which was really Amira’s.", "He praised “Amira’s” beautiful handwriting, which was really Callum’s."),
 ],
 # Mother-as-seamstress with thread; father-as-shepherd.
 "31-1": [("Her father was a shepherd and her mother a seamstress, and it was said that Agnes learned to read from the labels on her mother’s reels of thread.",
           "Her mother was a shepherd and her father a tailor, and it was said that Agnes learned to read from the labels on her father’s reels of thread.")],
}
PATCHES = {
 ("28-3", 5): {"items": ["Marcus gave Grandad a present.", "Dad reminded Marcus about the birthday.", "Marcus told Mrs Okafor his decision.", "Marcus opened the letter from school."]},
 ("28-3", 6): {"q": "Why did Marcus’s stomach lurch when Dad spoke about Saturday?"},
 ("28-3", 10): {"opts": ["Cross that Marcus had missed the final", "Annoyed with Dad", "Deeply touched", "Bored of chess"]},
 ("30-1", 8): {"q": "The driver “peered at her over her glasses”. What might she be thinking?",
               "a": "She is surprised / curious to see a young girl alone so late at night."},
 ("30-4", 6): {"q": "Amira’s gruff voice “sounded like a frog with a head cold”. Why is this a funny description?"},
}
