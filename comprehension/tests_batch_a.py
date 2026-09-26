from tests_src import T, Q2, TF

T(18, "18-2", "The New Climbing Frame", "Narrative", [
"On Monday morning, a big new climbing frame stood in the school playground. It was red and yellow, with a tall slide and a rope bridge. All the children stared at it. Amara had never seen anything so exciting.",
"At playtime, everyone ran to the climbing frame. Amara climbed up the ladder, but she stopped at the top. The rope bridge wobbled in the wind. Her legs felt shaky, and she looked down at the ground far below.",
"\u201cI can\u2019t do it,\u201d she whispered. She climbed back down and sat on a bench. She watched the other children cross the bridge, one by one. Her friend Tomasz waved from the top, but Amara pretended not to see him.",
"Soon Tomasz came and sat beside her. \u201cThe bridge is scary at first,\u201d he said. \u201cIt was scary for me, too. Shall we try it together? I will go first, and you can hold the rope.\u201d",
"Amara took a deep breath. Slowly, she climbed the ladder again. Step by step, she crept across the bridge, holding the rope tightly. It wobbled, but Tomasz was right in front of her, and he kept saying, \u201cNearly there!\u201d",
"At the end, Amara jumped onto the platform and laughed. \u201cI did it!\u201d she shouted. Then she whooshed down the slide with her arms in the air. When the bell rang, she did not want to go in. \u201cCan we do it again tomorrow?\u201d she asked.",
], [
 dict(d="2b",k="mc",m=1,q="What colours was the new climbing frame?",opts=["Blue and green","Red and yellow","Black and white","Orange and purple"],a="B"),
 dict(d="2a",k="find",m=1,q="Find and copy one word that tells you how Amara\u2019s legs felt at the top of the ladder.",a="shaky",g="Accept \u201cshaky\u201d only."),
 dict(d="2b",k="short",m=1,q="Who came and sat beside Amara on the bench?",a="Tomasz.",g="Accept Tomasz."),
 dict(d="2c",k="order",m=1,q="Number the events from 1 to 4 to show the order they happened in the story.",items=["Amara crossed the rope bridge.","Tomasz said he would go first.","Amara stopped at the top of the ladder.","Amara sat on the bench."],a=[4,3,1,2],g=Q2),
 dict(d="2d",k="short",m=1,q="Why do you think Amara pretended not to see Tomasz wave?",a="She felt scared or embarrassed because she could not cross the bridge.",g="Accept any answer about feeling scared, upset or embarrassed, or not wanting to be asked to cross the bridge."),
 dict(d="2a",k="mc",m=1,q="In the story, what does the word \u201ccrept\u201d mean?",opts=["Ran very fast","Jumped high","Fell over","Moved slowly and carefully"],a="D"),
 dict(d="2d",k="short",m=1,q="How can you tell that Tomasz is a kind friend? Give one piece of evidence.",a="He sat beside Amara / he said it was scary for him too / he went first / he kept saying \u201cNearly there!\u201d.",g="Accept any one relevant piece of evidence."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["The new climbing frame had a tall slide.","Amara crossed the bridge on her own.","Tomasz said the bridge was scary for him too."],a=["T","F","T"],g=TF),
 dict(d="2d",k="short",m=1,q="How did Amara feel at the end of the story? How can you tell?",a="Happy / proud / excited, because she laughed, shouted \u201cI did it!\u201d and wanted to do it again.",g="Accept a positive feeling with one piece of evidence (laughed, shouted, did not want to go in, wanted to do it again)."),
 dict(d="2e",k="short",m=1,q="What do you think Amara will do at playtime tomorrow?",a="Play on the climbing frame again / cross the bridge again.",g="Accept any sensible prediction linked to the climbing frame."),
])

T(18, "18-3", "Breakfast in Bed", "Narrative", [
"Kofi woke up early on Saturday. The house was quiet. His mum had been working late all week, and she was still fast asleep. \u201cLet\u2019s help her today,\u201d Kofi whispered to his little sister, Abena.",
"First, they tiptoed downstairs to the kitchen. Kofi took out the bread, and Abena found the butter. Kofi put two slices of bread in the toaster and waited. Pop! The toast jumped up, golden and warm.",
"Next, Abena picked a flower from the garden and put it in a small glass of water. \u201cMum loves yellow flowers,\u201d she said. Kofi filled the kettle, and he was very careful with the hot water. He made a cup of tea just the way Mum liked it, with a little milk and no sugar.",
"Then they put everything on a tray. Kofi carried it up the stairs very slowly. One step, two steps, three steps. The cup rattled, and a little tea spilled onto the tray. \u201cOh dear,\u201d said Kofi. Abena quickly wiped it up with a tissue.",
"They pushed open Mum\u2019s door. She opened one eye and then the other. When she saw the tray, she sat up and smiled. \u201cIs that breakfast in bed for me?\u201d she asked. \u201cYes!\u201d said the children.",
"Mum ate the toast and drank the tea. \u201cThis is the best breakfast ever,\u201d she said. \u201cI feel so lucky.\u201d Then she gave them both a big hug. Kofi felt warm inside.",
], [
 dict(d="2b",k="mc",m=1,q="Why was Mum still fast asleep?",opts=["She was ill.","She had lost her keys.","She had been working late all week.","She had been to a party."],a="C"),
 dict(d="2a",k="find",m=1,q="Find and copy one word that tells you what colour the toast was.",a="golden",g="Accept \u201cgolden\u201d only."),
 dict(d="2c",k="order",m=1,q="Number the events from 1 to 4 to show the order they happened in the story.",items=["Tea spilled on the tray.","Kofi made the toast.","Kofi made a cup of tea.","Abena put a flower in a glass."],a=[4,1,3,2],g=Q2),
 dict(d="2a",k="mc",m=1,q="In the story, what does the word \u201ctiptoed\u201d mean?",opts=["Walked very quietly","Ran quickly","Jumped up and down","Fell over"],a="A"),
 dict(d="2b",k="short",m=1,q="How did Mum like her tea?",a="With a little milk and no sugar.",g="Accept a little milk and no sugar. Both parts are needed."),
 dict(d="2d",k="short",m=1,q="Why did Kofi and Abena tiptoe downstairs?",a="So they would not wake Mum up.",g="Accept any answer about keeping quiet or not waking Mum."),
 dict(d="2d",k="short",m=1,q="Why do you think Kofi carried the tray up the stairs very slowly?",a="He did not want to spill the tea / drop the tray.",g="Accept any answer about being careful or not spilling."),
 dict(d="2d",k="short",m=1,q="How can you tell that Mum was pleased with her breakfast? Give one piece of evidence.",a="She smiled / she said it was the best breakfast ever / she gave them a hug.",g="Accept any one relevant piece of evidence."),
 dict(d="2g",k="short",m=1,q="The story says, \u201cKofi felt warm inside.\u201d How was Kofi feeling?",a="Happy / proud / pleased.",g="Accept any happy feeling. Do not accept \u201chot\u201d."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Abena picked a flower from the garden.","Kofi dropped the whole tray.","The children made cereal for breakfast."],a=["T","F","F"],g=TF),
])

T(18, "18-4", "How to Grow Cress", "Procedural", [
"Cress is a small plant that grows very quickly. You do not need a garden, because you can grow it on a window sill in about a week. It is fun to grow, and you can eat it in a sandwich. All you need is a few things from around the house.",
"You will need a small plastic tub, some cotton wool, a packet of cress seeds, and a jug of water.",
"Step 1. Put the cotton wool in the bottom of the tub. Make sure that it fills the tub and lies flat.",
"Step 2. Pour a little water onto the cotton wool until it is damp. It should not be dripping wet.",
"Step 3. Sprinkle the seeds over the top. Spread them out so that they are not all in one pile. Do not cover them up.",
"Step 4. Put the tub on a bright window sill, where the cress can get plenty of light. Add a little water each day to keep the cotton wool damp.",
"After two or three days, you will see tiny white roots and green shoots. After about a week, your cress will be as tall as your finger. Now it is ready to eat.",
"To pick your cress, ask an adult to help you cut the stems with scissors. Then rinse the cress under the tap. It is delicious on bread and butter, or in a salad. You can start again with fresh cotton wool and new seeds.",
], [
 dict(d="2b",k="mc",m=1,q="About how long does cress take to grow?",opts=["One day","A week","A month","A year"],a="B"),
 dict(d="2b",k="find",m=1,q="Find and copy the words that tell you how much water to pour onto the cotton wool in Step 2.",a="a little water",g="Accept \u201ca little water\u201d."),
 dict(d="2c",k="order",m=1,q="Number the steps from 1 to 4 to show the order to do them in.",items=["Spread the seeds on top.","Put the cotton wool in the tub.","Put the tub on a window sill.","Pour water onto the cotton wool."],a=[3,1,4,2],g=Q2),
 dict(d="2a",k="mc",m=1,q="In Step 2, what does the word \u201cdamp\u201d mean?",opts=["Very hot","Dripping wet","Slightly wet","Completely dry"],a="C"),
 dict(d="2b",k="short",m=1,q="What should you use to cut the cress stems?",a="Scissors (with an adult\u2019s help).",g="Accept scissors."),
 dict(d="2d",k="short",m=1,q="Why does the writer say, \u201cask an adult to help you\u201d cut the stems?",a="Scissors can be dangerous / so you do not hurt yourself.",g="Accept any answer about safety or scissors being sharp."),
 dict(d="2d",k="short",m=1,q="Ben puts his tub in a dark cupboard. Why is this not a good idea?",a="The cress needs plenty of light to grow.",g="Accept any answer that says cress needs light or a bright place."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Cress grows very slowly.","You need a packet of cress seeds.","You should cover the seeds with cotton wool."],a=["F","T","F"],g=TF),
 dict(d="2d",k="short",m=1,q="After two days, Mia can see tiny white roots. What does the text tell you will happen next?",a="Green shoots will appear / the cress will keep growing and be ready to eat after about a week.",g="Accept green shoots, or the cress getting taller, or being ready to eat in about a week."),
 dict(d="2c",k="mc",m=1,q="What is this text mainly about?",opts=["Why cress is good for you","How to grow cress at home","Which seeds grow biggest","How to make a sandwich"],a="B"),
])

T(18, "18-5", "All About Wind", "Information Report", [
"Wind is air that is moving. We cannot see it, but we can feel it on our faces, and we can see what it does. Wind makes the leaves on trees shake, and it makes flags flap.",
"Some winds are very gentle. A soft wind is called a breeze. A breeze feels cool on a hot day. It can blow the fluffy seeds of a dandelion away.",
"Other winds are much stronger. A strong wind can blow hats off heads, and it can make umbrellas turn inside out. A very strong wind is called a gale. In a gale, big branches can snap off trees, so it is best to stay indoors.",
"Wind is useful, too. Sailing boats have big sails that catch the wind and push the boat across the water. A windmill has long blades that spin round when the wind blows. Long ago, people used windmills to grind grain into flour. Nowadays, tall wind turbines turn in the wind to make electricity.",
"How can we tell how strong the wind is? Look at the trees. If only the leaves are moving, the wind is gentle. If the small branches are moving, the wind is stronger. If whole trees are swaying, the wind is very strong.",
"So the next time you go outside on a windy day, stop and look around. What can you see the wind doing?",
], [
 dict(d="2b",k="mc",m=1,q="What is wind?",opts=["Moving air","A kind of cloud","Falling rain","Warm sunshine"],a="A"),
 dict(d="2a",k="find",m=1,q="Find and copy the word for a soft, gentle wind.",a="breeze",g="Accept \u201cbreeze\u201d only."),
 dict(d="2a",k="mc",m=1,q="In paragraph 5, what does the word \u201cswaying\u201d mean?",opts=["Falling down","Standing still","Growing tall","Moving gently from side to side"],a="D"),
 dict(d="2b",k="short",m=1,q="What did people use windmills for long ago?",a="To grind grain into flour.",g="Accept: to make flour / to grind grain."),
 dict(d="2b",k="short",m=1,q="What do wind turbines make?",a="Electricity.",g="Accept electricity."),
 dict(d="2d",k="short",m=1,q="The writer says we cannot see wind. How do we know that wind is there?",a="We can feel it on our faces and we can see what it does (leaves shake, flags flap).",g="Accept feeling it or seeing what it moves."),
 dict(d="2d",k="short",m=1,q="Sam looks out of the window and sees whole trees swaying. What can he tell about the wind?",a="It is very strong.",g="Accept: very strong / a strong wind / a gale."),
 dict(d="2d",k="short",m=1,q="Priya\u2019s umbrella turned inside out. What kind of wind was it most likely to be?",a="A strong wind / a gale.",g="Accept strong wind or gale. Do not accept breeze."),
 dict(d="2c",k="tf",m=1,q="Tick True or False for each sentence.",items=["A breeze is a very strong wind.","Wind is air that is moving.","A windmill has long blades."],a=["F","T","T"],g=TF),
 dict(d="2g",k="short",m=1,q="The writer asks, \u201cHow can we tell how strong the wind is?\u201d Why do you think the writer asks a question here?",a="To make the reader think / to introduce the next part that answers it.",g="Accept any answer about getting the reader interested or leading into the answer."),
])

T(18, "18-6", "Rabbits as Pets", "Information Report", [
"Rabbits are soft, furry animals, and many families keep them as pets. A rabbit can live for eight years or more if it is looked after well.",
"A pet rabbit needs a safe home. A hutch is a wooden house for a rabbit. It needs a warm place to sleep, and it needs a run joined to it so that the rabbit can hop about. Rabbits need lots of space to run and jump every day.",
"A rabbit\u2019s most important food is hay or grass. A rabbit\u2019s teeth never stop growing, so chewing hay keeps them from getting too long. Rabbits also like fresh vegetables, such as cabbage and carrots, but they should only have a small amount. A rabbit must have fresh water every day.",
"Rabbits are friendly animals, and they do not like to be lonely. In the wild, they live in big family groups. A pet rabbit is happiest with another rabbit for company. If it has to live on its own, its owner should spend lots of time with it every day.",
"Some rabbits have long fur that needs to be brushed gently each day. Their hutch should be cleaned often, too, so that it stays fresh and dry. A tidy hutch keeps a rabbit happy.",
"Rabbits can make lovely pets. They need time and space, but they give a lot back to a family who look after them well.",
], [
 dict(d="2b",k="mc",m=1,q="How long can a pet rabbit live if it is looked after well?",opts=["Two years","Eight years or more","Fifty years","Only one year"],a="B"),
 dict(d="2b",k="find",m=1,q="Find and copy the two words that tell you what a rabbit must have every day to drink.",a="fresh water",g="Accept \u201cfresh water\u201d."),
 dict(d="2b",k="short",m=1,q="What is a hutch?",a="A wooden house for a rabbit.",g="Accept: a wooden home / house for a rabbit."),
 dict(d="2a",k="mc",m=1,q="In paragraph 4, what does the word \u201clonely\u201d mean?",opts=["Very hungry","Very sleepy","On your own without company","Full of energy"],a="C"),
 dict(d="2b",k="short",m=1,q="Why does a rabbit need to chew hay?",a="It keeps its teeth from getting too long.",g="Accept any answer about keeping its teeth short or from growing too long."),
 dict(d="2d",k="short",m=1,q="Why is it a good idea to keep two rabbits together?",a="Rabbits do not like to be lonely / they live in groups in the wild.",g="Accept either idea."),
 dict(d="2d",k="short",m=1,q="Aisha has one rabbit that lives on its own. What should Aisha do?",a="Spend lots of time with it every day.",g="Accept: spend lots of time with it / play with it or keep it company. Accept getting a second rabbit."),
 dict(d="2d",k="short",m=1,q="The writer says rabbits \u201cgive a lot back\u201d to a family. What do you think rabbits give back?",a="Friendship / fun / love / happiness.",g="Accept any sensible idea about enjoyment or company."),
 dict(d="2c",k="tf",m=1,q="Tick True or False for each sentence.",items=["Rabbits live in big family groups in the wild.","A rabbit\u2019s teeth stop growing.","Rabbits should eat lots of carrots."],a=["T","F","F"],g=TF),
 dict(d="2c",k="mc",m=1,q="Which sentence best sums up paragraph 3?",opts=["Rabbits should only eat carrots.","Rabbits need the right food and water to stay healthy.","Rabbits do not need to drink.","Rabbits have very small teeth."],a="B"),
])

T(19, "19-1", "A Day at the Farm Park", "Recount (Fictional)", [
"On Sunday, our family went to Hillside Farm Park. Dad packed sandwiches and drinks, and my little cousin Yusuf came with us. I sat in the back of the car and counted the sheep in the fields.",
"As soon as we arrived, we went to see the animals. In the big barn, a woman showed us how to feed the lambs with bottles of milk. The lambs pulled so hard on the bottles that Yusuf nearly fell over. Everyone laughed, and Yusuf laughed loudest of all.",
"After that, we walked to the pond to feed the ducks. There was a sign that said, \u201cPlease give the ducks only the special duck food.\u201d Dad bought a small bag, and we threw it in little handfuls. A very greedy white duck pushed to the front and ate most of it.",
"At lunchtime, we ate our sandwiches at a wooden picnic table. It was a windy day, and half of Mum\u2019s crisps blew away. A small brown hen strutted over to see if any had landed near her. She pecked at them, one by one.",
"In the afternoon, we went on a tractor ride around the farm. The trailer bumped over the grass, and we held on tight to the sides. The farmer pointed out the pigs, who were rolling in a muddy puddle. \u201cThey are keeping cool,\u201d he told us. Yusuf held his nose and giggled.",
"Before we left, we visited the gift shop. I chose a rubber pig for my desk, and Yusuf picked a woolly toy lamb. On the way home, we were all so tired that Dad turned the radio off. Yusuf fell asleep before we had even reached the main road, still holding his lamb.",
], [
 dict(d="2b",k="mc",m=1,q="Who came to the farm park with the writer\u2019s family?",opts=["A friend called Hillside","A cousin called Yusuf","A grandad","A neighbour"],a="B"),
 dict(d="2a",k="find",m=1,q="Find and copy one word from paragraph 3 that tells you the white duck wanted lots of food.",a="greedy",g="Accept \u201cgreedy\u201d only."),
 dict(d="2c",k="order",m=1,q="Number the events from 1 to 4 to show the order they happened in.",items=["They ate their sandwiches.","They went on a tractor ride.","They fed the lambs.","They fed the ducks."],a=[3,4,1,2],g=Q2),
 dict(d="2a",k="mc",m=1,q="In paragraph 5, what does \u201cpointed out\u201d mean?",opts=["Showed them where something was","Told them to be quiet","Took them away","Was cross with them"],a="A"),
 dict(d="2b",k="short",m=1,q="What did the sign at the pond say?",a="Please give the ducks only the special duck food.",g="Accept: only give the ducks the special (duck) food."),
 dict(d="2d",k="short",m=1,q="How can you tell that Yusuf enjoyed feeding the lambs?",a="He laughed loudest of all.",g="Accept: he laughed / everyone laughed."),
 dict(d="2d",k="short",m=1,q="Why do you think the hen came over to the picnic table?",a="She wanted to eat the crisps that had blown away.",g="Accept any answer about wanting the crisps or food."),
 dict(d="2d",k="short",m=1,q="Why do you think Dad turned the radio off on the way home?",a="Everyone was tired and Yusuf was asleep / so they could rest.",g="Accept any answer about tiredness, sleeping or quiet."),
 dict(d="2g",k="short",m=1,q="The writer says the lambs \u201cpulled so hard\u201d on the bottles. What does this tell you about the lambs?",a="They were very hungry / strong.",g="Accept hungry, eager, strong."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["The family travelled to the farm park by bus.","Yusuf chose a toy lamb in the gift shop.","The tractor ride happened before lunch."],a=["F","T","F"],g=TF),
])

T(19, "19-2", "The Missing Counter", "Narrative", [
"It was raining hard, so Ben and his sister Lola had to stay indoors. They had already read their comics and built a tower out of cushions. Now they were bored. \u201cLet\u2019s play Space Race,\u201d said Lola, pulling a dusty box from under the sofa.",
"They spread the board on the carpet. It showed a winding path of stars that led to a shiny silver rocket at the end. Lola chose the green counter, and Ben chose the blue one. Then they rolled the dice to see who would go first.",
"The game was close. First Lola was ahead, then Ben zoomed past her with a lucky six. Just as Ben was about to land on the last star, he reached for his counter. It was gone.",
"\u201cWhere is it?\u201d he cried. \u201cIt was right here!\u201d They searched under the sofa and behind the cushions. Lola lifted up the box and shook it. Nothing fell out. Ben was sure that Lola had hidden it as a trick, but she promised that she had not.",
"Just then, Biscuit, their little brown dog, wandered in from the kitchen. He was wagging his tail and looking very pleased with himself. Lola knelt down and peered into his basket. There, between a chewed bone and a soggy sock, sat the blue counter.",
"\u201cBiscuit!\u201d they groaned together. Lola wiped the counter on her jumper, and Ben put it back on the board. This time, Ben rolled a five and reached the silver rocket first. \u201cI win!\u201d he cheered. Lola shrugged. \u201cFine,\u201d she said, \u201cbut I\u2019m going to beat you in the next game.\u201d Biscuit yawned and went back to sleep.",
], [
 dict(d="2b",k="mc",m=1,q="Why did Ben and Lola have to stay indoors?",opts=["They were ill.","It was raining hard.","It was very late.","They had to tidy up."],a="B"),
 dict(d="2a",k="mc",m=1,q="In paragraph 3, what does the word \u201czoomed\u201d mean?",opts=["Moved very slowly","Stopped suddenly","Went very fast","Fell behind"],a="C"),
 dict(d="2b",k="short",m=1,q="Which counter did Lola choose?",a="The green one.",g="Accept green."),
 dict(d="2b",k="short",m=1,q="What was the aim of the game Space Race?",a="To reach the silver rocket at the end.",g="Accept: to get to the rocket / the end of the path of stars first."),
 dict(d="2c",k="order",m=1,q="Number the events from 1 to 4 to show the order they happened in.",items=["Lola found the counter in Biscuit\u2019s basket.","Ben rolled a lucky six.","Ben won the game.","Ben\u2019s counter went missing."],a=[3,1,4,2],g=Q2),
 dict(d="2d",k="short",m=1,q="How do you know that Biscuit had taken the counter? Give one piece of evidence.",a="The counter was in his basket / he looked very pleased with himself.",g="Accept either piece of evidence."),
 dict(d="2d",k="short",m=1,q="Lola says, \u201cFine.\u201d What does this tell you about how she felt when Ben won?",a="She was a little disappointed but she took it well / she wants to win next time.",g="Accept disappointed, or a good loser, or determined to win next time."),
 dict(d="2d",k="short",m=1,q="Biscuit was \u201clooking very pleased with himself\u201d. What does this suggest?",a="He knew he had done something cheeky / he was proud of taking the counter.",g="Accept any answer suggesting he seemed proud or knew what he had done."),
 dict(d="2e",k="short",m=1,q="What do you think Ben and Lola will do next?",a="Play another game.",g="Accept any sensible prediction, e.g. play again, Lola tries to win, they put the game away."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Ben chose the green counter.","The game was close.","Biscuit is a cat."],a=["F","T","F"],g=TF),
])

T(19, "19-3", "Show and Tell Friday", "Narrative", [
"On Friday morning, Kai walked into class holding a small cardboard box very carefully. It was Show and Tell day, and inside the box was something special. His friends crowded round, but Kai shook his head. \u201cYou will have to wait,\u201d he said with a grin.",
"After the register, Mrs Osei asked who wanted to go first. Kai\u2019s hand stayed by his side. His tummy felt as if it was full of butterflies. Instead, Chloe showed the class a blue feather that she had found in the park, and Hamza told a joke about a penguin, which made everybody groan and giggle.",
"Then it was Kai\u2019s turn. His legs felt wobbly as he walked to the front of the class. He stood the box on the table and took a deep breath. \u201cThis is my grandad\u2019s old compass,\u201d he began quietly.",
"He lifted out a round brass compass with a shiny glass top. A thin red needle trembled inside it. \u201cGrandad used it when he went walking in the hills,\u201d Kai explained. \u201cThe needle always points north, so he never got lost.\u201d He turned slowly on the spot, and everyone watched the needle swing round and settle again.",
"\u201cCan I have a go?\u201d asked Hamza. \u201cPlease may I try?\u201d said Chloe. Soon a line of children had formed beside the table. Mrs Osei let each child hold the compass for a moment and find north, and she reminded them all to be gentle.",
"By the end of the lesson, Kai\u2019s worries had melted away. \u201cThat was the best Show and Tell we have had all year,\u201d said Mrs Osei. Kai carefully put the compass back in its box. He could not wait to tell Grandad how much everybody had liked it.",
], [
 dict(d="2b",k="mc",m=1,q="What special day was it in Kai\u2019s class?",opts=["Sports Day","Show and Tell day","Book Week","Photo day"],a="B"),
 dict(d="2a",k="mc",m=1,q="In paragraph 4, what does the word \u201ctrembled\u201d mean?",opts=["Shook a little","Stopped completely","Shone brightly","Grew bigger"],a="A"),
 dict(d="2a",k="find",m=1,q="Find and copy one word from paragraph 3 that tells you how Kai\u2019s legs felt.",a="wobbly",g="Accept \u201cwobbly\u201d only."),
 dict(d="2b",k="short",m=1,q="What did Chloe show the class?",a="A blue feather.",g="Accept feather. Do not accept a compass or a joke."),
 dict(d="2c",k="order",m=1,q="Number the events from 1 to 4 to show the order they happened in.",items=["Kai showed the compass.","Hamza told a joke.","Children lined up for a go.","Kai walked in with a box."],a=[2,4,1,3],g=Q2),
 dict(d="2d",k="short",m=1,q="How can you tell that Kai felt nervous about going to the front? Give one piece of evidence.",a="His tummy felt full of butterflies / his legs felt wobbly / his hand stayed by his side / he spoke quietly.",g="Accept any one relevant piece of evidence."),
 dict(d="2d",k="short",m=1,q="Why do you think the other children wanted a go with the compass?",a="They thought it was interesting / special / they liked it.",g="Accept any answer about finding the compass interesting or exciting."),
 dict(d="2d",k="short",m=1,q="Why do you think Mrs Osei reminded the children to be gentle?",a="The compass was old and special / it might break.",g="Accept any answer about the compass being old, precious or easy to break."),
 dict(d="2g",k="short",m=1,q="The story says that Kai\u2019s worries had \u201cmelted away\u201d. What does this mean?",a="He stopped feeling nervous / worried.",g="Accept any answer saying his worries had gone."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Kai was the first to show something.","Hamza told a joke about a penguin.","The compass belonged to Kai\u2019s grandad."],a=["F","T","T"],g=TF),
])

T(19, "19-4", "Ladybirds", "Information Report", [
"Ladybirds are small, round beetles. Many of them are red or orange with black spots, but some are yellow, and some are black with red spots. A ladybird has six legs and two pairs of wings. The outer pair is hard and shiny, and it protects the thin inner wings that are used for flying.",
"The bright colours on a ladybird are a warning. Birds and other animals that might want to eat a ladybird see the colours and learn to stay away. Ladybirds also give out a nasty-tasting yellow liquid from their legs when they are in danger.",
"Gardeners are pleased to see ladybirds. They eat tiny insects called aphids that feed on plants and can damage flowers and vegetables. One ladybird can eat many aphids in a single day.",
"A ladybird begins life as a tiny yellow egg. The eggs are laid on leaves, close to a supply of aphids. After a few days, a larva hatches from each egg. The larva looks nothing like a ladybird. It is long and spiky, and it has no wings, but it eats a lot of aphids. When it is fully grown, it turns into a pupa, and inside the pupa its body changes. After about a week, an adult ladybird comes out.",
"In autumn, when the weather turns cold, ladybirds look for a safe place to spend the winter. Often, lots of them gather together under bark, in cracks in walls, or inside dry plant stems. They stay there, hardly moving, until the warm weather returns in spring.",
], [
 dict(d="2b",k="mc",m=1,q="How many legs does a ladybird have?",opts=["Four","Eight","Ten","Six"],a="D"),
 dict(d="2b",k="find",m=1,q="Find and copy the words that tell you what aphids are.",a="tiny insects",g="Accept \u201ctiny insects\u201d."),
 dict(d="2a",k="mc",m=1,q="In paragraph 5, what does the word \u201cgather\u201d mean?",opts=["Fly away","Come together in a group","Fall asleep","Look for food"],a="B"),
 dict(d="2c",k="order",m=1,q="Number the stages from 1 to 4 to show the life of a ladybird.",items=["Pupa","Adult ladybird","Egg","Larva"],a=[3,4,1,2],g=Q2),
 dict(d="2b",k="short",m=1,q="Where do ladybirds lay their eggs?",a="On leaves, close to aphids.",g="Accept: on leaves. Extra detail about aphids is not needed."),
 dict(d="2d",k="short",m=1,q="Why do you think ladybirds lay their eggs close to aphids?",a="So the larvae have food to eat as soon as they hatch.",g="Accept any answer about the young having food nearby."),
 dict(d="2d",k="short",m=1,q="Why are gardeners pleased to see ladybirds?",a="Ladybirds eat the aphids that damage plants.",g="Accept: they eat aphids / pests. Both the eating and the damage to plants are worth mentioning, but accept eating aphids alone."),
 dict(d="2d",k="short",m=1,q="Why might a bird decide not to eat a ladybird?",a="The bright colours warn it to stay away / ladybirds taste nasty.",g="Accept bright colours as a warning, or the nasty taste."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["All ladybirds are red.","A ladybird larva has no wings.","In winter, ladybirds hide in safe places."],a=["F","T","T"],g=TF),
 dict(d="2c",k="mc",m=1,q="Which is the best heading for paragraph 5?",opts=["How ladybirds catch food","Where ladybirds lay eggs","Why ladybirds have spots","How ladybirds spend the winter"],a="D"),
])

T(19, "19-5", "How to Make a Bird Feeder", "Procedural", [
"Do you like to watch birds in the garden? Wild birds often find it hard to get food in the cold months, so you can help them by making a bird feeder. It only takes about twenty minutes, and you can hang it outside for the birds to enjoy.",
"You will need: a large, dry pine cone; a piece of string about thirty centimetres long; some solid vegetable fat, called suet or lard; a bag of wild bird seed; a spoon; and a tray.",
"Step 1. Tie the string tightly around the top of the pine cone. Make a big loop at the end so that you can hang the feeder up later.",
"Step 2. Pour the bird seed onto the tray and spread it out. Ask an adult to soften the fat by leaving it in a warm room for an hour. It should be soft, but not runny.",
"Step 3. Use the spoon to push the fat between the scales of the pine cone. Be sure to fill every gap, and cover the outside of the cone as well.",
"Step 4. Roll the sticky pine cone in the bird seed until it is coated all over. Press the seeds on gently so that they stick.",
"Step 5. Hang your feeder from a branch outside, in a place where you can see it from a window. Then wait and watch. It may take a few days before the birds find it. Once they do, you will have lots of hungry visitors.",
"Remember to wash your hands well when you have finished.",
], [
 dict(d="2b",k="mc",m=1,q="About how long does it take to make the bird feeder?",opts=["Two hours","Twenty minutes","Two days","Twenty seconds"],a="B"),
 dict(d="2b",k="find",m=1,q="Find and copy the words that tell you what kind of pine cone you need.",a="a large, dry pine cone",g="Accept \u201clarge, dry pine cone\u201d (with or without \u201ca\u201d)."),
 dict(d="2a",k="mc",m=1,q="In Step 4, what does \u201ccoated all over\u201d mean?",opts=["Broken into pieces","Hidden away","Covered on every side","Tied up tightly"],a="C"),
 dict(d="2c",k="order",m=1,q="Number the steps from 1 to 4 to show the order to do them in.",items=["Roll the cone in bird seed.","Hang the feeder from a branch.","Push fat between the scales.","Tie string around the cone."],a=[3,4,2,1],g=Q2),
 dict(d="2b",k="short",m=1,q="What should you use to push the fat into the pine cone?",a="A spoon.",g="Accept spoon."),
 dict(d="2d",k="short",m=1,q="Why does the writer suggest hanging the feeder where you can see it from a window?",a="So you can watch the birds that come to it.",g="Accept any answer about watching or seeing the birds."),
 dict(d="2d",k="short",m=1,q="Sam hangs his feeder on Monday but sees no birds on Tuesday. What should he do?",a="Wait: it may take a few days for the birds to find it.",g="Accept be patient / wait / keep watching. Do not accept taking it down."),
 dict(d="2g",k="short",m=1,q="In Step 5, the writer says, \u201cyou will have lots of hungry visitors.\u201d Who are the \u201cvisitors\u201d?",a="The birds.",g="Accept birds / wild birds."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["The string is tied around the bottom of the pine cone.","The fat should be runny.","The bird seed is spread on a tray."],a=["F","F","T"],g=TF),
 dict(d="2d",k="short",m=1,q="The fat should be \u201csoft, but not runny\u201d. Why do you think it should not be runny?",a="It would drip off / it would not stay between the scales of the pine cone.",g="Accept any answer about it dripping, not staying in place or being messy."),
])

T(19, "19-6", "How Bread Is Made", "Explanation", [
"Every day, people around the world eat bread. A loaf of bread might seem simple, but making one takes several steps and a tiny helper called yeast. Yeast is a living thing so small that you cannot see one.",
"First, the baker mixes flour, water, salt and yeast in a large bowl. The ingredients stick together to make a soft, sticky lump called dough. Next, the baker kneads the dough. This means pressing, stretching and folding it again and again for about ten minutes. Kneading makes the dough smooth and stretchy.",
"Then the dough is left in a warm place to rest. While it rests, the yeast begins to feed on the sugars in the flour. As it feeds, it makes lots of tiny bubbles of gas. The bubbles get trapped inside the stretchy dough and push it upwards, so the dough slowly grows bigger and bigger. Bakers say that the dough is rising.",
"Next, the baker shapes the dough into a loaf and puts it on a tray. It is left for a little longer to rise again. Finally, the loaf goes into a very hot oven.",
"In the oven, the heat makes the bubbles grow even bigger, and the dough rises a little more. Then the heat turns the soft dough into a firm loaf. The outside of the loaf turns golden brown and crispy, and this is called the crust. The inside stays soft and full of small holes, where the bubbles used to be.",
"After about half an hour, the baker takes the loaf out of the oven. It is best to let it cool before you cut it. Then the bread is ready to eat.",
], [
 dict(d="2b",k="mc",m=1,q="What is yeast?",opts=["A kind of flour","A hot oven","A tiny living thing","A type of salt"],a="C"),
 dict(d="2a",k="find",m=1,q="Find and copy the word from paragraph 2 that means pressing, stretching and folding the dough.",a="kneads",g="Accept \u201ckneads\u201d only."),
 dict(d="2a",k="mc",m=1,q="In paragraph 3, what does the word \u201crising\u201d mean?",opts=["Growing bigger","Getting colder","Turning brown","Breaking apart"],a="A"),
 dict(d="2c",k="order",m=1,q="Number the steps from 1 to 4 to show how bread is made.",items=["The dough is baked in a hot oven.","The dough is left to rise.","The baker mixes the ingredients.","The baker kneads the dough."],a=[4,3,1,2],g=Q2),
 dict(d="2b",k="short",m=1,q="What do the tiny bubbles of gas do to the dough?",a="They push it upwards / make it grow bigger.",g="Accept: make it rise / grow bigger."),
 dict(d="2d",k="short",m=1,q="Why do you think the dough is left in a warm place to rest?",a="So the yeast works and the dough can rise.",g="Accept any answer about helping the yeast to work or the dough to rise."),
 dict(d="2d",k="short",m=1,q="What might happen to a loaf if the baker forgot to add yeast?",a="The dough would not rise / the bread would be flat and heavy.",g="Accept any answer saying there would be no bubbles, no rising or a flat loaf."),
 dict(d="2d",k="short",m=1,q="Why do you think the writer says it is best to let the loaf cool before you cut it?",a="It will be very hot / you could burn yourself.",g="Accept any answer about heat or safety."),
 dict(d="2c",k="mc",m=1,q="Which is the best heading for paragraph 5?",opts=["How to shape a loaf","What happens in the oven","Why yeast is small","How to eat bread"],a="B"),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Kneading takes about an hour.","Yeast makes bubbles of gas.","The crust is on the outside of the loaf."],a=["F","T","T"],g=TF),
])
