"""
Author: Romain Dzeinse
Date: 4/11/4
Objective: I like the idea of doing mini side quests, stuff that sort of happen in games online
"""
true_color_esc_key = "\033[38;2;"
reset = "\033[0m"
invert = "\033[07m"


def intro():
    print("\033[7mWelcome lil \033[0m\033[31mnigga\033[0m\033[7m to an adventure of a lifetime!\033[0m")
    print("Before choosing where you would like to go, let's start with your name.")
    name = input(">>> ")
    color_name = "\033[32m"
    print(f"Where would you like to travel today {color_name}{name}\033[0m:")
    true_color_esc = "\033[38;2;"
    color1 = "120;10;150m"
    color2 = "224;154;108m"
    "\033[38;2;224;154;108m"
    color_code = f"{true_color_esc}{color2}"
    the_reset = "\033[0m"
    countries = [f"{color_code}France{the_reset}-|-", f"{color_code}Germany{the_reset}-|-", f"{color_code}Cameroon{the_reset}-|-",
                 f"{color_code}China{the_reset}-|-", f"{color_code}Nigeria{the_reset}-|-", f"{color_code}Netherland{the_reset}]"]
    for i in countries:
        print(i, end="")
    print()
    # print(f"[{color_code}France{the_reset}-|-{color_code}Germany{the_reset}-|-{color_code}Cameroon{the_reset}-|-"
    #       f"{color_code}China{the_reset}-|-{color_code}Nigeria{the_reset}-|-{color_code}Netherland{the_reset}]")
    destination = input(">>> ")
    destination = destination[0].upper() + destination[1:]
    print(f"On your way to the beautiful cities of {color_code}{destination}{the_reset}, you find yourself lost.")
    print("The good news is, you can choose to move in any direction")
    print("The bad news is..., well, why don't we save that for later")
    print("Before I leave you I'll give you this sword: ⚔️\n it'll probably come in handy given this area")
    print(f"Good luck {color_name}{name}{the_reset}!")
    color_country = color_code
    return name, destination, color_name, color_country


def print_france_map():
    print()
    land_marks = ["* = You're Here", "💀 = Small Monster", "DE = Dead End ", "🦖🦕 = Dino fence", "⚔️⚔️⚔️⚔️ = 4 swords", "☠️ = Big Monster"]
    print("Welcome to France:")
    print("Here are the landmarks you need to remember:")
    the_invert = "\033[07m"
    the_reset = "\033[0m"
    for i in land_marks:
        print("| " + i + " |")
    print()
    the_map = [
        ["     |   |           "],
        [" ____| * |___________"],
        [" |                  |"],
        ["D|                  |"],
        ["E|     💀           |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |"],
        [f" |{the_invert}      ↑       {the_reset}|   |                            * = You're Here "],
        [f" |{the_invert}      |       {the_reset}|   |                            💀 = Small Monster  "],
        [f" |{the_invert}      |       {the_reset}|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|         DE = Dead End  "],
        [f" |{the_invert}   volcano    {the_reset}|   |☠️          ______|         🦖🦕 = Dino fence  "],
        [f" |{the_invert}      |       {the_reset}|   |     |      |               ⚔️⚔️⚔️⚔️ = 4 swords "],
        [f" |{the_invert}      |       {the_reset}|   |     |      |               ☠️ = Big Monster "],
        [" |______↓_______|   |     |      |"],
        [" |⚔️⚔️⚔️⚔️               |¯¯¯|  |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ¯¯¯¯¯|   |  |"],
        [" |🦕🦖🦕🦖🦕🦖🦕        |   |  |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |  exit"],
    ]

    for row in the_map:
        for col in row:
            print(col, end="")
        print()


user_name, user_destination, name_col, destination_col = intro()


def france_part1(u_name, u_des, u_n_color, u_d_color):
    you_died = False
    print(f"On your way to {u_d_color}{u_des}{reset}, you find a dog pound.")
    print("You remember you really really really LOVE dogs.")
    print("In fact when you were younger, your mom adopted a\npack of 10 dogs when you asked her.")
    print("Do you wanna go in? (y/n)")
    have_dog = False
    in_pound = input(">>> ").lower()
    dog_name = ""
    color = "193;224;108m"
    color_dog = f"{true_color_esc_key}{color}"
    if in_pound == "y":
        print("Anyways, you enter the dog pound and find a german shepherd\nfor some protection")
        dog_name = "Lola"
        print(f"The dog's name is {color_dog}{dog_name}{reset}. Do you want {color_dog}{dog_name}{reset} (y/n)")
        want_lola = input(">>> ").lower()
        if want_lola == "y":
            dog_name = "Rocky Balboa"
            have_dog = True
            print(f"You take Lola, and her name to {color_dog}{dog_name}{reset}")
        else:
            print(f"You remember, you don't actually like {color_dog}{dog_name}{reset} so you leave her")
    else:
        print("You remember you always loved dogs, but your mom\nhated them so she never let you have any")

    if have_dog:
        print(f"As you continue on your way to {u_d_color}{u_des}{reset}, a ghoul steals {color_dog}{dog_name}{reset}")
        print("stolen and you begin to cry and then quickly remember, a year ago, David Goggins was your mentor")
        print("so you tell yourself...")
        print("stay hard")
        print("you say again...")
        print("Stay Hard")
        print("then you scream aloud...")
        print("STAY HARD!!! AAAARRRRGGGG!!!😡")
        print(f"You chase him to {u_d_color}{u_des}{reset} and he gets away again")
        print("You see 4 different paths")
    else:
        print(f"As you continue on your way to {u_d_color}{u_des}{reset}, you trip on a rock and and your right big toe"
              f" is now bleeding.")
        print("Conveniently, you see a sign that says, \n\"NO hospitals until Russia\" ")
        print("You continue to your destination with a slight limp on your right foot")
        print(f"you now get to {u_d_color}{u_des}{reset} and you are met with 4 different paths")
    print("backwards/forwards/left/right")
    print("how would you like to proceed? (b/f/l/r)")
    direction = input(">>> ").lower()
    if direction == "b":
        print(f"Are you sure you want to leave {u_d_color}{u_des}{reset}, {u_n_color}{u_name}{reset}? (y/n)")
        leave = input(">>> ").lower()
        if leave == "y":
            if have_dog:
                print(f"You have now left {u_d_color}{u_des}{reset} and given away your protector,"
                      f"{color_dog}{dog_name}{reset}, to the ghoul")
                print(f"Out of sorrow of not avenging {color_dog}{dog_name}{reset}, you cry yourself to death")
                print(), print()
                print("Game Over")
                you_died = True
                return you_died
            else:
                print("Your big toe now becomes infected with the dust and dirt from the road and your toe wound ends"
                      " up getting bugger and nastier. ")
                print("You die.")
                print(), print()
                print("Game Over")
                you_died = True
                return you_died
    elif direction == "f":
        print("You go forward until you get across a water gun")
        print("You pick up the water gun just in case")
        print("You see a lava monster approach you as you walk forward.")
        print("Would you like to fight it (y/n)")
        fight_l_monster = input(">>> ").lower()
        if fight_l_monster == "y":
            print("You use the water gun you picked up earlier and shoot the\nlava monster until he evaporates to death")
            print("Then you find your way though this long hallway looking street and take it.")
            return you_died
        else:
            if have_dog:
                print("You decide to run away from the lava monster but you end up falling in the volcano and die")
                print(), print()
                print("Game Over")
                you_died = True
                return you_died
            else:
                print("You try to limp away from the lava monster but lava monster catches up and hugs you to death")
                print(), print()
                print("Game Over")
                you_died = True
                return you_died
    elif direction == "l":
        print("You take a left and fall in lava")
        print(), print()
        print("Game Over")
        you_died = True
        return you_died
    elif direction == "r":
        print("You take a right into a dead end and out of frustration that you might "
              "get lost forever, you hyper stress for 10 minutes until you "
              "die from overstress and a heart attack")
        print(), print()
        print("Game Over")
        you_died = True
        return you_died
    else:
        print("You decided to do nothing and the ground collapses on itself along with you,"
              " where you meet your doom.")
        print(), print()
        you_died = True
        return you_died


def france_map_after_part1():
    print()
    land_marks = ["* = You're Here", "💀 = Small Monster", "DE = Dead End ", "🦖🦕 = Dino fence", "⚔️⚔️⚔️⚔️ = 4 swords", "☠️ = Big Monster"]
    print("Welcome to France:")
    print("Here are the landmarks you need to remember:")
    invert = "\033[07m"
    the_reset = "\033[0m"
    for i in land_marks:
        print("| " + i + " |")
    print()
    the_map = [
        ["     |   |           "],
        [" ____|   |___________"],
        [" |                  |"],
        ["D|                  |"],
        ["E|                  |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |"],
        [f" |{invert}      ↑       {the_reset}|   |                            * = You're Here "],
        [f" |{invert}      |       {the_reset}|   |                            "],
        [f" |{invert}      |       {the_reset}|   |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|         DE = Dead End  "],
        [f" |{invert}   volcano    {the_reset}|   |☠️          ______|         🦖🦕 = Dino fence  "],
        [f" |{invert}      |       {the_reset}|   |     |      |               ⚔️⚔️⚔️⚔️ = 4 swords "],
        [f" |{invert}      |       {the_reset}|   |     |      |               ☠️ = Big Monster "],
        [" |______↓_______| * |     |      |"],
        [" |⚔️⚔️⚔️⚔️               |¯¯¯|  |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ¯¯¯¯¯|   |  |"],
        [" |🦕🦖🦕🦖🦕🦖🦕        |   |  |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |  exit"],
    ]

    for row in the_map:
        for col in row:
            print(col, end="")
        print()


part1 = france_part1(user_name, user_destination, name_col, destination_col)
if not part1:
    print()
    print("\033[32mCheckpoint 1 complete\033[0m✅")
    the_map = [
        ["     |   |           "],
        [" ____|   |___________"],
        [" |                  |"],
        ["D|                  |"],
        ["E|                  |"],
        [" |¯¯¯¯¯¯¯¯¯¯¯¯¯¯|   |"],
        [f" |{invert}      ↑       {reset}| ↓ |                            \033[7m\033[31m* = You're Here{reset} "],
        [f" |{invert}      |       {reset}| ↓ |                            "],
        [f" |{invert}      |       {reset}| ↓ |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|         DE = Dead End  "],
        [f" |{invert}   volcano    {reset}| ↓ |☠️          ______|         "],
        [f" |{invert}      |       {reset}| ↓ |     |      |               "],
        [f" |{invert}      |       {reset}| ↓ |     |      |               ☠️ = Big Monster "],
        [f" |______↓_______| {invert}\033[31m*{reset} |     |      |"],
    ]

    for row in the_map:
        for col in row:
            print(col, end="")
        print()


def france_part2():
    print("As you explore your surroundings, you find a set of 4 swords ⚔️⚔️⚔️⚔️!")
    print("Do you want to take it? (y/n)")
    take_object = input(">>> ").lower()
    if take_object == "y":
        print("You take the swords and put it in your bag")
    print("Now, you are met with another decision (l/f/b)")


print_france_map()

if __name__ == "__main__":
    print("I really like cheese")

