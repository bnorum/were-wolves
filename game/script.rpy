init python:
    def regblip(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/blip1.mp3", channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.play("audio/blip1.mp3", channel="sound", loop=False)


# Declare characters

define g = Character("guy", callback = regblip)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guy smile
    # These display lines of dialogue.

    g "You've created a new Ren'Py game."

    g "Once you add a story, pictures, and music, you can release it to the world!"

    g "Once you add a story, pictures, and music, you can release it to the world!"

    g "Once you add a story, pictures, and music, you can release it to the world!"

    g "You've created a new Ren'Py game."

    # This ends the game.

    return
