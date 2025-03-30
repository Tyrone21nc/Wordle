"""
Author: Romain Dzeinse
Date: 04/29/24
Objective: Building the board game Sorry with 4 players and have
"""

"""
Pseudo code:
1. build board for all 4 players

2.Make every player have a turn
    - a turn consists of rolling two dice

3.Check who won and end game
"""
# What the board could look like
"""
          ---------------------------------------------------
          |                                                 |
          |   ____________                   ____________   |
          |   |P1      P1|                   |P2      P2|   |
          |   |   START  |                   |  START   |   |
          |   |P1      P1|                   |P2      P2|   |
          |   |---|  |---|                   |---|  |---|   |
          |   |   |  |   |                   |   |  |   |   |
          |   |   |  |   |                   |   |  |   |   |
          |   |   |  |   |                   |   |  |   |   |
          |   |   ¯¯¯¯   |                   |   ¯¯¯¯   |   |
          |   |    END   |                   |    END   |   |
          |   |----------|                   |----------|   |
          |                                                 |
          |                                                 |
          |   |¯¯¯¯¯¯¯¯¯¯|                   |¯¯¯¯¯¯¯¯¯¯|   |
          |   |    END   |                   |    END   |   |
          |   |   ____   |                   |   ____   |   |
          |   |   |  |   |                   |   |  |   |   |
          |   |   |  |   |                   |   |  |   |   |
          |   |   |  |   |                   |   |  |   |   |
          |   |---|  |---|                   |---|  |---|   |
          |   |P3      P3|                   |P4      P4|   |
          |   |   START  |                   |  START   |   |
          |   |P3      P3|                   |P4      P4|   |
          |   |¯¯¯¯¯¯¯¯¯¯|                   |¯¯¯¯¯¯¯¯¯¯|   |
          |                                                 |
          ---------------------------------------------------
"""

board_reference = [
    ["---------------------------------------------------"],
    ["|                                                 |"],
    ["|   ____________                   ____________   |"],
    ["|   |P1      P1|                   |P2      P2|   |"],
    ["|   |   START  |                   |  START   |   |"],
    ["|   |P1      P1|                   |P2      P2|   |"],
    ["|   |---|  |---|                   |---|  |---|   |"],
    ["|   |   |  |   |                   |   |  |   |   |"],
    ["|   |   |  |   |                   |   |  |   |   |"],
    ["|   |   |  |   |                   |   |  |   |   |"],
    ["|   |   ¯¯¯¯   |                   |   ¯¯¯¯   |   |"],
    ["|   |    END   |                   |    END   |   |"],
    ["|   |----------|                   |----------|   |"],
    ["|                                                 |"],
    ["|                                                 |"],
    ["|   |¯¯¯¯¯¯¯¯¯¯|                   |¯¯¯¯¯¯¯¯¯¯|   |"],
    ["|   |    END   |                   |    END   |   |"],
    ["|   |   ____   |                   |   ____   |   |"],
    ["|   |   |  |   |                   |   |  |   |   |"],
    ["|   |   |  |   |                   |   |  |   |   |"],
    ["|   |   |  |   |                   |   |  |   |   |"],
    ["|   |---|  |---|                   |---|  |---|   |"],
    ["|   |P3      P3|                   |P4      P4|   |"],
    ["|   |   START  |                   |  START   |   |"],
    ["|   |P3      P3|                   |P4      P4|   |"],
    ["|   |¯¯¯¯¯¯¯¯¯¯|                   |¯¯¯¯¯¯¯¯¯¯|   |"],
    ["|                                                 |"],
    ["---------------------------------------------------"]
]


def make_empty_board():
    true_color_esc_key = "\033[38;2;"
    reset = "\033[0m"
    p1color = "57;163;85m"
    combo1 = true_color_esc_key + p1color
    p2color = "56;152;176m"
    combo2 = true_color_esc_key + p2color
    p3color = "184;127;42m"
    combo3 = true_color_esc_key + p3color
    p4color = "204;35;69m"
    combo4 = true_color_esc_key + p4color
    board = [
        [f"---------------------------------------------------"],
        [f"|   |{combo1}→  →  →  → {reset}                  {combo2}  →  →  →  →{reset}|   |"],
        [f"|---{combo1}____________{reset}                   {combo2}____________{reset}---|"],
        [f"|   {combo1}|P1      P1|{reset}                   {combo2}|P2      P2|{reset}   |"],
        [f"|---{combo1}|   START  |{reset}                   {combo2}|  START   |{reset}---|"],
        [f"|   {combo1}|P1      P1|{reset}                   {combo2}|P2      P2|{reset}   |"],
        [f"|---{combo1}|---|  |---|{reset}                   {combo2}|---|  |---|{reset}---|"],
        [f"|   {combo1}|   |  |   |{reset}                   {combo2}|   |  |   |{reset}   |"],
        [f"|---{combo1}|   |  |   |{reset}                   {combo2}|   |  |   |{reset}---|"],
        [f"|   {combo1}|   |  |   |{reset}                   {combo2}|   |  |   |{reset}   |"],
        [f"|---{combo1}|   ¯¯¯¯   |{reset}                   {combo2}|   ¯¯¯¯   |{reset}---|"],
        [f"|   {combo1}|    END   |{reset}                   {combo2}|    END   |{reset}   |"],
        [f"|---{combo1}|----------|{reset}                   {combo2}|----------|{reset}---|"],
        [f"|   |                                         |   |"],
        [f"|---|                                         |---|"],
        [f"|   {combo3}|¯¯¯¯¯¯¯¯¯¯|{reset}                   {combo4}|¯¯¯¯¯¯¯¯¯¯|{reset}   |"],
        [f"|---{combo3}|    END   |{reset}                   {combo4}|    END   |{reset}---|"],
        [f"|   {combo3}|   ____   |{reset}                   {combo4}|   ____   |{reset}   |"],
        [f"|---{combo3}|   |  |   |{reset}                   {combo4}|   |  |   |{reset}---|"],
        [f"|   {combo3}|   |  |   |{reset}                   {combo4}|   |  |   |{reset}   |"],
        [f"|---{combo3}|   |  |   |{reset}                   {combo4}|   |  |   |{reset}---|"],
        [f"|   {combo3}|---|  |---|{reset}                   {combo4}|---|  |---|{reset}   |"],
        [f"|---{combo3}|P3      P3|{reset}                   {combo4}|P4      P4|{reset}---|"],
        [f"|   {combo3}|   START  |{reset}                   {combo4}|  START   |{reset}   |"],
        [f"|---{combo3}|P3      P3|{reset}                   {combo4}|P4      P4|{reset}---|"],
        [f"|   {combo3}|¯¯¯¯¯¯¯¯¯¯|{reset}                   {combo4}|¯¯¯¯¯¯¯¯¯¯|{reset}   |"],
        [f"|---|{combo3}←  ←  ←  ← {reset} |  |  |  |  |  | {combo4}  ←  ←  ←  ←{reset}|---|"],
        [f"---------------------------------------------------"]
    ]
    return board


def print_empty_board(original_board):
    for i in range(len(original_board)):
        for j in range(len(original_board[i])):
            print("\t\t\t\t\t\t\t", original_board[i][j], end="")
        print()


def introduction():
    print("Welcome to the game of Sorry, a long tiring game \nof dice rolls and stuff.")
    print("Play the game and remember to have some fun.")


def play_game():
    introduction()
    # num_of_players = int(input("How many people are playing this game? "))
    board_values = make_empty_board()
    print_empty_board(board_values)


if __name__ == "__main__":
    # print(board_values[1])
    play_game()

