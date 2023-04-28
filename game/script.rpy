init python:
    config.nearest_neighbor = True

    def regblip(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/blip1.ogg", channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def groanblip(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/blip2.ogg", channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")



image duke rose:
    "duke rose 1"
    pause 0.3
    "duke rose 2"
    pause 0.3
    repeat

image duke quote:
    "duke quote 1"
    pause 0.3
    "duke quote 2"
    pause 0.3
    repeat

image duke wink:
    "duke wink 1"
    pause 0.3
    "duke wink 2"
    pause 0.3
    repeat

# Declare characters
define d = Character("Duke", callback = groanblip)
define b = Character("beet", callback = regblip)

# The game starts here.

label start:
    scene bg room
    "Welcome to the demo of \"We're Wolves.\" This is a game I'm making about werewolves. The game isn't done, nor is this demo."
    "The goal of the game is to go on 5 nights of speed dates with a group of 8 people. By the last night you must guess who isn't a werewolf."
    "Pretty cute, right? This demo takes you through one date with a very excellent man named Duke. Good luck out there."
    jump night1duke

label night1duke:

    

    "Okay, who's next"

    show duke neutral

    "..."
    "Holy shit"
    show duke rose
    d "Hello beautiful."
    d "I am Duke."

    show duke neutral

    d "But it is likely you already knew that. As a result of the fact that you saw me in your dreams last night."

    "You find yourself completely falling for Duke. {w=.2}This might be game over."

    ".{w=.2}.{w=.2}.{w=.5}Just kidding"

    d "I can benchpress a minivan."

    menu:
   
        d "I can benchpress a minivan.{fast}"


        "That is an interesting fact":
            jump dukefact

        "I am afraid of you":
            jump dukefear

label dukefact: 

    d "It is indeed an interesting fact about me."
    d "Here is another:"
    d "My friends call me D-Dog"
    d "Why do you think that is?"

    menu:
        d "Why do you think that is?{fast}"

        "The D is for Duke and dog is alliteration":
            jump dukefact2
        "You like dogs":
            jump dukefact2
           
label dukefact2:
    d "That is incorrect."
    d "It is because my pecorals are a DD cup. The OG is an abbreviation of{nw}"
    show duke quote
    d "It is because my pecorals are a DD cup. The OG is an abbreviation of{fast} \"original gangster.\""
    show duke neutral
    jump dukequestions

label dukefear: 
    d "It is only natural. My abundance of handsome attributes intimidates everyone."
    d "The hair. {w=.2}The muscles. {w=.2} The tasteful speech pattern."
    d "I truly am the honest-to-goodness{nw}"
    show duke quote
    d "I truly am the honest-to-goodness {fast}\"real deal.\""
    show duke neutral
    jump dukequestions


default d1squat = False
default d1season = False
default d1work = False
label dukequestions:
    d "Do you have any questions about yours truly?"

    $ config.menu_include_disabled = False
    menu:
        d "Do you have any questions about yours truly?{fast}"

        "What is your squat max?" if not d1squat:
            $ d1squat = True
            jump dukesquat

        "Do you have a favorite season?" if not d1season:
            $ d1season = True
            jump dukeseasons

        "What do you do for work?" if not d1work:
            $ d1work = True
            jump dukework

        "No":
            jump dukebye

label dukesquat:
    d "Ah?"
    d "Ahahahahaha{w=.2}ha{w=.2}ha{w=.4}ha"
    d "Let us not ask too much of each other. We have just met, after all."
    "He seems embarassed"
    "Ask more?"

    menu:
        "Ask more?{fast}"

        "Please, I'm very interested":
            jump dukesquatmore
        "No":
            jump dukequestions

label dukesquatmore:
    d "I seem to be forgetting."
    d "I have it written down. {w=.5} In my house. {w=.5} Yes, {w=.5} in a journal in my house"
    d "I can tell you tomorrow. {w=.2}I swear it on my name."
    jump dukequestions

label dukeseasons:
    d "I do indeed have a favorite season. It is Winter."
    d "Because Winter has the longest nights. {nw}"
    show duke wink
    d "Because Winter has the longest nights. {fast} If you are familiar with what I mean."
    show duke neutral
    d "I mean that there is more time in the gym without the sun up."
    d "I did not imply anything inappropriate there, did I?"
    jump dukequestions
    
label dukework:
    d "I am a personal trainer."
    d "I sense you didn't expect that."
    d "But I understand that I can be a very surprising individual."
    d "You probably expected that I am a librarian, because of how well read I am."
    d "While it is true, I'm more of a writer than a reader."
    d "That is, I write out routines for my clients."
    d "I don't do much writing beyond that.{w=.5} And acrostic poems."
    jump dukequestions


label dukebye:
    d "Ah, it looks like our time is up."
    d "I will miss you dearly."
    d "We know each other so well now, we are almost partners."
    "It has been five minutes, give or take."
    show duke wink
    d "Goodbye, my love."
    d "Until tomorrow."
    hide duke
    "Wow."
    jump night1beet
    
label night1beet:
    show beet neutral
    b "hey dude"
   
    menu:
        b "hey dude{fast}"

        "Hi": 
            jump beetHi

    #   "hi": 
    #      jump beetlowercase
   

label beetHi:
    b ".{w=.5}not much of a talker huh"
    b "im usually not on this side of the conversation lol"
    b "so uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    b "what do you do as a job"
    #allow keyboard entry. anything over ten characters "im not reading all that"
    $ job = renpy.input("Job?")
    $ job = job.strip()
    jump beetjob

label beetjob:
    if len(job) > 10:
        b "im not reading all that"
        b "youve got a long ass title man"
        b "couldnt make it a little more consumable for me ?"
        b "get it down to nine letters ? or something ?"
        b "whatever its fine i dont mind"
        b "you can do what youd like i dont judge"
    #if
    else:
        b "thats neat"
        b "thats a really cool job"
        b "im sure its fulfilling and stuff"
        b "are you any big projects youre working on at your job"
        $ proj = renpy.input("Big projects?")
        $ proj = proj.strip()
        if len(proj) > 10:
            b "phew wow that sure is a lot"
            b "must be stressful"
        #if
        else:
            b "oh that doesnt sound so bad"
            b "i think even i could do that"
        #else
    #else

    return

    
label beetlowercase:
    b ""
    return