# Declare characters used by this game. The color argument colorizes the name of the character.

define act = Character(None, what_italic=True, what_color="#c0c0c0")
define describe = Character(None, what_itelic=True, what_prefix="(", what_suffix=")")
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
    act "A tiny green bird flutters by and lands on a nearby bench."
    
    show hurdybirb at right
    
    who "*chirp* *chirp*"
    

    show receptionist at left

    who "Hi! Are you the new student? I don't think I've seen you before."
    "I am."
    who "What are you specializing in?"
    "I'm studying database administration."
    who "Oh, that sounds difficult! What made you decide to study at HCSSHS?"
    "This school is famous among database administrators!"
    "They don't just teach you how to manage one database here -- you're thrown into a sea of them." 
    "With hundreds of databases running simultaneously, the school's infrastructure is a beast. You don't just learn theory here -- you're thrown right into the fire."
    "The systems are complex, constantly changing, and the only way to keep up is to be better than anyone else. Failure's not an option."
    act "The student raises an eyebrow, clearly impressed by what she's just heard."
    who "Wow, sounds intense! I knew our program was tough, but I didn't realize it was {i}that{i} demanding. Well, I hope you're ready for the challenge!"
    act "She smiles and extends a hand in greeting"
    who "By the way, my name is Kaitlyn!" 
    r "By the way, my name is Kaitlyn!"
    r "I usually help out the student council."
    act "We shake hands, then she motions towards a hallway."
    "It's nice to meet you!"
    r "I'm in charge of greeting new students. Let me take you to the Development building."


    scene receptionist_desk
    show receptionist at left

    r "Here, let me introduce you to some friends."
    r "This is Heavy Bid."

    show heavybid at right

    hb "Hi"

    hide heavybid
    show receptionist at left

    r "And this is Heavy Job."

    show heavyjob at right

    r "(Bid and Job are sisters.)"
    hj "Nice to meet you."

    show receptionist at left

    r "And this is HurdyBirb"    

    hide heavyjob
    show hurdybirb at right

    who "..."

    return
