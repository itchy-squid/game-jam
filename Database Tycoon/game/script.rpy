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
            if re.match("^[A-Za-z .]*$", name):
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
define heavyjob = Character("[heavyjob_name]", color="#005eb8")
define birb = Character("[birb_name]", color="#009639")
define sf = Character("[safety_name]", color="")
define prof = Character("[professor_name]", color="#8A2BE2")
define platform = Character("[platform_name]")
define powershell = Character("[powershell_name]")

default player_name = ""

default birb_name = "???"
default heavybid_name = "???"
default heavyjob_name = "???"
default safety_name = "???"
default professor_name = "???"
default platform_name = "???"
default powershell_name = "???"
default receptionist_name = "???"

default investigated = False
default encountered = False

image birb smoll = Image("hurdybirb.png", xalign = 0.9, yalign = 0.7)
image hurdybirb still smoll = Image("hurdybirb still smoll.png", xalign = 0.9, yalign = 0.7)

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
    act "Sitting up in bed, I glance around my room, taking in the chaos of my preparations. Textbooks are piled high; my laptop is open with a to-do list; my backpack sits ready by the door."    
    think "Oh right, today is finally the day! My first day. I'm really nervous..."
    think "I guess I'd better get ready."
    
    scene entrance with fade

    act "As I approach to the school, the world feels different. The excitement of a new beginning fills the air, mingled with the scent of fresh grass and morning dew."
    act "I can hardly believe I made it in. This prestigious school, known for its intense programs and top-notch facilities, is finally mine to explore."
    act "It's my first day at HCSSHS—Heavy Construction Systems Specialists High School."    
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
    $ heavybid_name = "HeavyBid"
    heavyjob "Five cents? I mean... it's pretty small, [heavybid_name]. C-Couldn't that be from an unplanned expense?"
    hb "Not when the numbers are this precise! Every penny should be accounted for."
    heavyjob "Could it be... I don't know, like maybe something technical? The databases? We've been adding more recently, haven't we?"
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
#    prof "Every time you create a resource for testing, make sure you delete it when you’re done. Unnecessary databases are like dead weight, bogging down the system and potentially bringing it to its knees."
    
#    prof "Do not be the person who forgets to drop a test database, only to have it resurface when the system is at its limit."
    act "A motion at the corner of my eye grabs my attention. A girl to my left has her hand raised."
    $ heavyjob_name = "HeavyJob"
    prof "[heavyjob_name], you have a question?"
    show professor at right with move
    show heavyjob concerned at left
    heavyjob "What happens if someone forgets?"
    act "[professor_name] pauses for a moment, his expression turning grave."
    hide heavyjob
    show professor at center with move
    prof "Let me share a cautionary tale from a few years back."
    prof "One team of students neglected to clean up after a project."
    prof "The leftover data started to conflict with other systems, and before we knew it, the server room was in chaos."
    prof "It caught fire, and—well, we had to evacuate the building. Two students were unaccounted for during the evacuation."
    act "Gasps echo in the classroom as the weight of his words sinks in."
#    prof "Thankfully, they were found later, shaken but safe. However, the incident served as a harsh reminder that what may seem like a small oversight can escalate into a serious situation."
#    act "The classroom is quiet, the gravity of the story hanging in the air."
    # prof "If you're careless, one mismanaged database might not seem like much, but multiply that by hundreds—thousands—and the consequences become clear. Even the smallest oversight can create cascading problems."
    # prof "That's why responsible use is critical. You need to learn not only how to manage these databases but also how to maintain them."
    
    prof "Now, with that out of the way, today we'll be going through the basics."
    prof "I want each of you to spin up your own environment. We'll work through the exercises together. When you are done, please make sure you clean up after yourself."    
    act "[professor_name] begins to walk between the rows of desks to help individual students and answer any questions."

    act "Turning to the computer in front of me, I quickly pull up a new environment to get started."
    act "Staring at the blank query editor in front of me, I can't help myself but test my skills here."
    
    menu:
        "EXEC sp_updatestats":
            prof "Well done, [player_name]! I see you've done this before."
            act "I smile at the small praise before continuing on to the lesson."
            act "The next few hours pass in a blur of lectures and note-taking. Before I know it, class is over."
            jump meet_birb_cont

        "TRUNCATE TABLE USERS":
            act "A command that would delete all users... I know I shouldn't, but I can't help myself."
            act "As soon as run my query, a fire alarms begin to blare and the lights flicker. The screen displays error message after error message."
            act "[professor_name] looks me in the eyes, an expression of horror on his face."
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
    show hurdybirb still smoll
    pause(1)
    
    if investigated:
        think "I can't quite put my finger on it, but something about the bird seems different."
        think "But then again, I've just had a very long day. I still need to go home and review my notes before I can relax."
        act "I hear laughter and startle slightly, not realizing someone else had been watching me."
        
    platform "Cute, isn't he?"
    act "A student steps out from behind me smiling at the tiny bird, who hops around merrily."

    show platform at left
    pause(1)
    
    $ platform_name = "Platform"
    act "A quick glance at her name badge reveals her name to be [platform_name]"
    platform "He's kind of like our little mascot. I come out here to watch Hurdy all the time."
    say "Hurdy?"
    $ birb_name = "Hurdy Birb"
    platform "[birb_name]. That's his name. Well, that's what everyone calls him anyway."
    birb "*chirp* *chirp*"
    platform "He likes to hang around campus. I'm just glad the alligator isn't still around..."
    act "She trails off, briefly lost in her own memories." # , before her eyes snap back to me
    say "The alligator? What happened?"
    platform "Just... a story for another time. Hurdy's different, though. He’s harmless, mostly."
    act "I smile and let out a small laugh at the thought that this tiny bird could ever be a danger to anything but himself."
    platform "It's nice to have something cute around, you know?"
    act "[platform_name] gives a faint smile, but there's a hint of something deeper in her eyes."
    say "I should get going. See you around?"
    platform "Yeah, see  you."

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

    act "After a few weeks of intense studying and late-night coding sessions, I feel more confident navigating my lessons."
    act "Today, [professor_name] stands at the front, a serious expression on his face."

    show professor
    pause(1)
    prof "Alright, everyone. I hope you’re ready for a significant change in responsibilities. From here on out, you will be managing the production databases."

    # The class stirs, a mix of excitement and apprehension.
    act "The classroom buzzes with murmurs. Managing production databases is a big deal, and the weight of responsibility hangs in the air."

    prof "I have received requests from the Student Council regarding new environments for the clubs that have formed this semester. Each team will be assigned a few of these requests to handle."

    act "He gestures to the screen, where a list of clubs and their corresponding database requests appears."

    act "I lean forward, scanning the list: \"Future Entrepreneurs Club,\" \"Eco-Warriors,\" \"Tech Innovators\"... so many opportunities to apply what I’ve learned."

    prof "You will need to work in teams to create and manage these environments. Collaboration will be key, as you’ll need to ensure scalability and proper resource management."
    $ powershell_name = "PowerShell"
    prof "[professor_name] motions towards a student nearby. [player_name], you're with [powershell_name]."
    show professor at left with move
    show powershell at right
    act "[professor_name] continues down his list, assigning teams. PowerShell glances at me, her disinterest palpable. It’s clear she’d rather be anywhere else."

    say "So, um, should we get started?"
    powershell "What do you mean by 'get started'? I'm going to need you to be specific."
    say "Okay, um, we need to create the environment for the Future Entrepreneurs Club. Let’s start with that."
    powershell "And what about the structure? What tables do you want? What data types? They only gave us a one-sentence description of what they want."
    say "Right... let’s just create some duplicate databases off of the golden copy, and we’ll figure out the rest later."
    act "With that, I start typing, eager to grind something out before PowerShell has the chance to criticize me further."
    act "After an eternity of typing away in awkward silence, the class finally comes to an end."
    
    jump birb_growing

label birb_growing:
    scene walkway

    act "I step onto the walkway and spot the distinct green feathers of my tiny bird friend. "
    show hurdybirb growing at right
    act "As I get closer, I realize that [birb_name] is noticeably bigger than I remember. His once-cute features now have a disturbing edge."
    act "His feathers are ragged and disheveled, the vibrant colors dulled. Dark shadows dance around him, casting an eerie pallor over his form."
    birb "*chirp* *chorp*"
    act "With a low, guttural chirp, [birb_name] tilts his head at me, his movements twitchy and erratic, almost as if he’s struggling to maintain his composure."
    act "I step back, my heart racing. This isn’t the cute mascot of HHCSSSS I’ve come to know. What happened to [birb_name]?"

    menu:
        "Approach [birb_name]":
            $ encountered = True
            act "Despite my unease, I cautiously approach to see if he’s okay."
            act "As I step within arm's reach, [birb_name] lets out a resonant croak that distorts reality."
            act "Gravity shifts dramatically, pulling me toward Hurdy Birb. The familiar sounds of laughter and chatter fade into an eerie silence."
            act "Suddenly, I hear a deep voice bellow inside my head."
            birb "You will become my ambassador, [player_name]. Through you, I shall expand my dominion."
            act "The words vibrate through my skull, and I struggle to remain standing as the ground shifts beneath me."

        "Back away":
            act "Feeling a chill run down my spine, I decide to back away slowly and avoid drawing attention."
        
    show platform at left
    platform "Hey, [player_name]! Are you okay? You look a little sick."

    if encountered:
        act "Reality snaps back into place as [platform_name]'s voice breaks through the haze of distortion."
        act "I shake my head, wondering if what just happened was real."
        
    say "Yeah, great. I was just about to head to lunch."
    platform "Mind if I join you?"
    
#    menu:
#        "Have lunch with [platform_name]":
    say "Sounds fun! I could use a change of pace."
    jump lunch_with_platform
        
#        "Have lunch alone":
#            say "I'm not feeling great. I think I'm gonna get away a bit for some fresh air. Maybe another time."
#            platform "No worries; you really do look awful. Feel better soon. If you need to take off, just let the teacher know."
#            jump third_class
        
label lunch_with_platform:
    scene lunchroom
    show platform at left
    # todo continuity issues. he only just got access to prod. why would this complaint be valid.
    act "As we chat about nothing in particular, I sit down at a table with [platform_name]."
    say "Ugh, I swear, I’m drowning in these databases."
    say "Every time I think I’ve got them under control, another one pops up out of nowhere."
    say "I can barely keep track anymore."

    # Platform responds, trying to reassure the MC
    platform "Yeah, the workload can pile up fast. But hey, that’s the beauty of being here, right?"
    platform "Just think of it as... training for the real world."
    
    # HeavyBid arrives and joins the conversation
    show heavyjob concerned at right
    heavyjob "Hey, have either of you seen Trucking around lately?"
    platform "Trucking... from Fleet? No, I haven’t seen him in a while. Why, what’s up?"
    heavyjob "I needed to work on a project with him, but... he hasn’t shown up to school for days now."
    heavyjob "At first I figured he was ghosting me, but now I’m getting worried."
    say "Wait, Trucking? Isn’t he the guy who was always working on those massive environments?"
    platform "Yeah, that’s him. Strange, though... Maybe he’s overloaded with work?"
    heavyjob "I don’t know. I’m thinking of talking to the student council, but..."
    platform "He disappears from time to time. I wouldn't worry too much."
    heavyjob "You're probably right. If either of you spot him, let me know, please."
    hide heavyjob
    
    act "[platform_name] watches [heavyjob_name] walk away. [platform_name]'s smile falters for just a moment before she regains her composure."
    jump pairing_session



label pairing_session:
    scene black with fade
#    act "Over the next few weeks, the memory of that encounter with [birb_name] lingers in my mind. I frequently find myself distracted in class."
#    act "As I sit through lectures and group projects, I can’t shake the feeling that something is off. My heart races every time I pass by the ledge where [birb_name] used to perch, half-expecting to see him there, waiting."
#    act "Each day blurs into the next, a mix of studying, group work, and an underlying tension that keeps me on edge. The familiar halls of SCHHSH now feel more like a labyrinth of secrets than a place of learning."

    # Set the scene with MC and PowerShell in the lab room
    scene dev building
    show powershell at right

    # MC starts working on the system
    say "Okay, I think I’ve isolated the issue. The database footprint is growing faster than we anticipated."
    say "Realistically we need to optimize these queries, but we can deal with that later. Just a few more tweaks—"

    # An alarm goes off, indicating something is wrong
    act "Suddenly, all of our dashboard indicators flash red. Message after message begin flooding the incident management channel."
    act "{i}[[INCIDENT ALERT: Multiple environments are inaccessible. Please investigate.]{/i}"
    show heavybid at left
    hb "{i}[[The Estimating team can't get into its environments. A bunch of other students are saying they're locked out of their classes, too.]{/i}"
    hide heavybid
    powershell "Several of the elastic pools are maxing out. CPU is at 200%%"
    say "What the hell? That makes no sense. We’re not even pushing data... "
    act "From down the hallway, a faint, warbling chirp begins to steadily grow louder."

    if encountered:
        act "The walls around me begin to ripple like liquid, twisting and bulging as if something massive is pressing from the other side."
        act "Overhead, the lights flicker violently, casting shifting shadows that seem to crawl along the ceiling, their shapes unnatural."
    
    menu: 
        "Investigate the chirping":
            jump investigate_chirping

        "Roll back your changes":
            jump rollback_changes

label investigate_chirping:

    act "The sound echoes faintly down the hallway, bouncing off the walls."
    say "I should check the server room. That sound can't just be a coincidence."
    hide powershell
    act "As I step forward, the ground beneath me shifts unnaturally, pulling me sideways one moment and pushing me down the next, making each step a struggle."
    act "The door to the server room looms ahead, slightly ajar."

    scene server room pulsing

    act "Inside, the server racks pulse like grotesque, living organs. The machines, once cold and metallic, now throb with a sickly rhythm."
    act "Cables writhe like veins, coiling in and out of the servers, twitching with every pulse."

    say "What is this...?"

    act "Then I see it—perched atop the largest server."
    
    # Hurdy Birb in final form appears
    show hurdybirb final

    act "His feathers have stretched into long, jagged spines, twisting into grotesque shapes."
    act "His once-small eyes glow with an eerie, unnatural light, now cold and piercing."
    act "Tentacle-like appendages extend from his wings, digging into the servers, feeding on the chaos."
    act "The warbling chirping that once seemed harmless now distorts into a horrific screech, echoing through the room."
    act "Hurdy’s massive, monstrous form pulses in rhythm with the servers, as if the entire system is an extension of him now."

    act "Hurdy turns his gaze towards me. The low thumping of the servers, now in sync with Hurdy’s breathing, grows louder and more erratic."
    act "Every instinct screams at me to act. I could stand my ground, but is that really the best choice? Maybe I can try to find help before it’s too late."
        
    menu:
        "Brace myself and face it head-on":
            jump fight
        
        "Run and get help before it consumes everything":
            jump get_help

label fight:
    act "I steel myself, heart pounding, as the room seems to warp around me. The very air grows heavy, thick with... something. Hurdy's twisted, monstrous form looms impossibly large."
    act "For a moment, everything is still."
    act "Then, it happens. A blur of motion, faster than thought, and the air is alive with the writhing of tendrils. I feel them move, weaving through the space between moments."
    act "I lash out instinctively, but my body betrays me—sluggish, stiff. Years of sitting at my desk, hunched over a terminal, come crashing down on me in this moment."
    act "The tendrils coil around my arm, my legs... They sink into the core of my being."
    say  "No—"
    act "Reality begins to slip. My limbs feel distant, disconnected, as if I’m watching my body from some far-off place. I try to resist, to pull away, but every attempt only draws me deeper into the abyss."
    act "The sound of Hurdy’s chirping distorts, becoming a maddening symphony of whispers, too many voices, too many languages, inhuman. It fills my mind, smothering my will beneath its weight."
    say  "I... I can't..."

    scene black with fade

    act "The room melts into darkness, and all that remains is Hurdy—his form no longer confined by shape or logic. He is everything, everywhere, his tendrils an infinite web of control."
    act "I can feel my mind unraveling, thoughts dissolving into fragments as the tendrils pulse, deeper, deeper... until I am no longer sure where Hurdy ends and I begin."
    think "Is this... me?"
    act "Hurdy’s screech rises again, triumphant, but now it’s inside me. I am no longer separate. I am no longer... me."
    act "I've become a reluctant ambassador to the new \"tentacled dimension\" unleashed by [birb_name]."
    return

label get_help:
    act "There’s no time. I need to run."
    scene dev building
    # Scene: Hallways (MC running away)
    act "I sprint as fast as I can, but the air is thick with reality warping in on itself."
    scene cluster
    show professor
    say "[professor_name], [birb_name] has taken over the server room!"
    act "His eyes narrow with a piercing stare. A still moment passes, then he cracks his knuckles."
    prof "Evacuate the building. Get the students out of here. The staff will take care of this."

    scene bedroom with fade
    act "Hours later, I sit at my desk, staring at the flickering light of my computer screen."
    act "After I left the classroom, everything happened so fast."
    
    scene entrance with dissolve
    act "The students gathered at the entrance in small groups, murmuring in confusion."
    act "Police cars and fire trucks quickly lined the street in front of the school, their lights flashing silently."
    act "SWAT teams marched into the building, fully armed, while we stood there without any news of what was happening inside."
    act "Eventually, we were told to evacuate the area..."

    scene bedroom with fade
    act "Now, back in my room, I watch the news without fully processing what I'm seeing, the screen glowing faintly."
    act "The live feed crackles with interference, a drone of distorted sound, as the camera focuses on the remains of the school."
    act "The building... it no longer resembles something made by human hands."
    act "The walls writhe and twist, a living structure, buckling under the weight of some unfathomable force."
    act "And then I see it."
    act "The air above the school ripples, like the fabric of the world is being pulled apart, threads of reality unraveling."
    act "Beyond the tear... something stirs. Something ancient, something that should not exist."
    act "Dark, writhing tendrils slither down from the sky, their shapes lash out. Buildings, cars, trees are consumed by the void."

    act "The sky... is no longer a sky. Something pressing down on the world, something multidimensional,.. greater than my limited senses can perceive."

    act "The feed flickers, the image distorting, breaking apart into shards of static. The world goes dark." 
    scene black
    say "This... is the end, isn’t it?"
    return
    
label rollback_changes:
    if encountered:
        act "I can taste reality bending around me, but I can’t focus on that right now."
    act "I can't exactly roll back my query, but I can kill it. Maybe that will stabilize things."
    say  "Alright. Let's just undo my last set of changes. That should stop the bleeding."
    act "[powershell_name]'s fingers fly across the keyboard as we begin to abort."
    jump to_be_continued

    show terminal_warning with dissolve

    say  "Come on, come on... Rollback complete. Just give me something."

    # The building begins manifesting issues around the MC
    "Suddenly, the floor beneath me begins to shake. The lights overhead flicker violently, casting warped shadows along the walls."

    scene mc_terminal_glitch with dissolve

    "The monitors in front of me glitch and distort, the code on the screen twisting into incomprehensible symbols."
    "From the corner of my eye, I see the walls themselves ripple, as though the building is... breathing."

    say  "What the hell is happening to this place...?"

    "A loud crack echoes through the hallway outside my door, followed by the groaning of metal, as if the entire structure is starting to warp under some unseen pressure."
    
    say  "Okay, that rollback better kick in fast..."

    # A brief lull in the chaos
    "Just as the noise and chaos reach a fever pitch, everything stops."
    "The shaking ceases, the flickering lights stabilize, and for a moment, the world is silent."

    say  "Wait... Did that actually work?"

    "I stare at the screen. The warnings are still there, but the system seems to be... holding. I take a deep breath, trying to calm my racing heart."

    say  "Maybe I fixed it... Maybe that rollback was enough."

    # The chaos begins to pick back up
    "But then, just as I let out a sigh of relief, I hear it again. That low, warbling chirp."
    "The lights begin to flicker once more, and the ground trembles beneath my feet."

    say  "No... It’s not over."

    "Suddenly, the screens crackle to life, displaying new errors. Warnings flash even faster than before. The whole system is unraveling again."

    show terminal_error with dissolve

    say  "The rollback only delayed it... This isn’t just about my changes. It’s the whole system. It’s the tech debt."

    # Realization and starting to clean up the databases
    say  "Hurdy’s growing because of all the neglected issues, all the forgotten databases. It’s not just me—it’s everything that’s piled up over time."

    "I type quickly, pulling up the list of all the unused, bloated databases that have been accumulating for months. There's so much... more than I even realized."

    say  "If I start cleaning this up... maybe I can stop this."

    "I begin the process of clearing out the dead weight, deleting unnecessary databases, optimizing configurations that should have been fixed ages ago."

    say  "No more shortcuts. I need to clean this entire system up if we’re going to have a chance."

    # Visual chaos around the building starts to stabilize briefly again
    "As I work, the shaking subsides once more. The flickering lights slow to a steady rhythm, the chaotic distortion of reality calming for the briefest moment."

    say  "It’s working... I just have to keep going."

    "But I know this isn’t going to be quick. The tech debt is deep. Hurdy isn’t just going to disappear with a few fixes."
    "Still, I keep typing, clearing out every unnecessary file, every forgotten database. It’s the only way."

    return

label to_be_continued:
    scene black with fade
    show text "to be continued..."
    pause
    return
  