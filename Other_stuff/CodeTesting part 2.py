import random
import time

"""
length = 5
feet = "on"
print(feet)
feet = list(feet)
print(feet)

for i in range(length - len(feet)):
feet.append(" ")

print(feet)
feet = "".join(feet)
print(feet)
print(), print()
"""
######################
"""
# random was imported at the top of page
my_dict = {}

for i in range(1, 11):
my_dict[i] = chr(ord('A') + i - 1)

random_key = random.choice(list(my_dict.keys()))
print((list(my_dict.keys())))
print(random_key)
random_value = my_dict[random_key]

print(f"Randomly selected key: {random_key}")
print(f"Corresponding value: {random_value}")
print(), print()
"""
#######################
"""
print("chess")
# time.sleep(3) waits 3 seconds before doing the part down
time.sleep(2)
print("We waited for 3 secs")
print(), print()
"""
#######################
"""
# Set the time limit in seconds
time_limit = 5  # Change this to the desired time limit

# Get the start time
start_time = time.time()

# Your code or operation
print("Start of operation")

# time.time() - start_time: This calculates the elapsed time
# since the start of the loop. time.time() returns the current
# time in seconds, and start_time is the time when the loop started.
# < time_limit: This checks whether the elapsed time is less than
# the specified time_limit.

while time.time() - start_time < time_limit and False:
    # Your code here
    print(start_time)
    print(time.time())
    print(int(time.time() - start_time))
    time.sleep(1)
    print("Counting:", int(time.time() - start_time), "seconds")

# Continue with your code after reaching the time limit
print("End of operation")
print(), print()
t_limit = 30  # 120 for 2 minutes
start = time.time()
print()
print("start playing: game")
while time.time() - start < t_limit:
    like = input("What do you like to do: ")
    print("So you like to", like, "huh?!")
    print()
    if 20 <= time.time() - start <= t_limit:
        print("Hurry up only", t_limit - int(time.time() - start), "seconds left")
"""
#######################
"""
word = "abdcis"
letter = input("Enter a word: ")
letter_in_word = []
for i in range(len(letter)):  #4
    for j in range(len(word)):  #4
        if i in range(len(word)):  #6
            # print("Lengths: i+1->", i+1, len(word))
            if letter[i] == word[j]:
                # Allowing duplicate letters
                letter_in_word.append(letter[i])
print()
# for i in range(len(letter_in_word)):
#     print(letter_in_word[i], end=" ")
letter_in_word = "".join(letter_in_word)
# print(letter_in_word, type(letter_in_word))
all_words = {
    "abdcis": ["bad", "dib", "dab", "bid", "sad"],
}
# Drawing board
count_special_char = 0
for j in all_words:
    for i in range(len(all_words[j])):  # 5
        if count_special_char < len(all_words[j]):  # 5
            if letter_in_word == all_words[j][count_special_char]:
                print("——————")
                print("| " + all_words[j][count_special_char] + " |🟢")
                print("——————")
                print()
        count_special_char += 1
def final_draw_board(words_dict):
    # Drawing final board
    print("Below is the list of all possible words with the letters")
    for i in words_dict:
        for j in range(len(words_dict[i])):
            print("———")
            print("|" + words_dict[i][j] + "|🟢")
            print("———")
            print()
final_draw_board(all_words)
"""
##########################
"""
hangman = [
    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t\t      \t\t|" + "\t\t\t\t\n"
    "\t          \t\t|\n"
    "\t\t   \t\t\t|\n"
    "          \t\t\t|\n"
    "    \t  \t     \t|\n"
    "\t\t  \t\t\t|\n"
    "\t\t  \t\t\t|\n"
    "\t            \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",

    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t   —————  \t\t|" + "\t\t\t\t\n"
    "\t  (     ) \t\t|\n"
    "\t\t   \t\t\t|\n"
    "          \t\t\t|\n"
    "    \t  \t     \t|\n"
    "\t\t  \t\t\t|\n"
    "\t\t  \t\t\t|\n"
    "\t            \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",

    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t   —————  \t\t|" + "\t\t\t\t\n"
    "\t  (     ) \t\t|\n"
    "\t\t   \t\t\t|\n"
    "         |\t\t\t|\n"
    "    \t |\t     \t|\n"
    "\t\t |\t\t\t|\n"
    "\t\t |\t\t\t|\n"
    "\t     |      \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",

    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t   —————  \t\t|" + "\t\t\t\t\n"
    "\t  ( o o ) \t\t|\n"
    "\t\t~~~\t\t\t|\n"
    "         |\t\t\t|\n"
    "    \t |\t     \t|\n"
    "\t\t |\t\t\t|\n"
    "\t\t |\t\t\t|\n"
    "\t     |      \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",

    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t   —————  \t\t|" + "\t\t\t\t\n"
    "\t  ( o o ) \t\t|\n"
    "\t\t~~~\t\t\t|\n"
    "    //———|———\\\\\t\t|\n"
    "    \t |\t     \t|\n"
    "\t\t |\t\t\t|\n"
    "\t\t |\t\t\t|\n"
    "\t     |      \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",

    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t   —————  \t\t|" + "\t\t\t\t\n"
    "\t  ( o o ) \t\t|\n"
    "\t\t~~~\t\t\t|\n"
    "    //———|———\\\\\t\t|\n"
    "   /\t |\t   \\   \t|\n"
    "\t\t |\t\t\t|\n"
    "\t\t |\t\t\t|\n"
    "\t   ——|——      \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",

    "—————————|——————————"
    "|\n         | \t\t\t|\n"
    "         | \t\t\t|\n"
    "\t   —————  \t\t|" + "\t\t\t\t\n"
    "\t  ( o o ) \t\t|\n"
    "\t\t~~~\t\t\t|\n"
    "    //———|———\\\\\t\t|\n"
    "   /*\t |\t  *\\   \t|\n"
    "\t\t |\t\t\t|\n"
    "\t\t |\t\t\t|\n"
    "\t  \\——|——/      \t|\n"
    "\t\t\t\t\t|\n"
    "\t\t\t\t————|————\n",
]

print(), print(), print()
for i in range(len(hangman)):
    print(hangman[i])
    print()
"""
############################
"""

my_list = ["apple", "banana", "cherry"]
print("This ⬇️ (using enumerate)")
for i, value_of_i_in_list in enumerate(my_list):
    print(f"Index: {i}, Value: {value_of_i_in_list}")
print("Is the same as this⬇️ (using for-range)")
for i in range(len(my_list)):
    print(f"Index: {i}, Value: {my_list[i]}")
print("Enumerate sort of works like a regular for-range list\nbut instead"
      "of accessing the ith value of the list or\ntuple or string, by doing"
      "this: my_list[i] for lists,\nenumerates allows you to start your loop\n"
      "instantiation with two variables, with an 'index' and\nwith a 'value'"
      "so something like this:\n\n"
      "for index, value in enumerate(my_list):\n\n## and then printing the sentence"
      " could look like this\n\n"
      "    print(f'Index: {index}, Value: {value}')\n"
      "Which whichever way you do it, it'll look the same in this case")
print(), print()
my_list = ["apple", "banana", "cherry"]

# Using format method for string formatting
for index, value in enumerate(my_list): print("Index: {}, Value: {}".format(index, value))
print("\t  Same things")
for index, value in enumerate(my_list): print(f"Index: {index}, Value: {value}")
"""
############################
"""
# List comprehensions - basically writing a for loop
# and assigning it to a variable all in one sentence
word = "cheese"
guess = "e"
indices = [i for i, letter in enumerate(word) if letter == guess]
print(indices)

# Using a loop
even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i**2)
print(even_squares)

# Using list comprehension
even_squares = [i**2 for i in range(0,10) if i % 2 == 0]
print(even_squares)
"""
###################
"""
uppercase_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X",
            "Y", "Z", " "]
s_word = "boon dogs".upper()
word_completion = ""
word_completion = list(word_completion)
# Prints underscores with blanks if the secret word is two or more words
for index, value in enumerate(s_word):
    if value == " ":
        word_completion.append(" ")
        print(word_completion[index], end="")
    elif str(value).isalpha():
        word_completion.append("_")
        print(word_completion[index], end="")
word_completion = "".join(word_completion)
print(), print()

# The loop goes through every indice in the uppercase_alphabet and checks it with
# each letter in the secret word and returns true if correct
guess = input("Enter a word: ").upper()
num_count = 0
for some in range(len(guess)):
    for j in range(len(uppercase_alphabet)):
        if guess[some] == uppercase_alphabet[j]:
            num_count += 1
in_alphabet = False
if num_count == len(guess):
    in_alphabet = True
print()
if in_alphabet and len(guess) == len(s_word):
    # print()
    if guess == s_word:
        print(True)
"""
##########################
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# More list comprehension stuff this time with a nested for loop
# Using a loop
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)
print(flattened)
# Using list comprehension
flattened = [element for row in matrix for element in row]
print(flattened)
"""
####################
"""
# When using a while-else statement, as soon as the code gets to the else
# part, even if you have a varibale that may alter the while loops trucy,
# it can never go back up to check if the while loop is true.
# Run the code below to better understand
count_special_char = 0
again = ""

while count_special_char < 5 and (again.upper() == "Y" or again == ""):
    print(f"Count: {count_special_char}")
    count_special_char += 1
else:
    print("Loop condition is no longer true. Exiting the loop.")
    again = input("Play again (Y/N): ")
    count_special_char = 0
    while count_special_char < 5 and (again.upper() == "Y" or again == ""):
        print(f"Count: {count_special_char}")
        count_special_char += 1
    print("Loop condition is no longer true. Exiting the loop.")
    again = input("Play again (Y/N): ")
"""
######################
