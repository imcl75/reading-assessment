# Child-friendliness fixes (after the teacher's guidance: o'clock times, months and dates are fine; only bare 'at ten' style times are not)
PATCHES = {}
TEXT_PATCHES = {'28-3': [('at twelve;', 'at twelve o’clock;'), ('began at ten and might', 'began at ten o’clock and might')],
 '29-3': [('no shareholders or advertisements', 'no tills or advertisements')],
 '29-6': [('Every letter weighing up to half an ounce,', 'Every ordinary letter,')],
 '30-5': [('to mark a hundred years since the French Revolution', 'to show off amazing new inventions from around the world')]}
