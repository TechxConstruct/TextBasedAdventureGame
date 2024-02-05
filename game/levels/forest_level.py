"""
File: forest_level.py

This file represents the forest level of our text based adventure game.
"""
from game.scene_enum import SceneEnum
import game.scene_utils as utils


def the_beginning():
    utils.play_scene(SceneEnum.THE_BEGINNING.value)

    prompt = ("1 > Stare at the sky\n"
              "2 > Get up\n"
              "3 > Listen closely\n"
              "4 > Quit Game(close game)\n")

    choice = utils.get_user_choice(prompt)

    match choice:
        case "1":
            next_scene = SceneEnum.FOREST_STARE_SKY.value
        case "2":
            next_scene = SceneEnum.FOREST_EXPLORER.value
        case "3":
            next_scene = SceneEnum.FOREST_LISTENER.value
        case "4":
            exit(0)
        case _:
            print("Invalid option")
            exit(0)

    return next_scene


def stare_at_sky_scene():
    utils.play_scene(SceneEnum.FOREST_STARE_SKY.value)

    prompt = ("1 > Succumb to the pain\n"
              "2 > Try to block out the pain\n"
              "3 > Quit\n")

    choice = utils.get_user_choice(prompt)

    match choice:
        case "1":
            next_scene = SceneEnum.MOON_HAZE.value
        case "2":
            # maybe do some hidden path
            print("To be continued...")
            next_scene = None
        case "3":
            exit(0)
        case _:
            print("Invalid option")
            exit(0)

    return next_scene
