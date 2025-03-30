"""
Name: Romain Donfack Dzeinse
Date: 02/06/24
Objective: Well you already know I like wordle,
I am just adding wordle with a twist on it
"""
red = "\033[31m"
yellow_orange = "\033[33m"
green = "\033[32m"
end = "\033[0m"


def all_words():
    the_words = [
        [" ", "X", " ", "X", " "],
        ["X", "X", "X", "X", "X"],
        [" ", "X", " ", "X", " "],
        ["X", "X", "X", "X", "X"],
        [" ", "X", " ", "X", " "],
    ]
    return the_words


def actual_words():
    c_words = [
            [" ", "M", " ", "O", " "],
            ["B", "O", "M", "B", "S"],
            [" ", "N", " ", "X", " "],
            ["P", "E", "N", "I", "S"],
            [" ", "Y", " ", "N", " "]]
    return c_words


def print_board(board, color):
    for i in range(len(board)):
        print("                ", end="")
        for j in range(len(board[i])):
            if i % 2 == 0 and j % 2 == 0:
                print(f" {board[i][j]} ", end="")
            else:
                print(f"|{color}{board[i][j]}{end}|", end="")
        print()


def valid_word(the_word):
    if the_word.isalpha():
        return True
    else:
        return False


def change_places(board, correct_board, the_word):
    # This is assuming that the given word by the user is length 5
    for i in range(len(correct_board)):
        for j in range(len(correct_board[i])):
            for k in range(len(correct_board[i])):
                # print(f"{the_word[j]} == {correct_board[i][k]}")
                if the_word[j] == correct_board[i][k]:
                    board[i][k] = f"{correct_board[i][k]}"

    def printing_changed_board():
        for i in range(len(board)):
            print("                ", end="")
            for j in range(len(board[i])):
                if board[i][j] == correct_board[i][j]:
                    if i % 2 == 0:
                        if board[i][j] == " ":
                            print(f" {board[i][j]} ", end="")
                        else:
                            print(f"|{green}{board[i][j]}{end}|", end="")
                    else:
                        print(f"|{green}{board[i][j]}{end}|", end="")
                else:
                    print(f"|{red}{board[i][j]}{end}|", end="")
            print()

    printing_changed_board()

    return board


def win_or_not(board, correct_board):
    correct_length = 0
    for i in correct_board:
        correct_length += len(i)
    length = 0
    for i in range(len(correct_board)):
        for j in range(len(correct_board[i])):
            if correct_board[i][j] == board[i][j]:
                length += 1
    if correct_length == length:
        return True


def intro():
    print("        Let's play WORDLE with a twist sort off")
    print()
    print("                Rules")
    rules = [
        "\033[32mGreen\033[0m means in word and in\033[32m correct place\033[0m",
        "\033[31mRed\033[0m means either\033[31m placeholder\033[0m or\033[31m not in word\033[0m"
    ]
    for i in range(len(rules)):
        print(f"{i + 1}: {rules[i]}")
    print()


def play_game(word_set):
    intro()
    print_board(word_set, red)
    print()
    word_guessed = False
    tries = 0
    while tries < 6 and not word_guessed:
        print()
        print("Guess a word or a word")
        word = input(">>> ").upper()
        # create a function that checks if the word is valid
        #      - meaning it is not a special character or a number
        # the function can return a boolean value
        good_word = valid_word(word)
        # Now we check if the good word returned True, if it did, then we
        # have to check if the word is in the set of words
        if good_word:
            word_set = change_places(word_set, actual_words(), word)
        winning = win_or_not(word_set, actual_words())
        if winning:
            word_guessed = True
        tries += 1
    return [word_guessed, tries]


def wordle():
    result = play_game(all_words())
    if result[0]:
        print()
        print(f"🎉You Won🎉 in {result[1]} tries")
    else:
        print("Game Over")


if __name__ == "__main__":
    wordle()
    print("Would you like to play again (y/n): ")
    play_again = input(">>> ").lower()
    while play_again == "y":
        print()
        print()
        wordle()
