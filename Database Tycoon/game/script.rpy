#########################
# Function declarations #
#########################
init python: 
    import re

    def get_player_name(prompt):
        while True:
            name = renpy.input(prompt)
            name = name.strip()  # Limit to 20 characters
            if len(name) >= 20: 
                return ""
            if re.match("^[A-Za-z ]*$", name):
                return name
            else:
                return ""

# r: https://cdn.midjourney.com/733e59b0-5e01-42ae-bdc6-d6b509e385d6/0_0.png
# hb: 
#   neutral serious girl, hugging folders with papers, school uniform with green accents, long ash brown curly hair, bangs, isekai anime style, 3/4 body shot, white background https://s.mj.run/pmx1EzK5m6c
# hj: https://cdn.midjourney.com/d922501c-e707-45c2-80f6-d1643217c5b4/0_1.png
# 
# birb: https://cdn.midjourney.com/fa34cb9e-da8d-4e06-b6c7-e08adbbde87f/0_1.png
#
# platform: https://cdn.midjourney.com/cc5a4c41-2885-489d-8c13-ae9771a5386b/0_1.png
# 

# Declare characters used by this game. The color argument colorizes the name of the character.
define say = Character("[player_name]", what_color="#ffffff")
define act = Character(None, what_color="#c0c0c0", what_italic=True)#, what_prefix="(", what_suffix=")")
define think = Character("[player_name]", what_color="#c0c0c0", what_italic=True)

define r = Character("[r_name]", color="#FFFF00")
define hb = Character("[hb_name]", color="#009639")
define hj = Character("[hj_name]", color="#005eb8")
define birb = Character("[birb_name]", color="#009639")
define sf = Character("[sf_name]", color="")
define p = Character("[p_name]", color="#8A2BE2")

default player_name = ""

default birb_name = "???"
default hb_name = "???"
default hj_name = "???"
default sf_name = "???"
default p_name = "???"
default r_name = "???"

default investigated = False

image birb smoll = Image("hurdybirb.png", xalign = 0.9, yalign = 0.7)

label splashscreen:
    scene splash
    return

# The game starts here.
label start:
    jump legal
    
label legal:
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
    jump intro
    
label intro:
    scene bedroom #with Pixellate(2.0,5)
    pause

    think "What time is it?"
    think "Oh right, today is my first day. I'm really nervous..."
    think "I guess I'd better get ready."
    
    scene entrance #with pixellate

    think "I can't believe I'm finally here!"
    think "It's my first day at Heavy Construction Systems Specialists High School. They call it HCSSHS for short."
    think "I hope I can keep those letters straight."
    think "I've worked so hard to get here. The interview process alone took a year."
    think "I'll just have to do my best!"
    jump check_in
    
label check_in:
    scene receptionist_desk
    act "As I open the door to step inside, I'm greeted by a young woman behind a desk."
    show receptionist
    pause(0.5)

    r "Hi! I don't think I've seen you before. Can I help you?"
    say "Today is my first day. I was told to check in and pick up my class schedule?"
    r "Absolutely! I should have your forms here, if you give me a minute. What is your name?"

    $ player_name = get_player_name("What is your name?")

    # Provide a default name if the player doesn't enter one
    if player_name == "":
        r "Oh, hmm.... I'm not sure our system can handle that name." 
        r "We'll call you Michael."
        $ player_name = "Michael"
    else:
        r "It's good to meet you, [player_name]!"

    r "What are you specializing in?"
    say "I'm studying database administration."
    r "That sounds difficult. What made you decide to study at HCSSHS?"
    say "The program is unmatched. They don't just teach you how to manage one database -- you're thrown into a sea of them." 
    say "With hundreds running simultaneously, the school's infrastructure is a beast. If I can make it here, I'm practically guaranteed to make it in the real world."
    act "The young woman raises her eyebrows, clearly impressed."
    r "Wow, sounds intense! I knew our program was tough, but I didn't realize it was {i}that{/i} demanding. Well, I hope you're ready for the challenge!"
    act "She smiles and hands me a stack of papers."
    r "By the way,"
    $ r_name = "Kaitlyn"
    r "By the way, my name is [r_name]!"
    r "I help out the student council from time to time. I'm in charge of onboarding new students."
    act "She motions towards a hallway."
    r "Your first class is in the Development building, just behind the main building. Follow the path on the left and head out the side door. You’ll see it straight ahead."
    jump meet_birb
    
label meet_birb:
    scene walkway
    
    act "As I make my way to class, something small flutters into view."
    pause(0.5)
    show birb smoll
    pause(0.5)
    act "A tiny, green bird, no bigger than my hand, swoops down from a nearby branch. It lands a few feet in front of me, its head tilted, watching the ground intently." 
    birb "*chirp* *chirp*"
    act "In the distance, the school bell rings—a reminder that class is starting soon."
    
    think "What should I do?"
    menu:
        "Observe the bird":
            $ investigated = True
            act "Wondering at the little bird, I pause for a moment."
            act "Its colorful feathers catch the light as it hops around, completely unaware of the world rushing by."
            act "I can't help but smile before catching my breath to continue on my way."
            jump first_class

        "Hurry to class":
            act "As much as I'd like to stay, I shake off my moment of distraction."
            think "I can't afford to be late on my first day."
            jump first_class
    
label first_class:
    scene dev building
    show heavybid frustrated at left
    hb "AAAAAGGHHHHhhhh, it doesn't make sense!" with hpunch
    act "As I step inside the Dev building, I'm greeted by a raised voice from a passing student."
    hb "There's a five-cent discrepancy! I've recalculated this three times. Every. Single. Time."
    act "A small girl next to her fidgets nervously"
    show heavyjob concerned at right
    hj "Five cents? I mean... it's pretty small. C-Couldn't that be from an unplanned expense?"
    hb "Not when the numbers are this precise! Every penny should be accounted for."
    hj "Could it be... I don't know, like maybe something technical? The databases? We've been adding more recently, haven't we?"
    act "The girl in green pauses, narrowing her eyes"
    hb "The databases... sure, their footprint has been growing, but I'm looking at the entire financial structure here. Infrastructure costs, maintenance, power usage -- everything."
    hb "It all lines up. Everything except for those five cents."
    think "This conversation isn't really my business. I'd better get moving before I'm late for my first class."

    scene cluster
    pause(1)

    act "I step inside, scanning the room. The hum of computers and an overpowered AC fills the air."
    act "A few students are already seated. I grab a seat near the front, by a window, which affords me a view to the walkway and trees outside."
    
    act "A tall figure with a no-nonsense demeanor, walks to the front and taps a button, causing the electronic board to display a vast network of interconnected nodes."
    show professor
    p "Welcome to Database Administration."
    $ p_name = "Professor Diego"
    p "Welcome to Database Administration. My name is [p_name]."
    p "For some of you, this will be your first time managing live systems. For others, perhaps a continuation of previous experience. But let me make one thing absolutely clear from the beginning: our school runs on databases."
    act "He gestures toward the screen, where diagrams show hundreds of interconnected nodes."
    p "Each of these nodes represents a simulated environment—a meticulously designed system that supports learning."
    p "Our school is famous for its broad library of learning materials, thanks to these environments. Whether you’re studying business strategy, engineering, or environmental science, there’s a database powering those lessons."
    act "He pauses, his eyes scanning the class."
    p "However, there is a cost. The more databases we support, the greater the strain on our infrastructure. Scalability becomes a challenge, even here. Every query, every transaction, and every mismanaged piece of data adds up."
    think "So, this school isn’t just running a few databases—they’re running hundreds. Maybe even a thousand?"
    p "If you're careless, one mismanaged database might not seem like much, but multiply that by hundreds—thousands—and the consequences become clear. Even the smallest oversight can create cascading problems."
    p "That's why responsible use is critical. You need to learn not only how to manage these databases but also how to maintain them."
    p "Today, we'll be going through the basics. I want each of you to spin up your own environment. We'll work through the exercises together."
    p "When you are done, please make sure you clean up after yourself."
    act "The next few hours pass in a blur of lectures and note-taking. Before I know it, classes have ended."
    
    jump first_night
    
label first_night:
    scene bedroom
    think "My first day... It was overwhelming but exciting."
    act "As I lie in bed, my mind buzzing with new information and new faces, the weight of the day pulls at my eyelids. Slowly, the world fades, and I drift into sleep."
        
    scene black with fade
    pause(1)

    jump meet_birb_cont

    
label meet_birb_cont:
    scene walkway
    act "As I step out of the building, a familiar figure catches my eye, this time perching in a young tree."
    show birb smoll
    pause(1)
    
    if investigated:
        think "I can't quite put my finger on it, but something about the bird seems different."
        think "But then again, I've just had a very long day. I still need to go home and review my notes before I can relax."
        act "I hear laughter and startle slightly, not realizing someone else had been watching me."
        
    r "Cute, isn't he?"
    act "[r_name] steps out from behind me smiling at the tiny bird, who hops around merrily."

    show receptionist at left
    
    r "He's kind of like our little mascot. I come out here to watch Hurdy all the time."
    say "Hurdy?"
    r "Hurdy Birb. That's his name. Well, that's what everyone calls him anyway."
    $ birb_name = "Hurdy Birb"
    say "Oh, I didn't know the bird had a name."
    birb "*chirp* *chirp*"
    say "Hi, [birb_name]."
    r "He likes to hang around campus. I'm just glad the alligator isn't still around..."
    act "She trails off, briefly lost in her own memories." # , before her eyes snap back to me

    # TODO

    return