import random


def play_game():
    print("\t\t\t\t\t\t\tWelcome to TIME TO SLAY")
    print()
    return ""


def roll_dice():
    die = [1, 2, 3, 4, 5, 6]
    roll1 = random.choice(die)
    roll2 = random.choice(die)
    print(f"First roll {roll1}\nSecond roll {roll2}")


party_leader_cards = ["\tThe Brutal Bow", "\tCharismatic Song", "\tThe Cloaked Sage", "\tThe Devine Arrow",
                      "\tThe Fearless Flame",
                      "\tThe Fierce Panguardian", "\tThe first Reason", "\tThe Gnawing Dread",
                      "\tThe Illusive Trickster",
                      "\tThe Mystical Maestro", "\tThe Nobel Shaman", "\tThe Piercing Howl",
                      "\tThe Protecting Horn",
                      "\tThe Raging Manticore", "\tThe Shadow Claw", "\tThe Unstable Unicorn",
                      "\tThe Veiled Raider"]


print(play_game())


def print_party_leaders(p_l_cards):
    for i in range(len(party_leader_cards)):
        if i != 0 and i % 5 == 0:
            print()
        else:
            print(f"| {party_leader_cards[i]}", end="\t")
    print("|")


print(print_party_leaders(party_leader_cards))


"____________________________________________________________________________________"


def change_slayed_dragons():
    pass
