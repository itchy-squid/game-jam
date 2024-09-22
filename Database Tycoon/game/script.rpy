# Declare characters used by this game. The color argument colorizes the name of the character.

define act = Character(None, what_italic=True, what_color="#c0c0c0")
define think = Character(None, what_itelic=True, what_prefix="(", what_suffix=")")
define who = Character("???")
define r = Character("Kaitlyn")
define hb = Character("Heavy Bid")
define hj = Character("Heavy Job")

label splashscreen:
  scene splash

# The game starts here.
label start:
    scene black
    with Pause(1)
    show text """Disclaimer:{p}
The characters, locations, and events depicted in this game are entirely 
fictional. Any resemblance to actual persons, living or dead, or actual 
events is purely coincidental.{p}
The authors are solely responsible for the content of this game. HCSS and
its affiliates cannot be held responsible for any content or actions taken 
by the authors."""
    pause
    hide text

    scene bedroom with Pixellate(2.0,5)

    think "What time is it?"
    think "Oh right, today is my first day."
    think "I'm really nervous..."
    think "I guess I'd better get ready."

    scene entrance

    think "I can't believe I'm finally here!"
    think "It's my first day at Heavy Construction Systems Specialists High School."
    think "They call it HCSSHS for short."
    think "I don't know if I can keep all of those letters straight."
    think "I've worked so hard to get here."
    think "The interview process alone took a year."
    think "I'll just have to do my best!"
	
    scene receptionist_desk
    show receptionist at left

    who "Hi! Are you the new student? I don't think I've seen you before."
    "Hi, yes, today is my first day. I was told to check in and pick up my class schedule?"
    who "Absolutely! I should have your forms here, if you give me a minute. What are you specializing in?"
    "I'm studying database administration."
    who "Oh, that sounds difficult! What made you decide to study at HCSSHS?"
    "I've dreamed of coming here ever since I was little, when I first decided to become a database administrator. The program here is unmatched."
    "They don't just teach you how to manage one database here -- you're thrown into a sea of them." 
    "With hundreds running simultaneously, the school's infrastructure is a beast. You don't just learn theory here -- you're thrown right into the fire."
    "The systems are complex, constantly changing, and the only way to keep up is to be the best. Failure is not an option."
	"If I can make it here, I'm practically guaranteed to make it in the real world."
    act "The student raises an eyebrow, clearly impressed."
    who "Wow, sounds intense! I knew our program was tough, but I didn't realize it was {i}that{i} demanding. Well, I hope you're ready for the challenge!"
    act "She smiles and hands me a stack of papers to me."
    who "By the way, my name is Kaitlyn!" 
    r "By the way, my name is Kaitlyn!"
    r "I usually help out the student council. I'm in charge of greeting new students."
	act "She motions towards a hallway."
    r "Your first class is in the Development building, just behind the main building. Follow the path on the left, head out the side door, and you’ll see it straight ahead."
	
	scene walkway with pixelate
	
	act "As I make my way to my first class, something small flutters into view."
	act "A tiny, green bird, no bigger than my hand, swoops down from a nearby branch. It lands a few feet in front of me, its head tilted curiously, watching the ground intently." 
	show hurdybirb at right
    who "*chirp* *chirp*"
	act "Its colorful feathers catch the light as it hops around. I can't help but smile before catching my breath to step inside."
	
	scene cluster
	
	
	
	
    return
