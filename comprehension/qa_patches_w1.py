# British date wording for children: "the 31st of March 1889", not "31 March 1889". And no bare "at seven": say "seven o'clock".
TEXT_PATCHES = {
 "28-6": [("On the morning of 17 December 1903,", "On the morning of the 17th of December 1903,")],
 "29-6": [("On 1 May 1840,", "On the 1st of May 1840,"), ("from 6 May.", "from the 6th of May.")],
 "30-5": [("On 31 March 1889,", "On the 31st of March 1889,")],
 "33-1": [("at seven that morning", "at seven o’clock that morning")],
}
