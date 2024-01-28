"""
File: ForestLevel.py

This file represents the forest level of our text based adventure game.
"""
from game.scene_enum import SceneEnum

SCRIPT_PATH = "game/levels/scripts"


def the_beginning():
    with open(f"{SCRIPT_PATH}/{SceneEnum.THE_BEGINNING.value}.txt", "r") as script:
        for line in script:
            print(line.rstrip("\n"))
            input()

    script.close()

    prompt = "1 > Stare at the sky\n2 > Get up\n3 > Listen closely\n4 > Quit Game(close game)\n"
    choice = input(prompt)

    while choice == "" or choice.isalpha():
        print("invalid option detected")
        choice = input(prompt)

    next_scene = None

    if choice == "1":
        next_scene = SceneEnum.FOREST_STARE_SKY.value
    if choice == "2":
        next_scene = SceneEnum.FOREST_EXPLORER.value
    if choice == "3":
        next_scene = SceneEnum.FOREST_LISTENER.value
    if choice == "4":
        exit(0)

    return next_scene


def stare_at_sky_scene():
    with open(f"{SCRIPT_PATH}/{SceneEnum.FOREST_STARE_SKY.value}.txt", "r") as script:
        for line in script:
            print(line.rstrip("\n"))
            input("")

    script.close()

    prompt = "1 > Succumb to the pain\n"\
             "2 > Try to block out the pain\n"\
             "3 > Quit\n"

    choice = input(prompt)
    while choice == "" or choice.isalpha():
        print("invalid option detected")
        choice = input(prompt)

    next_scene = None

    if choice == "1":
        next_scene = SceneEnum.MOON_HAZE.value
    elif choice == "2":
        # maybe do some hidden path
        pass
    else:
        exit(0)

    return next_scene
