"""
File: ForestLevel.py

This file represents the forest level of our text based adventure game.
"""

import keyboard


def the_beginning():
    text_list = [
        "You awaken lying on the ground.",
        "It's soft.",
        "Your mind feels hazy",
        "You find it hard to concentrate on any particular thought.",
        "Your vision is slow to adjust, but you make out the scene before you.",
        "Your eyes adjust to see the full moon and the stars.",
        "Your mind is clearing up now.",
        "The moon looks closer than it should.",
        "The glow of the moon isn't quite right either.",
        "You look around and notice you're in a forest clearing",
        "The forest doesn't look familiar.",
        "It's quiet."
    ]
    # print("You awaken lying on the ground.\n"
    #       "It's soft.\n"
    #       "Your mind feels hazy\n"
    #       "You find it hard to concentrate on any particular thought.\n"
    #       "Your vision is slow to adjust, but you make out the scene before you.\n"
    #       "Your eyes adjust to see the full moon and the stars.\n"
    #       "Your mind is clearing up now.\n"
    #       "The moon looks closer than it should.\n"
    #       "The glow of the moon isn't quite right either.\n"
    #       "You look around you to notice your in a clearing in the forest.\n"
    #       "They don't look familiar.\n"
    #       "It's quiet.\n"
    #       )

    for text in text_list:
        print(text)
        input("")

    choice = input("1 > Stare at the sky\n2 > Get up\n3 > Listen closely\n4 > Quit Game(close game)\n")

    if choice == "4":
        exit(0)

    return choice


