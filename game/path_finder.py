# import levels.forest_level as forest_level
# import levels.moon_level as moon_level
from game.levels import forest_level


def find_path(choices: [str]):
    last_index = len(choices) - 1
    last_choice = choices[last_index]

    if last_choice == "0:0":
        path = forest_level.the_beginning()
        return f"0:{path}"
    # if last_choice is "0:1":

