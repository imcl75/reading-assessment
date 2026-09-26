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
 "Meg has a bun. A pup sat at Meg. The pup got the bun and ran off. Meg is mad.",
 [("who","Who has a bun?","Meg."),("what","What did the pup do?","Got the bun and ran off."),("why","Why is Meg mad?","The pup took her bun.")]),
("The Van",
 "At ten, Ben and Dad got in a cab. Ben had a nap. Dad did not nap. Dad had to get the cab up a hill.",
 [("when","When did Ben and Dad get in the cab?","At ten."),("who","Who had a nap?","Ben."),("why","Why did Dad not nap?","He was driving the cab.")]),
("The Hen",
 "Nan has a hen. The hen ran off in the mud. Nan ran to get it. Nan got the hen in a pen.",
 [("what","What did the hen run off in?","The mud."),("where","Where did Nan put the hen?","In a pen."),("why","Why did Nan run?","To get the hen (it had run off).")]),
("Bob in Bed",
 "Bob is in bed. It is ten. Mum ran in. Mum got Bob up. Bob is not mad. Bob had a hug.",
 [("who","Who is in bed?","Bob."),("when","When did Mum get Bob up?","At ten."),("why","Why did Mum get Bob up?","It was ten / it was late / time to get up.")]),
("Tim in the Sun",
 "Tim has a rug. Tim sat on it in the sun. It got hot. Tim ran in a hut. Tim is not hot.",
 [("where","Where did Tim sit?","On a rug in the sun."),("what","What did Tim run in?","A hut."),("why","Why did Tim run in the hut?","It was hot / to get out of the sun.")]),
]

# ---- Phase 3 (Weeks 1–3)
B[2] = [
("Chip the Dog",
 "Chip is a dog. He ran in the mud and got wet. Josh got Chip in the bath. Chip sat in the bath. Josh is wet as well.",
 [("what","What did Chip run in?","The mud."),("where","Where did Josh put Chip?","In the bath."),("why","Why did Josh put Chip in the bath?","He was wet and muddy.")]),
("The Chips",
 "Zed and Jen had chips. A gull sat on the shed. It got the chips. Zed is sad. Jen is sad.",
 [("what","What did Zed and Jen have?","Chips."),("where","Where did the gull sit?","On the shed."),("why","Why are Zed and Jen sad?","The gull got the chips.")]),
("The Jog",
 "Quin and Mum jog on the path. Quin has no hat. The sun is hot. Mum has a big hat. Mum got it on Quin.",
 [("who","Who has no hat?","Quin."),("where","Where do Quin and Mum jog?","On the path."),("why","Why did Mum get the hat on Quin?","The sun is hot / Quin had no hat.")]),
("Vin in Bed",
 "Vin is in bed. He is hot and red. Mum got him a wet rag. It is on his chin. Vin is not sad.",
 [("who","Who is in bed?","Vin."),("what","What did Mum get for Vin?","A wet rag."),("why","Why is Vin in bed?","He is ill.")]),
("Zeb the Cat",
 "Zeb is a cat. Zeb sat in the bin and had a nap. Jen did not check the bin. She shut the lid. Then Zeb is sad.",
 [("where","Where did Zeb have a nap?","In the bin."),("what","What did Jen shut?","The lid."),("why","Why is Zeb sad?","He is shut in the bin.")]),
("Jam on the Chin",
 "Beth and Ben had buns with jam. Ben got jam on his chin. Beth had a rag. She got it off.",
 [("what","What did Ben have on his chin?","Jam."),("who","Who had a rag?","Beth."),("why","Why did Beth use the rag?","To get the jam off Ben's chin.")]),
]

# ---- Phase 3 (Weeks 4–6)
B[3] = [
("The Moon",
 "Jess and Dad sat in the car. It was night. The moon was high. Jess had a nap. Dad had to keep on going.",
 [("who","Who sat in the car with Dad?","Jess."),("when","When was it?","At night."),("why","Why did Jess have a nap?","It was night / she was tired.")]),
("Rain",
 "It was raining. Ben had a coat on. Sam had no coat. Sam got wet. Ben let Sam get in the coat with him. Then Sam was not wet.",
 [("who","Who had no coat?","Sam."),("what","What was the weather like?","It was raining."),("why","Why did Ben let Sam get in his coat?","Sam was wet / he had no coat.")]),
("The Goat",
 "Mark has a goat and a hen. The goat got in the barn and had the hen food. The hen is sad. Then Mark got the goat off and the hen had the food.",
 [("what","What did the goat have?","The hen's food."),("where","Where did the goat go?","In the barn."),("why","Why is the hen sad?","The goat had her food.")]),
("The Torch",
 "It was dark. Tim had a torch. It had no light. Tim sat on the road. Mum had a big light on the car. Mum got Tim in the car with a hug.",
 [("what","What did Tim have?","A torch."),("where","Where did Tim sit?","On the road."),("why","Why did Mum get Tim?","He was in the dark / needed help.")]),
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
 "Kim sat on a chair in the park. It had jam on it. Kim got up and her top had jam on it. Her hair had jam in it as well! Mum is mad.",
 [("where","Where did Kim sit?","On a chair in the park."),("what","What was on the chair?","Jam."),("why","Why is Mum mad?","Kim's top has jam on it.")]),
("The Coin",
 "Ben had a coin. It fell in the soil near a rock. Ben dug and dug. Now Ben has the coin. Ben is not sad.",
 [("what","What did Ben have?","A coin."),("where","Where did it fall?","In the soil near a rock."),("why","Why did Ben dig?","To get / find the coin.")]),
("The Chick",
 "The farmer has a hen and a chick. The chick ran off. The hen was sad. The farmer had to look for the chick. It was in the barn. The farmer got the chick back.",
 [("who","Who has a hen and a chick?","The farmer."),("where","Where was the chick?","In the barn."),("why","Why was the hen sad?","Her chick ran off.")]),
("The Haircut",
 "Dad had a haircut. He sat in a chair. The man cut and cut. Now Dad has no hair on top!",
 [("what","What did Dad have?","A haircut."),("where","Where did Dad sit?","In a chair."),("why","Why has Dad no hair on top?","The man cut it all off.")]),
("The Shower",
 "Josh is in the shower. He got soap in his hair. The soap fell on the mat. Mum got her mop. The mat is wet now.",
 [("where","Where is Josh?","In the shower."),("what","What fell on the mat?","The soap."),("why","Why did Mum get her mop?","The mat was wet.")]),
]

# ---- Phase 4
B[5] = [
("The Frog",
 "A frog sat on a log next to a pond. The sun was hot. The frog jumped in with a splash. Now it is cool.",
 [("what","What sat on the log?","A frog."),("where","Where did the frog jump?","In the pond."),("why","Why did the frog jump in the pond?","It was hot.")]),
("The Shop",
 "Fran went to the shop to get milk. The shop was shut. A man said the shop is shut till ten. Fran sat on a step and waited.",
 [("what","What did Fran go to get?","Milk."),("where","Where did Fran sit?","On a step."),("why","Why did Fran wait?","The shop was shut.")]),
("The Bus",
 "Josh and Nan got on a bus. The bus was packed. Nan got a spot to sit. A man got up and let Josh sit. Josh said thanks.",
 [("what","What was the bus like?","Packed."),("who","Who let Josh sit?","A man."),("why","Why did the man get up?","So Josh could sit (Josh had no seat).")]),
("The Crab",
 "Pam and Jim went to a rock pool. They spotted a crab. Pam bent down to pat it. The crab pinched her hand! Pam yelped and jumped back.",
 [("where","Where did Pam and Jim go?","A rock pool."),("what","What did they spot?","A crab."),("why","Why did Pam yelp?","The crab pinched her hand.")]),
("The Flag",
 "Stan and Jess got a flag at the shop. They ran up the hill with it and stuck it in a crack. A strong gust hit the flag and it fell down.",
 [("what","What did Stan and Jess get at the shop?","A flag."),("where","Where did they stick the flag?","In a crack on the hill."),("why","Why did the flag fall down?","A strong gust hit it.")]),
("The Net",
 "Fred and Bill went to the pond with a net. Fred got a frog and a crab in the net. Bill said they must not keep them. They let the frog and the crab go in the pond.",
 [("what","What did Fred get in the net?","A frog and a crab."),("where","Where did they let the frog and the crab go?","In the pond."),("why","Why did Bill say they must not keep them?","The animals belong in the pond / they should be free.")]),
]

# ---- Phase 4 Mastery
B[6] = [
("The Dentist",
 "Sam had a bad tooth. He went to the dentist. She checked it and got Sam a red toothbrush. Sam was upset, but he will brush his teeth from now on.",
 [("who","Who did Sam go to see?","The dentist."),("what","What did the dentist get Sam?","A red toothbrush."),("why","Why did Sam go to the dentist?","He had a bad tooth.")]),
("The Elf",
 "An elf lost his hat. He checked in the shed, in the dustbin and under his blanket. The elf was upset. Then he felt a bump in his bag. The hat was in the bag!",
 [("what","What did the elf lose?","His hat."),("where","Where was the hat?","In his bag."),("why","Why was the elf upset?","He lost his hat.")]),
("The Picnic",
 "Ben and his sister had a picnic in the garden. Ben's basket had a blanket and six muffins in it. But an ant had got in the basket, and his sister didn't like it.",
 [("where","Where was the picnic?","In the garden."),("what","What did Ben's basket have in it?","A blanket and six muffins."),("why","Why didn't Ben's sister like it?","An ant had got in the basket.")]),
("The Rocket",
 "Josh and Sam had a rocket for the contest. They painted it red and stuck a flag on top. It didn't win, but the man said it was the smartest rocket in the contest.",
 [("what","What did Josh and Sam have for the contest?","A rocket."),("what","What did they stick on top?","A flag."),("why","Why do you think Josh and Sam were still proud?","The man said it was the smartest rocket.")]),
("The Hamster",
 "Nan's hamster got out. It isn't in its box. Nan checked in the basket and in her jacket. Then she felt a bump in her pocket. It was the hamster!",
 [("who","Whose hamster got out?","Nan's."),("where","Where did Nan find the hamster?","In her pocket (in her jacket)."),("why","Why did Nan check in the basket and in her jacket?","She was looking for the hamster / it had got out.")]),
("The Market",
 "Mum took Josh to the market. Josh had the basket. Mum got a pumpkin and some mushrooms and dropped them in it. Soon the basket was packed, and Josh's arms started to hurt. “It's my turn to have it,” said Mum.",
 [("who","Who had the basket at first?","Josh."),("what","What did Mum get at the market?","A pumpkin and some mushrooms."),("why","Why did Mum say it was her turn to have the basket?","It was packed and Josh's arms hurt.")]),
]

# ---- Phase 5a (Weeks 1–4)
B[7] = [
("A Wet Day",
 "It was a wet day. Rain fell all day. Ray had to stay in. He played with his toy boat in the bath.",
 [("what","What was the weather like?","Wet / raining."),("where","Where did Ray play with his boat?","In the bath."),("why","Why did Ray stay in?","It was raining.")]),
("The Bird",
 "A bird sat on the ground. It had a hurt wing. A girl found it. She called Mum and they got a box. Soon the bird was well and flew away.",
 [("what","What was wrong with the bird?","It had a hurt wing."),("who","Who found the bird?","A girl."),("why","Why did the girl call Mum?","To help the bird (it was hurt).")]),
("The Lost Boy",
 "Roy was at the fair. He looked round but Mum was not there. Roy called out. A man found him and took him to a shop. Mum was at the shop!",
 [("where","Where was Roy?","At the fair."),("who","Who found Roy?","A man."),("why","Why did Roy call out?","He could not see Mum / he was lost.")]),
("The New Pup",
 "Mrs Brown had a new pup. The pup chewed a rug. It chewed a chair. It chewed a hat. Mrs Brown was cross. She got a toy for the pup to chew.",
 [("who","Who had a new pup?","Mrs Brown."),("what","What did the pup chew?","A rug, a chair and a hat."),("why","Why did Mrs Brown get the pup a toy?","So it would chew the toy, not her things.")]),
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
 "Mike went up the hill with his kite. The wind was strong. Mike ran and the kite went up. Then it got stuck in a tree. Dad came and got it down.",
 [("where","Where did Mike go?","Up the hill."),("who","Who got the kite down?","Dad."),("why","Why did Mike run?","To get the kite up in the air.")]),
("The Snake",
 "Zane and Jade went to the zoo. They looked for a snake. It hid in a hole. Then it came out! Zane ran but Jade stayed and was brave.",
 [("where","Where did Zane and Jade go?","The zoo."),("where","Where did the snake hide?","In a hole."),("why","Why did Zane run?","He was scared of the snake.")]),
("The Bike",
 "Pete rode his bike to the shop. He left it next to the gate. When he came back, the bike was on the ground. The wind had made it drop. Pete picked it up and rode home.",
 [("what","What did Pete ride?","His bike."),("where","Where did Pete leave his bike?","Next to the gate."),("why","Why was the bike on the ground?","The wind made it drop.")]),
("The Lake",
 "It was a hot day in June. Luke and Kate ran to the lake. Luke jumped in. Kate stayed on the bank. She had left her swim kit at home.",
 [("when","When was it?","A hot day in June."),("where","Where did Luke and Kate run?","To the lake."),("why","Why did Kate stay on the bank?","She had left her swim kit at home.")]),
("The Stone",
 "Rose found a smooth stone on the path. She liked it, so she took it home. She painted a smile on it. Now the stone smiles at Rose.",
 [("where","Where did Rose find the stone?","On the path."),("what","What did Rose paint on the stone?","A smile."),("why","Why did Rose take the stone home?","She liked it.")]),
]

# ---- Phase 5b
B[9] = [
("The Snow",
 "It was very cold and snow fell all day. Kim and her friends made a big snowman. Then the sun came out and it got hot. The snowman melted.",
 [("what","What did Kim and her friends make?","A snowman."),("when","When did the snowman melt?","When the sun came out."),("why","Why did the snowman melt?","It got hot / the sun came out.")]),
("The Mouse",
 "Once, a mouse lived in a big house. The mouse was very hungry. It could smell some cake, so it crept up the stairs. The mouse found the cake on a plate and ate it.",
 [("where","Where did the mouse live?","In a big house."),("what","What did the mouse find?","Cake."),("why","Why did the mouse creep up the stairs?","It was hungry / it could smell cake.")]),
("The Rope",
 "Cindy went to the gym in the city. She wanted to go up the rope. It was hard at first. Cindy kept trying and got to the top. Her friends were proud.",
 [("where","Where did Cindy go?","The gym."),("what","What did Cindy want to climb?","The rope."),("why","Why were her friends proud?","She kept trying and got to the top.")]),
("The Farm Trip",
 "On Monday, the children went by bus to a farm. They saw many animals. A goat tried to eat Ben's hat! Ben laughed because he thought it was silly.",
 [("when","When did the children go to the farm?","On Monday."),("what","What did the goat try to eat?","Ben's hat."),("why","Why did Ben laugh?","He thought it was silly / funny.")]),
("The Baby",
 "Mum had a new baby. The baby cried and cried. Ted tried to help. He sang a song. Soon the baby was fast asleep.",
 [("who","Who cried and cried?","The baby."),("what","What did Ted do?","He sang a song."),("why","Why did Ted sing?","To help the baby stop crying.")]),
("Mr Cole",
 "Mr Cole is old and kind. Each day, he feeds the birds in the park. One day, he was ill and could not come. The birds were hungry. They waited and waited for Mr Cole.",
 [("who","Who feeds the birds?","Mr Cole."),("where","Where does he feed the birds?","In the park."),("why","Why were the birds hungry?","Mr Cole was ill and did not come.")]),
]

# ---- Phase 5c
B[10] = [
("The Present",
 "Wes wrote a note for his gran. He wrapped it in paper and tied a knot in the string. Gran was so pleased with her present.",
 [("who","Who did Wes write a note for?","His gran."),("what","What did Wes tie a knot in?","The string."),("why","Why was Gran pleased?","She got a present from Wes.")]),
("The Match",
 "Mitch went to a football match with Dad. He was in goal. A big kick came at him. Mitch jumped and caught the ball! Dad shouted with joy.",
 [("where","Where was Mitch in the match?","In goal."),("what","What did Mitch catch?","The ball."),("why","Why did Dad shout with joy?","Mitch caught the ball / saved a goal.")]),
("The Bridge",
 "Bridget stood on the bridge and looked down. The river was far below. Her knees felt weak and she held the rail.",
 [("where","Where did Bridget stand?","On the bridge."),("what","What was far below?","The river."),("why","Why did Bridget hold the rail?","She felt scared / weak.")]),
("The Pet Lamb",
 "Nick has a pet lamb. It follows him to the school gate. The lamb waits there and butts his knee till home time. Then it follows Nick back to the farm.",
 [("what","What is Nick's pet?","A lamb."),("where","Where does the lamb wait?","At the school gate."),("why","Why does the lamb wait till home time?","Nick is at school / it wants to go home with him.")]),
("The Picture",
 "Kim painted a picture for Mum. She used red, blue and green. Mum hung it in the kitchen. Kim smiled when she saw it on the wall.",
 [("what","What did Kim paint?","A picture."),("where","Where did Mum hang it?","In the kitchen (on the wall)."),("why","Why did Kim smile?","Mum hung her picture up / she was proud.")]),
("The Gnat",
 "A gnat bit Dad on the wrist. It itched and itched. Dad scratched it. Mum got a cream to stop the itch. Soon Dad felt fine.",
 [("what","What bit Dad?","A gnat."),("where","Where did it bite him?","On the wrist."),("why","Why did Mum get the cream?","To stop the itch.")]),
]
