"""
File: forest_level.py

This file represents the moon level of our text based adventure game.
"""

from game.scene_enum import SceneEnum

SCRIPT_PATH = "game/levels/scripts"


def the_haze():
    with open(f"{SCRIPT_PATH}/{SceneEnum.MOON_HAZE.value}.txt") as script:
        for line in script:
            print(line.rstrip("\n"))
            input("")

    script.close()

    prompt = ("1 > Run\n"
              "2 > Wait for the figures arrival\n"
              "3 > Quit Game\n")

    choice = input(prompt)

    while choice == "" or choice.isalpha():
        print("Invalid choice. Try again.")
        choice = input(prompt)

    next_scene = None

    if choice == "1":
        next_scene = SceneEnum
    elif choice == "2":
        print("To be continued")
    elif choice == "3":
        exit(0)

    return next_scene

def the_cave():
    with open(f"{SCRIPT_PATH}/{SceneEnum.MOON_THE_CAVE}.txt") as script:
        for line in script:
            print(line.rstrip("\n"))
            input("")

    script.close()

    next_scene = None

    return next_scene