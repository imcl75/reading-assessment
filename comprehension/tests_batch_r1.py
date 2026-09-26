from tests_src import T, Q2, TF

T(19, "19-4", "Ladybirds", "Information Report", [
"Ladybirds are small, round beetles. Many are red with black spots. Some are yellow or orange. A few are black with red spots. A ladybird has six legs and two pairs of wings. The hard outer wings keep the thin inner wings safe. The inner wings are the ones it uses to fly.",
"The bright colours are a warning. Birds see the colours and learn to stay away. A ladybird can also give out a yellow liquid that tastes nasty when it is in danger.",
"Gardeners like ladybirds. They eat tiny insects called aphids. Aphids feed on plants and can harm flowers and vegetables. One ladybird can eat lots of aphids in a day. That helps the plants to grow well. This is why some gardeners buy ladybirds and set them free in the garden.",
"A ladybird starts life as a tiny yellow egg. The eggs are laid on leaves, near aphids. After a few days, a larva comes out of each egg. The larva looks nothing like a ladybird. It is long and spiky and has no wings. It eats lots of aphids and grows bigger and bigger. Then it turns into a pupa. Inside the pupa, its body changes. After about a week, an adult ladybird comes out.",
"In autumn, the weather gets cold. Ladybirds look for a safe place to spend the winter. Lots of them gather together under bark, in cracks in walls or inside dry plant stems. They stay there and hardly move. When spring comes and the weather is warm, they wake up and fly away.",
], [
 dict(d="2b",k="mc",m=1,q="How many legs does a ladybird have?",opts=["Four","Eight","Ten","Six"],a="D"),
 dict(d="2b",k="find",m=1,q="Find and copy the words that tell you what aphids are.",a="tiny insects",g="Accept “tiny insects”."),
 dict(d="2a",k="mc",m=1,q="In paragraph 5, what does the word “gather” mean?",opts=["Fly away","Come together in a group","Fall asleep","Look for food"],a="B"),
 dict(d="2c",k="order",m=1,q="Number the stages from 1 to 4 to show the life of a ladybird.",items=["Pupa","Adult ladybird","Egg","Larva"],a=[3,4,1,2],g=Q2),
 dict(d="2b",k="short",m=1,q="Where do ladybirds lay their eggs?",a="On leaves, near aphids.",g="Accept: on leaves. Extra detail about aphids is not needed."),
 dict(d="2d",k="short",m=1,q="Why do you think ladybirds lay their eggs near aphids?",a="So the larvae have food to eat as soon as they hatch.",g="Accept any answer about the young having food nearby."),
 dict(d="2d",k="short",m=1,q="Why are gardeners pleased to see ladybirds?",a="Ladybirds eat the aphids that harm plants.",g="Accept: they eat aphids / pests. Accept eating aphids alone."),
 dict(d="2d",k="short",m=1,q="Why might a bird decide not to eat a ladybird?",a="The bright colours warn it to stay away / ladybirds taste nasty.",g="Accept bright colours as a warning, or the nasty taste."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["All ladybirds are red.","A ladybird larva has no wings.","In winter, ladybirds hide in safe places."],a=["F","T","T"],g=TF),
 dict(d="2c",k="mc",m=1,q="Which is the best heading for paragraph 5?",opts=["How ladybirds catch food","Where ladybirds lay eggs","Why ladybirds have spots","How ladybirds spend the winter"],a="D"),
])

T(20, "20-2", "Owls at Night", "Information Report", [
"Owls are birds that hunt at night. During the day, most owls rest in trees, barns or old buildings. When the sun goes down, they wake up and look for food. Owls live in many parts of the world, and there are more than two hundred kinds.",
"An owl has very large eyes. They help it to see in the dark. The eyes cannot move around like ours, so an owl turns its whole head instead. It can turn its head a long way round to look behind it. Owls also have excellent hearing. Their ears are hidden under the feathers on the sides of their heads. An owl can hear a tiny mouse moving in the grass.",
"Owls have soft, fluffy feathers. The edges of their wings are soft too. This means an owl makes almost no sound when it flies. A mouse cannot hear it coming until it is too late.",
"Owls eat small animals such as mice, voles and beetles. They have sharp claws, called talons, for catching their food. Then they use a strong, curved beak to tear it up. Some owls swallow small animals whole. Later, the owl coughs up a small pellet of the parts it cannot digest, such as fur and tiny bones. Scientists collect these pellets to find out what an owl has been eating.",
"Most owls make their nests in holes in trees. Some use old nests that other birds have left behind. The mother owl lays her eggs, and she sits on them to keep them warm. After a few weeks, the chicks hatch. Both parents bring food to the nest until the young owls are big enough to fly.",
], [
 dict(d="2b",k="short",m=1,q="When do most owls hunt for food?",a="At night.",g="Accept: in the dark / after the sun goes down."),
 dict(d="2b",k="mc",m=1,q="How does an owl look behind it?",opts=["It moves its eyes","It flies backwards","It turns its whole head","It hops around"],a="C"),
 dict(d="2a",k="find",m=1,q="Find and copy the word in paragraph 4 that means the sharp claws of an owl.",a="talons",g="Accept “talons” only."),
 dict(d="2a",k="mc",m=1,q="In paragraph 2, what does the word “excellent” mean?",opts=["Very good","Rather quiet","Not good","Quite small"],a="A"),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Owls have soft feathers.","Owls only eat fish.","Owl chicks are fed by both parents."],a=["T","F","T"],g=TF),
 dict(d="2d",k="short",m=1,q="Why does an owl make almost no sound when it flies?",a="Its feathers and wing edges are soft.",g="Accept any answer about soft feathers or soft wings."),
 dict(d="2d",k="short",m=1,q="Why do you think a mouse cannot hear an owl coming?",a="The owl flies silently.",g="Accept any answer about the owl making no sound."),
 dict(d="2d",k="short",m=1,q="Why do scientists collect owl pellets?",a="To find out what the owl has been eating.",g="Accept any answer about finding out the owl’s food."),
 dict(d="2c",k="order",m=1,q="Number the parts of the text from 1 to 4 in the order they appear.",items=["How owls make nests","What owls eat","How owls fly quietly","Owls’ eyes and ears"],a=[4,3,2,1],g=Q2),
 dict(d="2c",k="mc",m=1,q="Which is the best heading for paragraph 4?",opts=["How owls look","What owls eat","Where owls sleep","How owls fly"],a="B"),
 dict(d="2d",k="short",m=1,q="Why might an owl use an old nest that another bird has left?",a="It saves the owl building a new nest.",g="Accept any sensible answer, such as: it is easier, quicker or already made."),
])

T(20, "20-6", "Diwali, the Festival of Lights", "Information Report", [
"Diwali is a festival. Millions of people all over the world celebrate it. It is often called the Festival of Lights. Hindu, Sikh and Jain people all celebrate Diwali, but they may do so for different reasons. It happens in autumn, in October or November.",
"Diwali lasts for five days. The main night is the third day. On that night there is no moon, so the sky is very dark. This makes the lights shine even more brightly.",
"Lamps are a big part of Diwali. Families light little clay lamps called diyas. They put them on windowsills, on doorsteps and along garden walls. Some people hang up strings of coloured lights too. The whole street can glow. Lighting the lamps is a way of welcoming happiness into the home.",
"Before the festival, people clean their homes from top to bottom. They also make patterns called rangoli on the floor by the front door. A rangoli can be made from coloured powder, rice or flower petals. The bright shapes are there to welcome visitors.",
"Food is important at Diwali too. Families cook special meals and make sweets to share. Laddoos are little round sweets. Barfi is cut into small squares. People give boxes of sweets to friends and neighbours. Sharing food with others is a very happy part of the festival.",
"Many people wear their best or new clothes for Diwali. Families visit each other, send cards and give gifts. Children often enjoy this part of the festival very much. In some places, there are fireworks at night that fill the sky with colour.",
"Diwali is a time for family and friends to come together. Lighting a lamp, making a rangoli or sharing a sweet are all ways to spread joy and kindness.",
], [
 dict(d="2b",k="short",m=1,q="How many days does Diwali last?",a="Five days.",g="Accept 5."),
 dict(d="2b",k="mc",m=1,q="In which season does Diwali happen?",opts=["Spring","Summer","Winter","Autumn"],a="D"),
 dict(d="2a",k="find",m=1,q="Find and copy the name of the small clay lamps used at Diwali.",a="diyas",g="Accept “diyas” (or “diya”)."),
 dict(d="2b",k="tf",m=1,q="Tick True or False for each sentence.",items=["Rangoli patterns are made near the front door.","Laddoos are cut into small squares.","Only Hindu people celebrate Diwali."],a=["T","F","F"],g=TF),
 dict(d="2d",k="short",m=1,q="Why do the lights shine “even more brightly” on the main night?",a="Because the sky is very dark (no moon).",g="Accept any answer about the dark sky or no moon."),
 dict(d="2a",k="mc",m=1,q="In paragraph 4, what does the word “patterns” mean?",opts=["Meals","Designs made of shapes and colours","Clothes","Gifts"],a="B"),
 dict(d="2c",k="mc",m=1,q="Which of these is the best heading for paragraph 5?",opts=["Lamps and lights","Cleaning the home","Food and sweets","Fireworks"],a="C"),
 dict(d="2d",k="short",m=1,q="Why do you think people clean their homes before Diwali?",a="To get the house ready for visitors / to welcome happiness.",g="Accept any sensible reason about getting ready, visitors or a fresh start."),
 dict(d="2d",k="short",m=1,q="How can you tell that sharing is an important part of Diwali? Give one example from the text.",a="People give boxes of sweets to friends and neighbours / cook meals to share / give gifts.",g="Accept any one example."),
 dict(d="2c",k="order",m=1,q="Number the parts of the text from 1 to 4 in the order they appear.",items=["Sweets and special meals","Lamps called diyas","How long the festival lasts","Rangoli patterns"],a=[4,2,1,3],g=Q2),
 dict(d="2g",k="short",m=1,q="The writer says Diwali is about “joy and kindness”. Which word tells us that the festival is happy?",a="joy",g="Accept “joy”."),
])
