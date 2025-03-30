"""
File: length_converter.py
Author: Romain Donfack Dzeinse
objective: So you can say you are ... centimeters tall if someone asks instead of saying it in feet, like you're weird
"""
import random


def play_game():
    print("\t\t\t\t\t\t\tWelcome to TIME TO SLAY")
    print()
    def roll_dice():
        die = [1, 2, 3, 4, 5, 6]
        roll1 = random.choice(die)
        roll2 = random.choice(die)
        print(f"First roll {roll1}\nSecond roll {roll2}")
    party_leader_cards = ["\tThe Brutal Bow", "\tCharismatic Song", "\tThe Cloaked Sage", "\tThe Devine Arrow",
                          "\tThe Fearless Flame",
                          "\tThe Fierce Panguardian", "\tThe first Reason", "\tThe Gnawing Dread",
                          "\tThe Illusive Trickster",
                          "\tThe Mystical Maestro", "\tThe Nobel Shaman", "\tThe Piercing Howl", "\tThe Protecting Horn",
                          "\tThe Raging Manticore", "\tThe Shadow Claw", "\tThe Unstable Unicorn", "\tThe Veiled Raider"]

    def print_party_leaders(p_l_cards):
        for i in range(len(party_leader_cards)):
            if i != 0 and i % 5 == 0:
                print()
            else:
                print(f"| {party_leader_cards[i]}", end="\t")
        print("|")

    print_party_leaders(party_leader_cards)
    # Format this correctly later
    playerX_deck = [
           ["-----------------------------------"],
           ["|Player:X |                      |"],
           ["|          |                      |"],
           ["|¯¯¯¯¯¯¯¯¯¯¯                      |"],
           ["|                                 |"],
           ["|       ___________________       |"],
           ["|       |Dragons Slayed:0 |       |"],
           ["¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"]]

    def print_empty_board(player_x):
        for i in range(len(player_x)):
            for j in range(len(player_x[i])):
                if i == 0 or i == 7:
                    print(f"  {player_x[i][j]}")
                else:
                    print(f"{i - 1} {player_x[i][j]}")

    # Below I try to access the play of the colon in the 2d list
    place = 0
    num_list = 0
    other_num_list = 0
    for i in range(len(playerX_deck)):
        for j in range((len(playerX_deck[i]))):
            for k in range(len(playerX_deck[i][j])):
                if playerX_deck[i][j][k] == ":":
                    place = k
                    num_list = i
                    other_num_list = j
                    # print(k)

    # print(f"index of ':' in board is {place} in the {num_list}th list")
    # I've got to convert it to a list first before changing its 24th index value
    to_list = playerX_deck[6]
    # playerX_deck[num_list][other_num_list][num_list+1] = "3"

    for i in range(4):
        the_player = input(f"Who wants to be player{i+1} (enter initials): ")
        something = playerX_deck[1][0]
        something.strip("")
        X = something.replace("X", the_player)
        playerX_deck[1].append(X)
        playerX_deck[1].pop(0)
        print_empty_board(playerX_deck)


play_game()








