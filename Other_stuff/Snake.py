"""
Name: Romain Dzeinse
Date 2/1/24 Black History Month
Objective: Build a snake game like the one online
"""
piece = "🐍"
row = 10
col = 15
board = []


def the_board(the_row, the_col):
    place_snake = input("Where do you want to place the 🐍 : ")
    print("—" * the_col)
    for i in range(the_row):
        for j in range(the_col):
            if j == 0 or j == the_col - 1:
                print("|", end="")
            else:
                print(" ", end="")
        print()
    print("—" * the_col)


the_board(row, col)
print()
my_board = [["—" * col], ["|             |"],
            [f"|{piece}           |"],
            ["|             |"],
            ["|             |"],
            ["|             |"],
            ["|       🍅    |"],
            ["|             |"],
            ["|             |"],
            ["|             |"],
            ["|             |"], ["—" * col]]
print()
for i in range(len(my_board)):
    for j in range(len(my_board[i])):
        print(my_board[i][j], end="")
        print(f"\ti: {i}\tj: {j}", end="")
        print()
