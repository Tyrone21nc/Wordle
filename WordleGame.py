"""
Author: Romain Donfack Dzeisne
Date: 1/19/24 about 8pm
Finished on 1/20/24 1:03 am
Objective: Build a Wordle Game
"""
import random
import time
# This will contain 5-letter words
my_words = {1: "ARISE", 2: "ADIEU", 3: "AUDIO", 4: "SLATE", 5: "CRANE",
            6: "RAISE", 7: "TRACE", 8: "SHARE", 9: "SOOTY", 10: "STARE",
}
num = random.choice(list(my_words.keys()))
random_word = my_words[num]

print("  Welcome to Wordle!")
time.sleep(1)
empty = "     "
original_times = 0
"""
Printing the original board
"""

# Prints the board 6 original times
for j in range(19):
    if j == 0:
        print(" -—", end="")
    else:
        print("—", end="")
print("-")
for i in range(5):
    # print("——", end="")
    print(" |", empty.upper()[i], end="")
print(" |")
for j in range(19):
    if j == 0:
        print(" -—", end="")
    else:
        print("—", end="")
print("-")
# Below is the code to make the show the empty sides of the original board
gray = "🩶"
print(" ", end="")
for m in range(5):
    print("|", end="")
    if empty[m]:
        print(gray, end="")
    print("|", end="")
print()
time.sleep(1)
print("\tDirections:")
for i in range(6):
    if i == 0:
        print(str(i+1) + ": To win you must guess the\t\t" + str(i+1+1) + ": "
                         "You have 6 tries")
    elif i == 1:
        print("   correct word\t\t\t\t\t")
    elif i == 2:
        print(str(i+1) + ": Must guess a 5 letter", end="\t\t\t")
    elif i == 3:
        print(str(i+1) + ": Learn a new word")
    elif i == 4:
        print(str(i+1) + ": You have 2 minutes to get" + "\t\t" + str(i+1+1) + ": 🟢 = letter in the correct place\n"
                         "   the word right starting as" + "\t\t" + "   🟠 = letter in word but not in correct place\n"
                         "   soon as you guess your i" + "\t\t   🔴 = letter not in word\n"
                         "   word" + "\t\t\t\t\t\t\t\t   🩶 = blank space")
green = "🟢"
orange = "🟠"
red = "🔴"

print(), print()
attempt = input("    Guess the word: ").upper()
###############################
"""
the time_limit variable gives the user 2 minutes to get the word correct
start_time is the variable that keeps track of the 
current time (not the time being 11:10pm, not that type of time)
"""
time_limit = 120
start_time = time.time()
a_third_of_limit = time_limit//3
"""
Playing the game
"""
tries = 1
word = "bread".upper()
correct_letters = 0
###############################
"""Find a way to make the attempt into list like this ["w","h","a","t"]
then append the remaining number of blanks at the end of it:  len(word) - len(attempt)
 --> 5-4 = 1; Add only one space at the end of the word ["w","h","a","t"," "]
                        OR if attempt were "ten"
attempt = "ten"  ->  len(word) - len(attempt) = 5-3=2;
attempt before spaces ["t","e","n"]
attempt after spaces ["t","e","n"," "," "]
find a way to convert it back to a string
"""
if len(attempt) < 5:
    attempt = list(attempt)
    for n in range(len(random_word) - len(attempt)):
        attempt.append(" ")
    attempt = "".join(attempt)
"""
Commented code above is for adding blacks at the end of the attempt if its not length 5
"""
# The for loop below is to print all the correct letters in the word
for letter in range(5):
    if attempt[letter] in random_word:
        correct_letters += 1
print(correct_letters, "letters are in the correct word!")

while tries <= 5 and attempt != random_word and (time.time() - start_time < time_limit):
        """
    To assist the player with the attempts, I will include hints including:
    - Number of letters they have correct --> DONE (correct_letters is the variable that makes this change)
    - Maybe even telling them if the position of the letters are correct or not 
        --> DONE (with the green, yellow and red variables)
    - Adding spaces for when they enter a word with the length less than 5 
        --> DONE (check where I made attempt a list and used the .join() keyword on it)
        """
        for j in range(19):
            if j == 0:
                print(" -—", end="")
            else:
                print("—", end="")
        print("-")
        for i in range(5):
            # print("——", end="")
            print(" |", attempt[i], end="")
        print(" |")
        for j in range(19):
            if j == 0:
                print(" -—", end="")
            else:
                print("—", end="")
        print("-")
        print(" ", end="")
        for i in range(5):
            print("|", end="")
            if attempt[i] in random_word:
                if attempt[i] == random_word[i]:
                    print(green, end="")
                else:
                    print(orange, end="")
            else:
                print(red, end="")
            print("|", end="")
        print()
        # print("  Attempt number:", tries + 1)
        if a_third_of_limit <= time.time()-start_time <= time_limit:
            print("You only have", time_limit - int(time.time() - start_time), "seconds left!")
            print("And counting...")
        print()
        attempt = input("    Guess the word: ").upper()
        # This below is to make sure there's no error when user enters a non-5-letter word
        if len(attempt) < 5:
            attempt = list(attempt)
            for n in range(len(random_word) - len(attempt)):
                attempt.append(" ")
            attempt = "".join(attempt)
        # This above is to make sure there's no error when user enters a non-5-letter word

        # Correct Letters is the number of letters from the attempt that are in the correct word
        correct_letters = 0
        for letter in range(5):
            if attempt[letter] in random_word:
                correct_letters += 1
        print(correct_letters, "letters are in the correct word!")
        tries += 1

else:
    print("\nYour Guess:")

    # This below is to make sure there's no error when user enters a non-5-letter word
    if len(attempt) < 5:
        attempt = list(attempt)
        for n in range(len(random_word) - len(attempt)):
            attempt.append(" ")
        attempt = "".join(attempt)
    # This above is to make sure there's no error when user enters a non-5-letter word

    # This below is what the user guessed
    for j in range(19):
        if j == 0:
            print(" -—", end="")
        else:
            print("—", end="")
    print("-")
    for i in range(5):
        # print("——", end="")
        print(" |", attempt.upper()[i], end="")
    print(" |")
    for j in range(19):
        if j == 0:
            print(" -—", end="")
        else:
            print("—", end="")
    print("-")
    # Print the colors
    print(" ", end="")
    for i in range(5):
        print("|", end="")
        if attempt[i] in random_word:
            if attempt[i] == random_word[i]:
                print(green, end="")
            else:
                print(orange, end="")
        else:
            print(red, end="")
        print("|", end="")
    print()

    print("The correct word: ")
    # This below is the correct answer
    for j in range(19):
        if j == 0:
            print(" -—", end="")
        else:
            print("—", end="")
    print("-")
    for i in range(5):
        # print("——", end="")
        print(" |", random_word[i], end="")
    print(" |")
    for j in range(19):
        if j == 0:
            print(" -—", end="")
        else:
            print("—", end="")
    print("-")
    # Below will print if user got the Wordle or not
    if int(time.time() - start_time) >= time_limit:
        print("Game Over: You ran out of time")
        print("You ended in:", int(time.time() - start_time), "seconds")
        print("You had: " + str(time_limit) + " seconds (2 minutes)")
    else:
        if random_word == attempt.upper():
            print("😀😀😀😀 Wordle in", tries, "😀😀😀😀")
            print("Good shit lil nigga!👨🏿‍🦱")
            print("You finished in:", int(time.time() - start_time), "seconds")
        else:
            print("You lost Wordle 😤😤😤")
            print("I'd be mad too if I were you")
            print("You ended in:", int(time.time() - start_time), "seconds")
"I am making a change"
