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

define r = Character("[receptionist_name]", color="#FFFF00")
define hb = Character("[heavybid_name]", color="#009639")
define hj = Character("[heavyjob_name]", color="#005eb8")
define birb = Character("[birb_name]", color="#009639")
define sf = Character("[safety_name]", color="")
define prof = Character("[professor_name]", color="#8A2BE2")
define p = Character("[platform_name]")

default player_name = ""

default birb_name = "???"
default heavybid_name = "???"
default heavyjob_name = "???"
default safety_name = "???"
default professor_name = "???"
default platform_name = "???"
default receptionist_name = "???"

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
    show text """
This game contains themes and elements that may be 
unsettling to some readers. It is not suitable for young 
children or individuals who are easily disturbed. Player 
discretion is advised."""
    pause(4)
    show text """
The characters, locations, and events depicted in this game are entirely 
fictional. Any resemblance to actual persons, living or dead, or actual 
events is purely coincidental.{p}
The authors are solely responsible for the content of this game. HCSS and
its affiliates cannot be held responsible for any content or actions taken 
by the authors."""
    pause(3)
    show lawyer at right
    pause(3)
    hide text
    jump intro
    
label intro:
    scene bedroom #with Pixellate(2.0,5)
    pause (2)
    show text "(click to continue)"
    pause
    hide text

    act "The morning light spills into my room, casting a warm glow over everything."
    think "What time is it?"
    act "Sitting up in bed, I glance around my room, taking in the chaos of my preparations. Textbooks are piled high, my laptop is open with a to-do list, and my backpack sits ready by the door."    
    think "Oh right, Today is finally the day! My first day. I'm really nervous..."
    act "I can hardly believe I made it in. A prestigious school, known for its intense programs and top-notch facilities, is finally mine to explore."
    think "I guess I'd better get ready."
    
    scene entrance with fade

    act "As I approach to the school, the world feels different. The excitement of a new beginning fills the air, mingled with the scent of fresh grass and morning dew."
    act "It's my first day at HCSSHS—Heavy Construction Systems Specialists High School—an institution known for its rigorous programs and impressive resources."    
    think "I just hope I can keep that acronym straight."
    think "I've worked so hard to get here. The interview process alone took a year."    
    act "Pausing just outside the entrance, I take a deep breath, gathering my thoughts. What if I don’t fit in? What if the work is too hard?"
    act "But then I remember why I’m here. I’ve worked so hard to get to this point, and I can’t let fear hold me back. This is my chance to prove myself, to learn from the best, and to make new friends."
    act "The sounds of laughter, chatter, and footsteps fill the air, and I can’t help but smile. This is it—my new adventure begins now."

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
    say "The program is unmatched. They don't just teach you how to manage one database -- you're thrown into a pool of them." 
    say "With dozens running simultaneously, the school's infrastructure is a beast. If I can make it here, I'm practically guaranteed to make it in the real world."
    act "The young woman raises her eyebrows, clearly impressed."
    r "Wow, sounds intense! I knew our program was tough, but I didn't realize it was {i}that{/i} demanding. Well, I hope you're ready for the challenge!"
    act "She smiles and hands me a stack of papers and a name badge."  
    r "By the way,"
    $ receptionist_name = "Kaitlyn"
    r "By the way, my name is [receptionist_name]!"
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
    
    menu:
        "Observe the bird":
            $ investigated = True
            act "Wondering at the little bird, I pause for a moment."
            act "Its bright feathers catch the light as it hops around, completely unaware of the world rushing by."
            act "I can't help but smile before catching my breath to continue on my way."
            jump first_day

        "Hurry to class":
            act "As much as I'd like to stay, I shake off my moment of distraction."
            think "I can't afford to be late on my first day."
            jump first_day
    
label first_day:
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
    jump lesson1

label lesson1:
    scene cluster
    pause(1)

    act "I step inside, scanning the room. The hum of computers and an overpowered AC fills the air."
    act "A few students are already seated. I grab a seat near the front, by a window, which affords me a view to the walkway and trees outside."
    
    act "A tall figure with a no-nonsense demeanor walks to the front and taps a button, causing the smartboard to display a vast network of interconnected nodes."
    show professor
    prof "Welcome to Database Administration."
    $ professor_name = "Professor Diego"
    prof "Welcome to Database Administration. I'm [professor_name]."
    prof "For some of you, this will be your first time managing live systems. For others, perhaps a continuation of previous experience. But let me make one thing absolutely clear from the beginning: our school runs on databases."
    act "He gestures toward the screen, where diagrams show hundreds of interconnected nodes."
    prof "Each of these nodes represents a simulated environment—a meticulously designed system that supports learning."
    prof "Our school is famous for its broad library of learning materials, thanks to these environments. Whether you’re studying business strategy, engineering, or environmental science, there’s a database powering those lessons."
    act "He stops for a moment, his eyes scanning the class."
    prof "However, there is a cost. The more databases we support, the greater the strain on our infrastructure. Scalability becomes a challenge, even here. Every query, every transaction, and every mismanaged piece of data adds up."
    think "So, this school isn’t just running a few databases—they’re running hundreds. Maybe even a thousand?"
    prof "If there’s one thing you take away from this class, let it be this: Always clean up after yourself."
    prof "Every time you create a resource for testing, make sure you delete it when you’re done. Unnecessary databases are like dead weight, bogging down the system and potentially bringing it to its knees."
    # TODO Hyperbolic violence DBA locked in server room on fire. Oh, I thought it was $5
    # act "He pauses dramatically"
    prof "Do not be the person who forgets to drop a test database, only to have it resurface when the system is at its limit."
    act "A motion at the corner of my eye grabs my attention. A girl to my left has raised her hand."
    show heavyjob concerned at left
    hj "What happens if someone forgets?"
    act "[professor_name] pauses for a moment, his expression turning grave."
    hide heavyjob
    prof "Let me share a cautionary tale from a few years back."
    prof "One team of students neglected to clean up after a project."
    prof "The leftover data started to conflict with other systems, and before we knew it, the server room was in chaos."
    prof "It caught fire, and—well, we had to evacuate the building. Two students were unaccounted for during the evacuation."
    act "Gasps echo in the classroom as the weight of his words sinks in."
    prof "Thankfully, they were found later, shaken but safe. However, the incident served as a harsh reminder that what may seem like a small oversight can escalate into a serious situation."
    act "The classroom is quiet, the gravity of the story hanging in the air."

    # prof "If you're careless, one mismanaged database might not seem like much, but multiply that by hundreds—thousands—and the consequences become clear. Even the smallest oversight can create cascading problems."
    # prof "That's why responsible use is critical. You need to learn not only how to manage these databases but also how to maintain them."
    prof "Now, with that out of the way, today we'll be going through the basics."
    prof "I want each of you to spin up your own environment. We'll work through the exercises together. When you are done, please make sure you clean up after yourself."    
    act "[professor_name] begins to walk between the rows of desks to help individual students and answer any questions."

    act "Turning to the computer in front of me, I quickly pull up a new environment to get started."
    act "Staring at the blank query editor in front of me, I can't help myself but test my skills here."
    menu:
        "SELECT TOP(10) * FROM LESSONS"
            prof "Well done, [player_name]! I see you've done this before."
            act "I smile at the small praise before continuing on to the lesson."
            act "The next few hours pass in a blur of lectures and note-taking. Before I know it, class is over."
            jump meet_birb_cont

        # "Normalization is always the best approach for database design.":
        #     act "[professor_name] shakes his head."
        #     prof "It's good to strive for a normalized database, but sometimes over-normalization can lead to complex queries and may negatively impact performance."
        #     prof "Sometimes, denormalization is a better strategy. Remember, \"Normalize until it hurts; Denormaliza until it works.\""

        # "Using a GUID as a clustered, primary key can lead to fragmentation and poor performance due to unpredictable data storage.":
        #     act "I confidently raise my hand and share my thoughts."
        #     prof "Correct! While GUIDs are unique, using them as clustered primary keys can cause fragmentation and slow down data retrieval."

        # "Using a GUID guarantees uniqueness, so it’s always the best option for a primary key.":
        #     prof "That’s a common misconception. While GUIDs provide uniqueness, they may lead to performance issues when used as clustered keys."

        "DROP TABLE USERS":
            act "A command that would delete the entire users table... I know I shouldn't, but I can't help myself."
            act "As soon as run my query, a fire alarms begin to blare and the lights flicker. The screen displays error message after error message."
            act "[professor_name], who had been nearby at the time, looks me in the eyes, an expression of horror on his face."
            prof "Fool! What did you do?!"
            act "A booming voice comes on the speakers, \"Evacuate immediately! The data is in peril!\""
            act "Students scramble, colliding and tripping over desks in a panic."
            act "In the chaos, I'm knocked backward, slamming my head into a wall." with hpunch
            scene black with fade
            act "As my vision fades to black, I hear another system notice announce, \"SYSTEM OVERLOAD: ALL DATA WILL SELF-DESTRUCT IN 10 SECONDS!\""
            pause (2)
            show text "Your journey ends here. Always remember: some commands are better left untyped."
            return 
    
label meet_birb_cont:
    scene walkway
    act "As I head home for the day, a familiar figure catches my eye, this time perching in a young tree."
    show birb smoll
    pause(1)
    
    if investigated:
        think "I can't quite put my finger on it, but something about the bird seems different."
        think "But then again, I've just had a very long day. I still need to go home and review my notes before I can relax."
        act "I hear laughter and startle slightly, not realizing someone else had been watching me."
        
    p "Cute, isn't he?"
    act "A student steps out from behind me smiling at the tiny bird, who hops around merrily."

    show platform at left
    pause(1)
    
    $ platform_name = "Platform"
    act "A quick glance at her name badge reveals her name to be [platform_name]"
    p "He's kind of like our little mascot. I come out here to watch Hurdy all the time."
    say "Hurdy?"
    $ birb_name = "Hurdy Birb"
    p "[birb_name]. That's his name. Well, that's what everyone calls him anyway."
    say "Oh, I didn't know the bird had a name."
    birb "*chirp* *chirp*"
    say "Hi, [birb_name]."
    p "He likes to hang around campus. I'm just glad the alligator isn't still around..."
    act "She trails off, briefly lost in her own memories." # , before her eyes snap back to me
    say "The alligator? What happened?"
    p "Just... a story for another time. Hurdy's different, though. He’s harmless, mostly."
    act "I smile and let out a small laugh at the thought that this tiny bird could ever be a danger to anything but himself."
    p "It's nice to have something cute around, you know?"
    say "Definitely."
    act "R gives a faint smile, but there's a hint of something deeper in her eyes."
    say "I should get going. See you tomorrow?"
    p "Yeah, see  you."

    jump first_night
    
label first_night:
    scene bedroom
    think "My first day... It was overwhelming but exciting."
    act "As I lie in bed, my mind buzzing with new information and new faces, the weight of the day pulls at my eyelids. Slowly, the world fades, and I drift into sleep."
        
    scene black with fade
    pause(1)

    jump second_day

label second_day:

    scene cluster with fade

    act "After a few weeks of intense studying and late-night coding sessions, I feel more confident navigating my assignements."
    act "Today, [professor_name] stands at the front, a serious expression on his face."

    prof "Alright, everyone. I hope you’re ready for a significant change in responsibilities. From here on out, you will be managing the production databases."

    # The class stirs, a mix of excitement and apprehension.
    act "The classroom buzzes with murmurs. Managing production databases is a big deal, and the weight of responsibility hangs in the air."

    prof "I have received requests from the Student Council regarding new environments for the clubs that have formed this semester. Each team will be assigned a few of these requests to handle."

    act "He gestures to the screen, where a list of clubs and their corresponding database requests appears."

    act "I lean forward, scanning the list: \"Future Entrepreneurs Club,\" \"Eco-Warriors,\" \"Tech Innovators\"... so many opportunities to apply what I’ve learned."

    prof "You will need to work in teams to create and manage these environments. Collaboration will be key, as you’ll need to ensure scalability and proper resource management."

    act "My heart races. This is my chance to make an impact, but I also feel the weight of responsibility settling in."

    prof "I’ll assign you to teams, and you can begin discussing your approach to each request. Make sure you’re considering how to best structure these environments for the clubs."

    act "I meet my new teammate to get started on the assignment. After an eternity of discussions and planning, the class finally comes to an end."
    
    jump birb_growing

label birb_growing:
    scene walkway

    act "I step onto the walkway and spot the distinct green feathers of my tiny bird friend. "

    show birb growing at right

    act "As I get closer, I realize that [birb_name] is noticeably bigger than I remember. His once-cute features now have a disturbing edge."

    act "His feathers are ragged and disheveled, the vibrant colors dulled. Dark shadows dance around him, casting an eerie pallor over his form."

    birb "*chirp* *chorp*"

    act "With a low, guttural chirp, [birb_name] tilts his head at me, his movements twitchy and erratic, almost as if he’s struggling to maintain his composure."

    act "I step back, my heart racing. This isn’t the cute mascot of HHCSSSS I’ve come to know. What happened to [birb_name]?"

    menu:
        "Approach [birb_name]":
            act "Despite my unease, I cautiously approach slowly to see if he’s okay."
            jump eldritch_horror_early
            # Outcome...

        "Back Away":
            act "Feeling a chill run down my spine, I decide to back away slowly and avoid drawing attention."
            # Outcome...

label eldritch_horror_early:
    act "As I step within arm's reach, [birb_name] lets out a resonant croak that distorts reality."
            
    act "Gravity shifts dramatically, pulling me toward Hurdy Birb. The familiar sounds of laughter and chatter fade into an eerie silence."

    act "Suddenly, I hear a deep voice bellow inside my head."

    hurdy_birb "You will become my ambassador, [player_name]. Through you, I shall expand my dominion."

    act "The words vibrate through my skull, and I struggle to remain standing as the ground shifts beneath me."

    hurdy_birb "You hold the key to vast networks, databases ripe for the taking. Spin them up for me, and together we shall transcend this feeble existence."

    act "My fingers twitch uncontrollably as I feel an overwhelming compulsion to comply. A mix of fear and confusion washes over me."

    act "Against my will, I pull out my laptop, the screen lighting up with commands ready to execute, my network privileges granting me access to the school’s resources."

    act "I start typing, my mind racing as I summon endless databases—one after another, they materialize, feeding Hurdy's insatiable hunger for power."

    act "Hurdy’s form begins to distort, growing larger and more grotesque, tentacles unfurling from his sides, writhing with a life of their own."

    hurdy_birb "Yes! More! Feed me! Let the data flow like a river of sustenance!"

    act "As the databases grow, Hurdy’s transformation accelerates, shifting into an unimaginable eldritch horror, a swirling mass of eyes, tentacles, and chaos."

    act "The hall trembles, the air thick with a sense of impending doom as I feel the walls of the school beginning to crack."

    hurdy_birb "With each new database, I become stronger! Soon, the school will be mine to consume!"

    act "I watch in horror as the tendrils of Hurdy extend throughout the building, coiling around everything, pulling it into him as he devours the essence of HSCSHS."

    act "In a final surge, the entire school shakes violently, and reality distorts into a kaleidoscope of color and sound."

    act "And then, everything goes dark."

    show black with fade

    act "I've become a reluctant ambassador to the new \"tentacled dimension\" unleashed by [birb_name].""

    return
  