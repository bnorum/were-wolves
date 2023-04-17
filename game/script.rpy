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


# Declare characters

define g = Character("Jean", callback = regblip)
define d = Character("Duke", callback = groanblip)

# The game starts here.

label start:

    scene bg room

    show jean smile
    g "soo... youre pretty weird huh"

    menu:

        g "soo... youre pretty weird huh{fast}"

        "Yeah":
            jump yeahjean

        "No":
            jump nojean

label yeahjean:

    g "lol i didnt expect you to admit to it"

    jump afternoyeah

label nojean:

    g "lol you are"

    jump afternoyeah

label afternoyeah:

    g "pretty cool that you at least answered"
    g "most people get kinda mad"
    g "you know what"
    g "date over weirdo"
    g "peace"

    hide jean smile
    jump dukestart

label dukestart:    
    "That guy was weird. Not me. I'm not weird, right? Not werewolf-weird at least."

    "Ok who's next"

    show duke neutral

    "..."
    "Holy shit"
    show duke rose
    d "Hello beautiful."
    d "I am Duke."

    show duke neutral

    d "But you probably already knew that. Since you saw me in your dreams last night."

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
    jump dukeafter

label dukefear: 
    d "It is only natural. My abundance of handsome attributes intimidates everyone."
    d "The hair. {w=.2}The muscles. {w=.2} The tasteful speech pattern."
    d "I truly am the honest-to-goodness{nw}"
    show duke quote
    d "I truly am the honest-to-goodness {fast}\"real deal.\""
    show duke neutral
    jump dukeafter

label dukeafter:
    d "I must go."
    d "Goodbye, my love."
    return
