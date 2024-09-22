# Declare characters used by this game. The color argument colorizes the name of the character.

define think = Character(None, what_italic=True, what_color="#c0c0c0")
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

    show receptionist at left

    who "Hi! Are you the new student? I don't think I've seen you before."
    "I am."
    who "What are you specializing in?"
    "I'm studying database administration."
    who "Oh, that sounds difficult!"
    who "I didn't even know that was an option at HCSSHS."
    who "By the way, my name is Kaitlyn! Nice to meet you."
    r "By the way, my name is Kaitlyn! Nice to meet you."

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
