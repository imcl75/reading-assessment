# KS1 phonics comprehension texts, grouped by Unlocking Letters and Sounds phase (see levels.py NAMES).
# Each: (title, text, [(type, question, model answer)]). 3 questions per text: who/what/where/when plus one "why" needing a simple inference.
# Questions are read aloud by an adult, so they are not checked for decodability.
B = {}

# ---- Phase 2
B[1] = [
("Sam and the Cat",
 "Sam is sad. A cat got on his lap. It sat and sat. Sam pats the cat. Sam is not sad.",
 [("who","Who got on Sam's lap?","A cat."),("what","What did Sam do to the cat?","He patted it."),("why","Why is Sam not sad now?","The cat is on his lap / he has a cat to pat.")]),
("The Bun",
 "Meg has a bun. A pup ran up to Meg. The pup got the bun and ran off. Meg is mad.",
 [("who","Who has a bun?","Meg."),("what","What did the pup do?","Got the bun and ran off."),("why","Why is Meg mad?","The pup took her bun.")]),
("The Bus",
 "Ben and Nan got on a bus. Ben had a nap. Nan did not nap. Nan pats Ben. Ben is up. Ben and Nan get off.",
 [("who","Who got on the bus with Ben?","Nan."),("who","Who had a nap?","Ben."),("why","Why did Nan pat Ben?","To get him up (so they could get off the bus).")]),
("The Hen",
 "Nan has a hen. The hen ran off. It ran in the mud. Nan ran and got it. Nan got it in a pen.",
 [("what","What did the hen run in?","The mud."),("where","Where did Nan put the hen?","In a pen."),("why","Why did Nan run?","To get the hen (it had run off).")]),
("Bob in Bed",
 "Bob is in bed. The sun is up. Dad is in. Dad pats Bob and Bob is up. Bob had a hug.",
 [("who","Who is in bed?","Bob."),("what","What did Bob have?","A hug."),("why","Why did Bob get up?","The sun was up (and Dad woke him).")]),
("Tim in the Sun",
 "Tim has a rug. Tim sat on it in the sun. Tim got hot. Tim ran to a hut. Tim is not hot.",
 [("where","Where did Tim sit?","On a rug in the sun."),("what","What did Tim run to?","A hut."),("why","Why did Tim run to the hut?","He was hot / to get out of the sun.")]),
]

# ---- Phase 3 (Weeks 1–3)
B[2] = [
("Chip the Dog",
 "Josh has a dog. It is Chip. Chip ran in the mud and got wet. Josh got Chip in the bath. Chip sat in the bath. Josh got wet as well.",
 [("what","What did Chip run in?","The mud."),("where","Where did Josh put Chip?","In the bath."),("why","Why did Josh put Chip in the bath?","He was wet and muddy.")]),
("The Chips",
 "Zed and Jen had chips. A gull sat on the shed. It got the chips. Zed is sad. Jen is sad.",
 [("what","What did Zed and Jen have?","Chips."),("where","Where did the gull sit?","On the shed."),("why","Why are Zed and Jen sad?","The gull got the chips.")]),
("The Jog",
 "Quin and Mum jog on the path. The sun is hot. Quin has no hat. Mum has a big hat and a cap. Mum got the cap on Quin.",
 [("who","Who has no hat?","Quin."),("where","Where do Quin and Mum jog?","On the path."),("why","Why did Mum get the cap on Quin?","The sun is hot / Quin had no hat.")]),
("Vin in Bed",
 "Vin is in bed. He is hot and red. Dad got a wet rag. Vin is not as hot. Vin is not sad.",
 [("who","Who is in bed?","Vin."),("what","What did Dad get for Vin?","A wet rag."),("why","Why is Vin in bed?","He is ill (hot and red).")]),
("Zeb the Cat",
 "Zeb is a cat. Zeb hid in the bin and had a nap. Jen shut the lid. Zeb is in the bin! Zeb is sad.",
 [("where","Where did Zeb have a nap?","In the bin."),("what","What did Jen shut?","The lid."),("why","Why is Zeb sad?","He is shut in the bin.")]),
("Jam on the Chin",
 "Beth and Ben had buns with jam. Beth got jam on the chin. Ben had a rag. He got it off.",
 [("what","What did Beth get on the chin?","Jam."),("who","Who had a rag?","Ben."),("why","Why did Ben use the rag?","To get the jam off Beth's chin.")]),
]

# ---- Phase 3 (Weeks 4–6)
B[3] = [
("The Moon",
 "Jess and Dad sat in the car. It was night and the moon was high. Jess had a nap. Dad had to keep on going.",
 [("who","Who sat in the car with Dad?","Jess."),("when","When was it?","At night."),("why","Why did Jess have a nap?","It was night.")]),
("Rain",
 "It was raining. Ben had a big coat on. Sam had no coat and got wet. Ben let Sam get in the coat with him. Then Sam was not wet.",
 [("who","Who had no coat?","Sam."),("what","What was the weather like?","It was raining."),("why","Why did Ben let Sam get in his coat?","Sam was wet / he had no coat.")]),
("The Goat",
 "Mark has a goat and a hen. The goat got in the barn and had the food for the hen. The hen is sad. Mark got the goat off. Then the hen had the food.",
 [("what","What did the goat have?","The hen's food."),("where","Where did the goat go?","In the barn."),("why","Why is the hen sad?","The goat had her food.")]),
("The Torch",
 "It was dark. Tim had a torch but it had no light. Tim sat on a log. Mum ran to Tim with a big torch. Mum had a hug for Tim.",
 [("what","What did Tim have?","A torch."),("where","Where did Tim sit?","On a log."),("why","Why did Mum run to Tim with a big torch?","It was dark and Tim's torch had no light.")]),
("The Book",
 "Joan and Dad sat in the boat. Joan had a book. Rain fell on the boat. The book got wet. Joan is sad.",
 [("who","Who sat in the boat with Joan?","Dad."),("what","What did Joan have?","A book."),("why","Why is Joan sad?","Her book got wet.")]),
("The Thorn",
 "Ben sat on the mat. He had a thorn in his foot. It was sharp and Ben was sad. Mum got the thorn off.",
 [("where","Where was the thorn?","In Ben's foot."),("who","Who got the thorn off?","Mum."),("why","Why was Ben sad?","The thorn was sharp / it hurt.")]),
]

# ---- Phase 3 (Weeks 7–8)
B[4] = [
("The Cow",
 "Mum and Ted are in the car. A cow got on the road. It sat down. Mum had to wait for the cow to get off the road.",
 [("what","What got on the road?","A cow."),("who","Who had to wait?","Mum."),("why","Why did Mum have to wait?","The cow was in the road.")]),
("The Chair",
 "Kim sat on a chair in the park. It had jam on it! Kim got up and the jam was on her top and in her hair. Kim was sad.",
 [("where","Where did Kim sit?","On a chair in the park."),("what","What was on the chair?","Jam."),("why","Why was Kim sad?","She had jam on her top and in her hair.")]),
("The Coin",
 "Beth had a coin. It fell in the soil near a rock. Beth dug and dug. Now Beth has the coin. Beth is not sad.",
 [("what","What did Beth have?","A coin."),("where","Where did it fall?","In the soil near a rock."),("why","Why did Beth dig?","To get / find the coin.")]),
("The Chick",
 "The farmer had a hen and a chick. The chick ran off. The hen was sad. The farmer had to look for the chick. It was in the barn. The farmer got the chick back.",
 [("who","Who had a hen and a chick?","The farmer."),("where","Where was the chick?","In the barn."),("why","Why was the hen sad?","Her chick ran off.")]),
("The Haircut",
 "Dad had a haircut. He sat in a chair. The barber cut and cut. Now Dad has no hair on top!",
 [("what","What did Dad have?","A haircut."),("where","Where did Dad sit?","In a chair."),("why","Why has Dad no hair on top?","The barber cut it all off.")]),
("The Shower",
 "Josh is in the shower. He got soap in his hair. The soap fell on the mat. The mat is wet now. Dad got a mop.",
 [("where","Where was Josh?","In the shower."),("what","What fell on the mat?","The soap."),("why","Why did Dad get a mop?","The mat was wet.")]),
]

# ---- Phase 4
B[5] = [
("The Frog",
 "A frog sat on a log next to a pond. The sun was hot. The frog jumped in with a splash. Now it is cool.",
 [("what","What sat on the log?","A frog."),("where","Where did the frog jump?","In the pond."),("why","Why did the frog jump in the pond?","It was hot.")]),
("The Shop",
 "Fran went to the shop to get milk. The shop was shut. A man said, \"Back soon.\" Fran sat on a step and waited.",
 [("what","What did Fran go to get?","Milk."),("where","Where did Fran sit?","On a step."),("why","Why did Fran wait?","The shop was shut.")]),
("The Bus",
 "Josh and Nan went on a bus. The bus had men and kids on it. Nan sat down. Josh had to stand. A man got up and let Josh sit. Josh said thanks.",
 [("who","Who was on the bus with Josh and Nan?","Men and kids."),("who","Who let Josh sit?","A man."),("why","Why did the man get up?","Josh had to stand / had no seat.")]),
("The Crab",
 "Pam and Jim went to a rock pool. They had a look at a crab. Jim bent down to pick it up. The crab pinched his hand! Jim yelped and jumped back.",
 [("where","Where did Pam and Jim go?","A rock pool."),("what","What did they look at?","A crab."),("why","Why did Jim yelp?","The crab pinched his hand.")]),
("The Flag",
 "Stan and Jess got a flag at the shop. They ran up the hill and stuck it in a crack in a rock. A strong wind hit the flag and it fell down.",
 [("what","What did Stan and Jess get at the shop?","A flag."),("where","Where did they stick the flag?","In a crack in a rock on the hill."),("why","Why did the flag fall down?","A strong wind blew.")]),
("The Net",
 "Fred and Beth went to the pond with a net. Beth got a frog and a crab in the net. Fred said they must not keep them. They let the frog and the crab go in the pond.",
 [("what","What did Beth get in the net?","A frog and a crab."),("where","Where did they let the frog and the crab go?","In the pond."),("why","Why did Fred say they must not keep them?","The animals belong in the pond / they should be free.")]),
]

# ---- Phase 4 Mastery
B[6] = [
("The Dentist",
 "Sam had a bad tooth. He went to the dentist. She had a look, then she handed Sam a red toothbrush. Now Sam will brush his teeth with the toothbrush a lot.",
 [("who","Who did Sam go to see?","The dentist."),("what","What did the dentist give Sam?","A red toothbrush."),("why","Why did Sam go to the dentist?","He had a bad tooth.")]),
("The Elf",
 "An elf lost his hat. He looked in the shed, in the dustbin and under his blanket. The elf was sad. Then he felt a bump in his bag. The hat was in the bag!",
 [("what","What did the elf lose?","His hat."),("where","Where was the hat?","In his bag."),("why","Why was the elf sad?","He lost his hat.")]),
("The Picnic",
 "Ben and his sister had a picnic in the garden. Ben's basket had a blanket and six muffins in it. But an ant had got in the basket, and Ben didn't like it. His sister picked it out.",
 [("where","Where was the picnic?","In the garden."),("what","What did Ben's basket have in it?","A blanket and six muffins."),("why","Why didn't Ben like it?","An ant had got in the basket.")]),
("The Rocket",
 "Josh and Jess had a box at the picnic. It was a rocket! They painted it red and stuck a flag on top. It was not big, but Gran said it was the best rocket at the picnic. Josh and Jess sat on the blanket with big smiles.",
 [("what","What did Josh and Jess paint red?","The box (the rocket)."),("what","What did they stick on top?","A flag."),("why","Why did Josh and Jess have big smiles?","Gran said it was the best rocket.")]),
("The Hamster",
 "Nan's hamster got out. It was not in its box. Nan looked in the basket and in her jacket. Then she felt a bump in her pocket. It was the hamster!",
 [("who","Whose hamster got out?","Nan's."),("where","Where did Nan find the hamster?","In her pocket (in her jacket)."),("why","Why did Nan look in the basket and in her jacket?","She was looking for the hamster / it had got out.")]),
("The Market",
 "Dad took Josh to the market. Josh had the basket. Dad got a pumpkin and some mushrooms and dropped them in it. Soon the basket had lots in it, and Josh's arms started to hurt. “It's my turn to have it,” said Dad.",
 [("who","Who had the basket at first?","Josh."),("what","What did Dad get at the market?","A pumpkin and some mushrooms."),("why","Why did Dad say it was his turn to have the basket?","It had lots in it and Josh's arms hurt.")]),
]

# ---- Phase 5a (Weeks 1–4)
B[7] = [
("A Wet Day",
 "It was a wet day. Rain fell all day. Ray had to stay in. He played with his toy boat in the bath.",
 [("what","What was the weather like?","Wet / raining."),("where","Where did Ray play with his boat?","In the bath."),("why","Why did Ray stay in?","It was raining.")]),
("The Bird",
 "A bird sat on the ground. It had a hurt wing. A boy found it. He called Gran and they got a box for it. Soon the bird was well and flew away.",
 [("what","What was wrong with the bird?","It had a hurt wing."),("who","Who found the bird?","A boy."),("why","Why did the boy call Gran?","To help the bird (it was hurt).")]),
("The Lost Boy",
 "Roy was at the fair. He looked round but Dad was not there. Roy called out. A helper found him and took him to a tent. Dad was in the tent!",
 [("where","Where was Roy?","At the fair."),("who","Who found Roy?","A helper."),("why","Why did Roy call out?","He could not see Dad / he was lost.")]),
("The New Pup",
 "Mr Brown had a new pup. The pup chewed a rug. It chewed a chair. It chewed a hat. Mr Brown was cross. He got a toy for the pup to chew.",
 [("who","Who had a new pup?","Mr Brown."),("what","What did the pup chew?","A rug, a chair and a hat."),("why","Why did Mr Brown get the pup a toy?","So it would chew the toy, not his things.")]),
("The Dolphin",
 "Sue and Dad went on a boat. Sue saw a dolphin jump up. It landed with a splash and got Sue wet.",
 [("where","Where did Sue and Dad go?","On a boat."),("what","What did Sue see?","A dolphin."),("why","Why was Sue wet?","The dolphin splashed her.")]),
("The Blue Cat",
 "Sue drew a blue cat with a red hat. Mr Grey saw it. He said it was the best one. Sue was proud.",
 [("what","What did Sue draw?","A blue cat with a red hat."),("who","Who saw the picture?","Mr Grey."),("why","Why was Sue proud?","Mr Grey said it was the best.")]),
]

# ---- Phase 5a (Weeks 5–6)
B[8] = [
("The Cake",
 "Jake made a cake for Mum. He made a big mess. Jam was on the mat and jam was on the tile. Mum smiled when she came home.",
 [("who","Who made the cake?","Jake."),("what","What was on the mat?","Jam."),("why","Why did Mum smile?","Jake made a cake for her.")]),
("The Kite",
 "Mike went up the hill with his kite. The wind was strong. Mike ran and the kite went up. Then it got stuck in a tree. Mum came and got it down.",
 [("where","Where did Mike go?","Up the hill."),("who","Who got the kite down?","Mum."),("why","Why did Mike run?","To get the kite up in the air.")]),
("The Snake",
 "Zane and Jade went to the zoo. They looked for a snake. It hid in a hole. Then it came out! Zane ran but Jade stayed and was brave.",
 [("where","Where did Zane and Jade go?","The zoo."),("where","Where did the snake hide?","In a hole."),("why","Why did Zane run?","He was scared of the snake.")]),
("The Bike",
 "Pat rode her bike to the shop. She left it next to the gate. When she came back, the bike was on the ground. The wind had pushed it down. Pat picked it up and rode home.",
 [("what","What did Pat ride?","Her bike."),("where","Where did Pat leave her bike?","Next to the gate."),("why","Why was the bike on the ground?","The wind pushed it down.")]),
("The Lake",
 "It was a hot day in June. Luke and Kate ran to the lake. Kate jumped in. Luke stayed on the sand. He had left his swim kit at home.",
 [("when","When did Luke and Kate run to the lake?","A hot day in June."),("where","Where did Luke and Kate run?","To the lake."),("why","Why did Luke stay on the sand?","He had left his swim kit at home.")]),
("The Stone",
 "Rose found a smooth stone on the path. She liked it, so she took it home. She painted a smile on it. Now the stone smiles at Rose.",
 [("where","Where did Rose find the stone?","On the path."),("what","What did Rose paint on the stone?","A smile."),("why","Why did Rose take the stone home?","She liked it.")]),
]

# ---- Phase 5b
B[9] = [
("The Snow",
 "It was very cold and snow fell all day. Kim and her friends made a big snowman. Next day the sun came out and it got warm. The snowman melted.",
 [("what","What did Kim and her friends make?","A snowman."),("when","When did the snowman melt?","When the sun came out."),("why","Why did the snowman melt?","It got warm / the sun came out.")]),
("The Mouse",
 "Once, a mouse lived in a big house. The mouse was very hungry. It could smell some cake, so it crept up the stairs. The mouse found the cake on a plate and ate it.",
 [("where","Where did the mouse live?","In a big house."),("what","What did the mouse find?","Cake."),("why","Why did the mouse creep up the stairs?","It was hungry / it could smell cake.")]),
("The Rope",
 "Cindy went to the gym with her friends. She wanted to go up the rope. It was hard at first. Cindy kept trying and got to the top. Her friends were proud.",
 [("where","Where did Cindy go?","The gym."),("what","What did Cindy want to go up?","The rope."),("why","Why were her friends proud?","She kept trying and got to the top.")]),
("The Farm Trip",
 "On Monday, the children went by bus to a farm. They saw many animals. A goat tried to eat Ben's hat! Ben laughed because he thought it was silly.",
 [("when","When did the children go to the farm?","On Monday."),("what","What did the goat try to eat?","Ben's hat."),("why","Why did Ben laugh?","He thought it was silly / funny.")]),
("The Baby",
 "Ted had a new baby sister. The baby cried and cried. Ted tried to help. He sang a song. Soon the baby was fast asleep.",
 [("who","Who cried and cried?","The baby."),("what","What did Ted do?","He sang a song."),("why","Why did Ted sing?","To help the baby stop crying.")]),
("Mr Cole",
 "Mr Cole was old and kind. Each day he fed the birds in the park. One day he was ill and could not come. The birds were hungry. They waited and waited for Mr Cole.",
 [("who","Who fed the birds?","Mr Cole."),("where","Where did he feed the birds?","In the park."),("why","Why were the birds hungry?","Mr Cole was ill and did not come.")]),
]

# ---- Phase 5c
B[10] = [
("The Present",
 "Wes wrapped a book for his gran. He wrote a note on it and tied a knot in the string. Gran was so pleased.",
 [("who","Who did Wes wrap a book for?","His gran."),("what","What did Wes tie a knot in?","The string."),("why","Why was Gran pleased?","She got a book from Wes.")]),
("The Match",
 "Mitch had a football match. Dad came to watch. Mitch was in goal. A big kick sent the ball at him. Mitch jumped and caught it! Dad shouted with joy.",
 [("where","Where was Mitch in the match?","In goal."),("what","What did Mitch catch?","The ball."),("why","Why did Dad shout with joy?","Mitch caught the ball / saved a goal.")]),
("The Bridge",
 "Bridget stood on the bridge and looked down. The river was far below. Her knees did not shake. She held the rail and looked for a fish.",
 [("where","Where did Bridget stand?","On the bridge."),("what","What was far below?","The river."),("why","Why did Bridget hold the rail?","To stay safe.")]),
("The Pet Lamb",
 "Nick has a pet lamb. It follows him to the school gate. The lamb waits there till home time. Then the lamb follows Nick back to the farm.",
 [("what","What is Nick's pet?","A lamb."),("where","Where does the lamb wait?","At the school gate."),("why","Why does the lamb wait till home time?","Nick is at school / it wants to go home with him.")]),
("The Picture",
 "Kim painted a picture for Dad. She used red, blue and green. Dad hung it in the kitchen. Kim smiled when she saw it on the wall.",
 [("what","What did Kim paint?","A picture."),("where","Where did Dad hang it?","In the kitchen (on the wall)."),("why","Why did Kim smile?","Dad hung her picture up / she was proud.")]),
("The Gnat",
 "A gnat bit Mum on the wrist. It itched and itched. Mum scratched it. Dad got a cream to stop the itch. Soon Mum felt fine.",
 [("what","What bit Mum?","A gnat."),("where","Where did it bite her?","On the wrist."),("why","Why did Dad get the cream?","To stop the itch.")]),
]
