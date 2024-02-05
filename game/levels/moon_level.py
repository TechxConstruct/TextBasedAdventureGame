"""
File: moon_level.py

This file represents the moon level of our text based adventure game.
"""

from game.scene_enum import SceneEnum
import game.scene_utils as utils


def the_haze():
    utils.play_scene(SceneEnum.MOON_HAZE.value)

    prompt = ("1 > Run\n"
              "2 > Wait for the figures arrival\n"
              "3 > Quit Game\n")

    choice = utils.get_user_choice(prompt)

    match choice:
        case "1":
            print("To be continued")
            next_scene = None
        case "2":
            print("To be continued")
            next_scene = None
        case "3":
            exit(0)
        case _:
            print("Invalid option")
            exit(0)

    return next_scene


def the_cave():
    utils.play_scene(SceneEnum.MOON_THE_CAVE.value)

    next_scene = None

    return next_scene
