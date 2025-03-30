"""
Author: Romain Dzeinse
Date: 4/23/24
Objective: Create a program that plays the black jack game with one player
Inspiration: I remembered a friend of mine in High school. I remembered how
we used to play soccer together and how he taught me to play Black Jack.

So, thank you, Brandon Faison, for teaching me BlackJack
"""
import random


def blackjack():
    """
    Takes no variable, just call it, and you get it
    :return: returns the number of times the user played the game,
             the biggest round out of all the times th user played,
             the final sum when the user decided not to play
             again, and then the name of the user

    """
    types_of_people = ["Jack", "Marco", "Romain", "James"]
    print("Who do you want to be (enter name or no)", end="\n|")
    for i in types_of_people:
        print("\033[31m", i, end="\033[0m |")
    to_be = input("\n>>> ")
    if to_be == "no":
        print("Enter your name")
        to_be = input(">>> ")
    play_again = True
    num_times_played = 1
    all_rounds = []
    user_sum = 0
    while play_again:
        round_counter = 1
        user_sum = 0
        while user_sum < 21:
            card1 = ""
            card2 = ""
            if round_counter > 1:
                print()
            print(f"\033[40m++++++++This is round \033[31m{round_counter}\033[0m++++++++\033[0m")
            print("type \033[7mdraw\033[0m when ready to draw your cards")
            print("Card 1")
            draw1 = input(">>> ").lower()
            if draw1 == "draw":
                card1 = random.choice(range(1, 10))
            print(f"you drew, \033[35m{card1}\033[0m")
            print("Card 2")
            draw2 = input(">>> ").lower()
            if draw2 == "draw":
                card2 = random.choice(range(1, 10))
            print(f"you drew, \033[35m{card2}\033[0m")
            user_sum += card1 + card2
            print(f"This is your total: \033[31m{user_sum}\033[0m")
            round_counter += 1

        all_rounds.append(round_counter-1)
        if user_sum == 21:
            print(f"{to_be}, you WON BlackJack!!!")
        else:
            print(f"{to_be}, you lost BlackJack ")
        print("Would you like to play again (y/n):")
        again = input(">>> ").lower()
        if again == "y":
            play_again = True
            print("************************")
            print("*                      *")
            print("*       \033[30mBLACK\033[0m          *")
            print("*        \033[30mJACK\033[0m          *")
            print("*                      *")
            print("************************")
            num_times_played += 1
        else:
            play_again = False
    biggest_round = all_rounds[0]
    for i in range(len(all_rounds)-1):
        if biggest_round < all_rounds[i+1]:
            biggest_round = all_rounds[i+1]
    return num_times_played, biggest_round, user_sum, to_be


if __name__ == "__main__":
    times_played, max_rounds, final_sum_of_user, user_name = blackjack()
    print(f"\033[45m{user_name}\033[0m played \033[45m{times_played}\033[0m games, with a maximum of "
          f"\033[45m{max_rounds}\033[0m rounds, his last total was \033[45m{final_sum_of_user}\033[0m")


