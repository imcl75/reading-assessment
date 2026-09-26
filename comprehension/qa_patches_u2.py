# Child-friendliness fixes (after the teacher's guidance: o'clock times, months and dates are fine; only bare 'at ten' style times are not)
PATCHES = {('27-4', 8): {'q': 'Why might cafés and guest houses lose customers if the turbines are built?'},
 ('27-5', 10): {'q': 'The writer says Fleming “is said to have murmured”, “That is strange.” What does the phrase “is said to have” tell '
                     'the reader?'}}
TEXT_PATCHES = {'25-1': [('you nailed it', 'you did it brilliantly'), ('by no more than a whisker', 'by only the tiniest bit')],
 '27-4': [('cafés and B&Bs', 'cafés and guest houses')],
 '27-5': [('That’s funny', 'That is strange')]}
