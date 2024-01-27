import game.path_finder as path_finder

print("Welcome to my text based game called The Forest \n"
      "In this game your objective is simply leave the forest. \n"
      "Of course, it won't be that easy. You'll have to play the game to "
      "find out why.\n"
      "To advance the text on screen press enter.\n"
      "To choose your path going forward, simply enter the selection by the "
      "by the corresponding option.\n"
      "With all that out of the way, good luck and have fun!\n")

has_game_ended = False
choices = ["0:0"]

while not has_game_ended:
    next_path = path_finder.find_path(choices)

    if next_path is None:
        has_game_ended = True

    choices.append(next_path)
    input("Press enter to continue or [q + enter] to quit")

print("Thanks for playing!")
