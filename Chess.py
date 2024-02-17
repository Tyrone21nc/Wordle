"""
Author: Romain Donfack Dzeinse
Date: 1/21/24
Objective: Try your very best to build a chess board and game
Inspiration: I enjoy playing chess with friends and thinking intensely about every move
"""

print("\tLets play Chess")
print()


def board():
    black_pawns = "▪️"
    black_rook = "🔳"
    black_king = "🫅🏿"
    black_bishop = "⚫"
    black_queen = "🖤"
    black_knight = "🏴"

    white_pawns = "▫️"
    white_rook = "🔲"
    white_king = "🫅🏻"
    white_bishop = "⚪"
    white_queen = "🤍"
    white_knight = "🏳️"

    num_of_pawns = 8
    num_of_rooks = 2
    num_of_bishops = 2
    num_of_knights = 2
    num_of_queen = 1
    num_of_king = 1

    letters = "ABCDEFGH"
    print("\t", end="")
    for i in range(len(letters)):
        print(letters[i], end="  ")
    print()
    my_board = [list(white_rook+white_bishop+white_knight+white_queen+white_king+white_knight+white_bishop+white_rook),
                list(white_pawns*num_of_pawns),
                list("❔" * num_of_pawns),
                list("❔" * num_of_pawns),
                list("❔" * num_of_pawns),
                list("❔" * num_of_pawns),
                list(black_pawns*num_of_pawns),
                list(black_rook+black_bishop+black_knight+black_queen+black_king+black_knight+black_bishop+black_rook)]
    for i in range(len(my_board)):
        print(i+1, end="")
        print("\t", end="")
        for j in range(len(my_board[i])):
            print(my_board[i][j], end="")
        print()

    print("\t", end="")
    for i in letters:
        print(i, end="  ")
    print()

    which_piece = input("Which pieces would you like to move (num num): ")
    which_piece.split()
    row = int(which_piece[0])
    col = int(which_piece[1])
    place = " "
    for i in range(len(my_board)):
        for j in range(len(my_board[i])):
            if row == i:
                if col == j:
                    place = str(my_board[i][j])
    print(place)
    # character = my_board[row]
    my_board[row][place] = 2
    print("cheese")
    letter = int(input("Where would you like to move (letter): "))
    number = int(input("Where would you like to move (number): "))
    # my_board[letter][number] =


board()

board()































