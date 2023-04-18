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

define g = Character("Jean", callback = regblip)
define d = Character("Duke", callback = groanblip)

# The game starts here.

label start:
    "Welcome to the demo of \"We're Wolves.\" This is a game I'm making about werewolves. The game isn't done, nor is this demo."
    "The goal of the game is to go on 5 nights of speed dates with a group of 8 people. By the last night you must guess who isn't a werewolf."
    "Pretty cute, right? This demo takes you through one date with a very excellent man named Duke. Good luck out there."
    jump night1duke

label night1duke:

    scene bg room

    "Okay, who's next"

    show duke neutral

    "..."
    "Holy shit"
    show duke rose
    d "Hello beautiful."
    d "I am Duke."

    show duke neutral

    d "But it is likely you already knew that. Since you saw me in your dreams last night."

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
    d "Here's another:"
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

label dukequestions:
    d "Do you have any questions about yours truly?"

    menu:
        d "Do you have any questions about yours truly?{fast}"

        "What is your squat max?":
            jump dukesquat
        "Do you have a favorite season?":
            jump dukeseasons
        "No":
            jump dukebye

label dukesquat:
    d "Ah?"
    d "Ahahahahaha{w=.2}ha{w=.2}ha{w=.8}ha"
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
    d "I do indeed have a favorite season. It's Winter."
    d "Because Winter has the longest nights. {nw}"
    show duke wink
    d "Because Winter has the longest nights. {fast} If you know what I mean"
    show duke neutral
    d "I mean that there is more time for a morning run without the sun up."
    d "I didn't imply anything inappropriate there, did I?"
    jump dukequestions
    
label dukebye:
    d "I must go."
    show duke wink
    d "Goodbye, my love."
    show duke neutral
    
    return
