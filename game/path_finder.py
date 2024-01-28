from game.levels import forest_level
from game.levels import moon_level
from game.scene_enum import SceneEnum


def get_path(next_scene: str):

    if next_scene == SceneEnum.THE_BEGINNING.value:
        return forest_level.the_beginning()

    if next_scene == SceneEnum.FOREST_STARE_SKY.value:
        return forest_level.stare_at_sky_scene()

    if next_scene == SceneEnum.MOON_HAZE.value:
        return moon_level.the_haze()
