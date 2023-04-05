init python:
    config.nearest_neighbor = True
    def regblip(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/blip1.mp3", channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.play("audio/blip1.mp3", channel="sound", loop=False)


# Declare characters

define g = Character("Jean", callback = regblip)


# The game starts here.

label start:

    scene bg room

    show jean smile

    g "soo... youre pretty weird huh"

    menu:

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

    # This ends the game.

    return
