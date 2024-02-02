SCRIPT_PATH = "game/levels/scripts"


def play_scene(scene):
    with open(f"{SCRIPT_PATH}/{scene}.txt", "r") as script:
        for line in script:
            print(line.rstrip("\n"))
            input()

    script.close()


def get_user_choice(prompt):
    choice = input(prompt)

    while choice == "" or choice.isalpha():
        print("Invalid choice. Try again.")
        choice = input(prompt)

    return choice
