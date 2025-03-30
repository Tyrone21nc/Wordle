"""
Author: Romain Dzeinse
Date: 6/17/24
file: wordSearch.py
Objective: Create a game of Word Search inspired by the game Word Search
"""
import random


"""
Pseudo code:
    - create game function 
        - word_search(set_of_words)
    - have 10 words that match a category and put them in a list
    - words should be a variety ranging from length 3 to length 6
    - grid of word search should be 6X7
        - 6 horizontally and 7 vertically
    - create an empty 2D list of the dimensions
    
    - create a helper function to help you randomly put the words in the 2D list
    - create a helper function to help populate the remaining empty spaces with 
        random letters of the alphabet
    - display the grid with all the letters in regular white colors
    - create a function that will change the highlights of the letters everytime 
        the user guesses a correct word 
        - 10 different colors
    - create a function that prints the grid correctly
    - display the list of the words after every turn
        - if the word is has been guessed, display it
    - everytime the user guesses the wrong word, say try again
    - everytime the user guesses the correct word, display the grid again with  
        the appropriate highlight on the word they guessed correctly
    - the game ends when all the words have been guessed correctly and it has 
        been displayed (highlighted) correctly on the grid
    - ask the user if they would like to play again
        - if yes, loop the game again, if no, end the program
"""


def create_grid(row, col):
    grid = []
    for i in range(col):
        grid.append([])
        for j in range(row):
            grid[i].append("-")
    return grid


def display_grid(grid):
    for i in grid:
        print(end="|")
        for j in i:
            print(j, end="|")
        print()


def apply_words(words, grid):
    random_hor = random.choice(range(1, 4))
    column = random.choice(range(1, 6))
    for i in range(random_hor):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print()
            # if grid[i][j] == "-" and words[i][j]:
            #     grid[i][j] = words[i][j]
            # else:
            #     grid[i] = "-"

    # for i in range(len(grid)):
    #     pass
    return grid


def game(list_of_words):
    print("\033[7m\t\t\tLet's play Word Search\t\t\t\033[0m\n")
    print("\033[7m\t\t\t\t\tRules\t\t\t\t\t\033[0m\nThe rules are simple:\n1. There are 10 words to find\n2. "
          "Find them all and you win a "
          "CA$H💵 prize\n\nIf at any time, you want to stop playing, \njust type 'quit'. "
          "\033[7mGood Luck!!\033[0m\n")
    the_grid = create_grid(6, 7)  # Creates grid and stores it in the my_grid variable
    # display_grid(the_grid)  # displays(prints) the grid
    the_grid = apply_words(list_of_words, the_grid)
    print()
    print()
    display_grid(the_grid)


if __name__ == "__main__":
    # The category is things to do when bored
    words_list = ["chess", "soccer", "code", "uno", "PingPong", "read", "music", "games", "workout", "cook"]
    game(words_list)


