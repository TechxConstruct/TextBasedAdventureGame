from game.path_finder import get_path
from game.scene_enum import SceneEnum

SCRIPT_PATH = "game/levels/scripts"

has_game_ended = False


def start_the_game():
    with open(f"{SCRIPT_PATH}/intro.txt", "r") as script:
        print(script.read())
        print("----------------------------------\n")
    script.close()


if __name__ == "__main__":
    start_the_game()

    next_scene = SceneEnum.THE_BEGINNING.value

    while next_scene is not None:
        next_scene = get_path(next_scene)

    print("Thanks for playing!")
