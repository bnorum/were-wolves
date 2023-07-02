init python:
    config.nearest_neighbor = True

    def beetblip(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/blip1.ogg", channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def dukeblip(event, **kwargs):
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

image beet paper:
    "beet paper 1"
    pause 0.3
    "beet paper 2"
    pause 0.1
    "beet paper 3"
    pause 0.3
    "beet paper 2"
    pause 0.1
    repeat

# Declare characters
define d = Character("Duke", callback = dukeblip)
define b = Character("beet", callback = beetblip)

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
            jump dukefinal1

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


label dukefinal1:
    d "At this point, I would have liked to offer you a minigame in exchange for an interesting fact about me."
    d "But, alas, I had a fog in my mind and left my minigame in the car."
    jump dukebye

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

   

label beetHi:
    b ".{w=.5}not much of a talker huh"
    b "im usually not on this side of the conversation lol"
    b "so uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    b "what do you do as a job"
    # allow keyboard entry. anything over ten characters "im not reading all that"
    $ job = renpy.input("Job?")
    $ job = job.strip() # remove spaces
    jump beetjob

label beetjob:
    if len(job) > 10:
        b "im not reading all that"
        b "youve got a long ass title man"
        b "couldnt make it a little more consumable for me ?"
        b "get it down to nine letters ? or something"
        b "whatever its fine i dont mind"
        b "you can do what youd like i dont judge"
    #if
    else:
        b "thats neat"
        b "thats a really cool job"
        b "im sure its fulfilling and stuff"
        b "are there any big projects youre working on at your job"
        $ proj = renpy.input("Big projects?")
        $ proj = proj.strip()
        if len(proj) > 10:
            b "phew wow that sure is a lot"
            b "must be stressful"
            b "youre so strong"
        #if
        else:
            b "oh that doesnt sound so bad"
            b "i think even i could do that"
        #else
    #else
    b ".."
    b "okay well anyway you dont seem to be talking much"
    b "which is fine but im gonna need some effort"
    b "so"
    show beet paper
    b "im gonna write out some questions for you to ask me on this paper"
    b "ok here."
    show beet neutral
    b "read these out please"
    jump beetdanquestions


default danlike = False
default dansong = False
default danalbum = False
default danband = False

label beetdanquestions:
    menu:
        b "read these out please {fast}"

        "do you like steely dan" if not danlike:
            $ danlike = True
            jump beetlike
        "what is your favorite steely dan song" if not dansong:
            $ dansong = True
            jump beetsong
        "what is your favorite steely dan album" if not danalbum:
            $ danalbum = True
            jump beetalbum
        "what is your favorite band" if not danband:
            $ danband = True
            jump beetband
        "Ask your own question.":
            jump beetownquestions


label beetlike:
    b "yea"
    jump beetdanquestions
label beetsong:
    b "doctor wu"
    b "so good"
    b "something about the sax and the vocals theres so much emotion in it"
    b "and its got like a story"
    b "all their songs have a story but this one is the coolest"
    b "a therapist whos more than he lets on ? so sick so relatable"
    jump beetdanquestions
label beetalbum:
    b "that is such a good question"
    b "and so many fantastic options"
    b "my favorite is the royal scam"
    b "like its their most advanced album"
    show beet finger
    b "you have to have a lot up here to understand it and stuff" #point to head animation
    show beet neutral
    b "but like. kid charlemagne man"
    b "and HAITIAN DIVORCE dude haitian divorce" #pog somehow
    b "steely damn. thats what i always say"
    b "steely damn"
    jump beetdanquestions
label beetband:
    b "the doobie brothers"
    b "LMAO just kidding steely dan"
    #pog
    b "theyre so advanced did you know that they had a cycling tour group of musicians because they thought certain players sounded better on certain songs and sometimes during concerts there would be more than six guitarists because they wanted their music to be perfect{nw}"
    b "and anyway when walter becker died it was the worst day of my life"
    jump beetdanquestions

label beetownquestions:
    b "you have your own questions"
    b "what a surprise youre full of surprises right now did you know that"
    b "go ahead"
    b "{w=.2}.{w=.2}.{w=.2}"
    b "just kidding you have to do this minigame first"
    b "boom minigame"
    b "go minigame"
    b "shit it doesnt wanna work"
    b "gimme a sec"
    hide beet
    "She's gone."
    show beet neutral
    b "yeah its broken"
    b "the mini game is broken"
    b "so none of your questions today unfortunately were gonna have to put a hold on that unfortunately"
    b "we can do this instead"
    b "try drawing a picture of me flipping you off"
    $ my_drawing = draw_logic.Draw.main()
    b "LMAO sweet"
    b "ok now say something mean to me"
    $ job = renpy.input("Something Mean?")
    b "wtf dude"
    hide beet
    show expression my_drawing
    b "eat shit pal"
    hide expression my_drawing
    jump beetbye

label beetbye:
    show beet neutral
    b "anyway it was nice meeting you"
    b "yeah and ill probably see you tomorrow"
    b "if youre arent busy with uhh"
    b "[job]"
    hide beet
