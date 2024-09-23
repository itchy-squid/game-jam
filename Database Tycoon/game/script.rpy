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

# Declare characters used by this game. The color argument colorizes the name of the character.
define say = Character("[player_name]", what_color="#ffffff")
define act = Character(None, what_color="#c0c0c0", what_italic=True, what_prefix="(", what_suffix=")")
define think = Character(None, what_color="#c0c0c0", what_italic=True)
define r = Character("[r_name]", color="#FFFF00")
define hb = Character("[hb_name]", color="#009639")
define hj = Character("[hj_name]", color="#005eb8")
define birb = Character("[b_name]", color="#009639")

default player_name = ""
default r_name = "???"
default hb_name = "???"
default hj_name = "???"
default b_name = "???"

image birb smoll = Image("hurdybirb.png", xalign = 0.9, yalign = 0.7)

label splashscreen:
    scene splash
    return

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
    
    scene receptionist_desk
    act "As I open the door to step inside, I'm greeted by a young woman behind a desk."

    show receptionist

    r "Hi! I don't think I've seen you before. What's your name?"
    
    $ player_name = get_player_name("What is your name?")

    # Provide a default name if the player doesn't enter one
    if player_name == "":
        r "Oh, hmm.... That name is a bit difficult." 
        r "We'll call you Michael."
        $ player_name = "Michael"
    else:
        r "It's good to meet you [player_name]!"

    say "Today is my first day. I was told to check in and pick up my class schedule?"
    r "Absolutely! I should have your forms here, if you give me a minute. What are you specializing in?"
    say "I'm studying database administration."
    r "That sounds difficult. What made you decide to study at HCSSHS?"
    say "I've dreamed of coming here ever since I was little. The program is unmatched."
    say "They don't just teach you how to manage one database -- you're thrown into a sea of them." 
    say "With hundreds running simultaneously, the school's infrastructure is a beast. If I can make it here, I'm practically guaranteed to make it in the real world."
    act "The young woman raises her eyebrows, clearly impressed."
    r "Wow, sounds intense! I knew our program was tough, but I didn't realize it was {i}that{/i} demanding. Well, I hope you're ready for the challenge!"
    act "She smiles and hands me a stack of papers."
    r "By the way, my name is Kaitlyn!"
    $ r_name = "Kaitlyn"
    r "I usually help out the student council. I'm in charge of greeting new students."
    act "She motions towards a hallway."
    r "Your first class is in the Development building, just behind the main building. Follow the path on the left and head out the side door. You’ll see it straight ahead."
    
    scene walkway
    
    act "As I make my way to class, something small flutters into view."
    pause(0.5)
    show birb smoll
    pause(0.5)
    act "A tiny, green bird, no bigger than my hand, swoops down from a nearby branch. It lands a few feet in front of me, its head tilted curiously, watching the ground intently." 
    birb "*chirp* *chirp*"
    act "Its colorful feathers catch the light as it hops around."
    act "Wondering at the little bird, I pause for a moment. I can't help but smile before catching my breath to enter the building."

    scene dev building
    show heavybid frustrated at left
    hb "AAAAAGGHHHHhhhh, it doesn't make sense!" with hpunch
    act "As I step inside, I'm greeted by a raised voice from a passing student."
    hb "There's a five-cent discrepancy! I've recalculated this three times. Every. Single. Time."
    act "A small girl next to her fidgets nervously"
    show heavyjob concerned at right
    hj "Five cents? I mean... it's pretty small. Couldn't that be from an unplanned expense?"
    hb "Not when the numbers are this precise! Every penny should be accounted for."
    hj "Could it be... I don't know, like maybe something technical? The databases? We've been adding more recently, haven't we?"
    act "The girl in green pauses, narrowing her eyes"
    hb "The databases... sure, their footprint has been growing, but I'm looking at the entire financial structure here. Infrastructure costs, maintenance, power usage -- everything."
    hb "It all lines up. Everything except for those five cents."
    think "This conversation isn't really my business. I'd better get moving before I'm late for my first class."

    scene cluster
    pause(1)

    # act "I take an empty seat."
    return
