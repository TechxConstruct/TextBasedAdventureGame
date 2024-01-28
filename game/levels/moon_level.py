"""
File: forest_level.py

This file represents the moon level of our text based adventure game.
"""

from game.scene_enum import SceneEnum

SCRIPT_PATH = "game/levels/scripts"


def the_haze():
    with open(f"{SCRIPT_PATH}/{SceneEnum.MOON_HAZE.value}.txt") as script:
        for line in script:
            print(f"> {line}")
            input("")