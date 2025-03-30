"""
Author: Romain Donfack Dzeinse
Date: 1/20/24
Objective: Build a Wordscape type game
Inspiration: I play Wordscape on my phone and I like it
"""
import random

print("\t\t\t\t\tWelcome to WORDSCAPES")
print("Directions: ")
max_screen = 60  # The maximum length of a sentence across the screen can only be 60 characters
directions = "Win the game by guessing all the words with the associated letters salt and pepper"
if len(directions) > max_screen:
    print(directions[:max_screen-1] + "-")
    print(directions[max_screen-1: (max_screen*2)-1])
print("Words used here are from www.wordunscrambler.net/")
check_word = {
    "smoart": ["art", "smart", "mart", "sat", "rat", "start"]
}
word = random.choice(check_word["smoart"])

confirm_words_from_dict = 0


def draw_board(words_dict):
    # Drawing board
    count = 0
    for i in words_dict:
        for j in range(len(words_dict[i])):
            if count < len(check_word[i]):
                if letter_in_word == words_dict[i][count]:
                    print("——————")
                    print("| " + words_dict[i][j] + " |🟢")
                    print("——————")
                    print()
            count += 1


def final_draw_board(words_dict):
    # Drawing final board
    print("Below is the list of all possible words with the letters")
    for i in words_dict:
        for j in range(len(words_dict[i])):
            print("———")
            print("|" + words_dict[i][j] + "|🟢")
            print("———")
            print()












letter_in_word = []
print("Your letters are:\t\t", end="")
for i in range(len(word)):
    print(word[i], end="\t")
print()
letter = input("Give me a word with these letters: ")
for i in range(len(letter)):  #4
    for j in range(len(word)):  #6
        if i in range(len(word)):  #6
            if letter[i] == word[j]:
                # Allowing duplicate letters
                # To remove duplicates, do:
                # if letter[i] not in letter_in_word:
                #    then append it
                letter_in_word.append(letter[i])
letter_in_word = "".join(letter_in_word)  # Changing it to a string
################### The while toop to play the Game











while (letter == letter_in_word) and (letter_in_word in check_word[word]) and confirm_words_from_dict < len(check_word[word])-1:
    # You have a bug here - Go through line for line again to make sure
    # you don't allow user to do duplicate words
    # From after the last single line comments to right before the
    # else of this while loop
    draw_board(check_word)
    confirm_words_from_dict += 1
    letter_in_word = []
    letter = input("Give me a word with these letters: ")
    for i in range(len(letter)):  # 4
        for j in range(len(word)):  # 6
            if i in range(len(word)):  # 6
                if letter[i] == word[j]:
                    # Allowing duplicate letters
                    # To remove duplicates, do:
                    # if letter[i] not in letter_in_word:
                    #    then append it
                    letter_in_word.append(letter[i])
    if letter in letter_in_word:
        # This checks if there is a duplicate word
        print("Duplicate word. Try again")
        letter_in_word = []
        letter = input("Give me a word with these letters: ")
        for i in range(len(letter)):  # 4
            for j in range(len(word)):  # 6
                if i in range(len(word)):  # 6
                    if letter[i] == word[j]:
                        # Allowing duplicate letters
                        # To remove duplicates, do:
                        # if letter[i] not in letter_in_word:
                        #    then append it
                        if letter[i] not in letter_in_word:
                            letter_in_word.append(letter[i])

    letter_in_word = "".join(letter_in_word)  # Changing it to a string
else:
    if confirm_words_from_dict == len(check_word[word])-1:
        draw_board(check_word)
        print("You won the game")
    else:
        print("Make sure you use nothing but the given letters.")






















# while letter_in_word in all_words["smoart"]:  # find a way to check for all the words in the key "smoart"
#     print(letter_in_word)
#     letter_in_word = []
#     letter = input("Give me a word with these letters: ")
#     for i in range(len(letter)):  # 4
#         for j in range(len(word)):  # 4
#             if i in range(len(word)):  # 6
#                 if letter[i] == word[j]:
#                     # Allowing duplicate letters
#                     # To remove duplicates, do:
#                     # if letter[i] not in letter_in_word:
#                     #    then append it
#                     letter_in_word.append(letter[i])
#     letter_in_word = "".join(letter_in_word)  # Changing it to a string
# else:
#     print("Use the given letters in your word.")
#     print("Final Answer")
#     def final_draw_board(words_dict):
#         # Drawing board
#         for i in words_dict:
#             for j in range(len(words_dict[i])):
#                     print("———")
#                     print("|" + words_dict[i][j] + "|🟢")
#                     print("———")
#                     print()



