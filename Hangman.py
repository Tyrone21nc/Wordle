"""
Author: Romain Donfack Dzeinse
Date: 1/21/24
Objective: Build a Hangman Game
Inspiration: I like playing Hangman
"""
import random
this_words = [
    "nigga", "boon dogs", "chess", "Marvel", "DC", "superheroes"
]
my_categories = {
    "Marvel": ["Hulk", "Captain America", "Iron Man", "Hawkeye", "Black Widow",
               "Falcon", "Thor", "Loki", "Chicken Beef Pot"],
    "DC": ["Flash", "Superman", "Batman", "Wonder Woman", "Wolverine", "Cyborg",
           "Supergirl"],
    "Spider-man": ["Mary Jane Watson", "Peter Parker", "May", "Miles Morales",
                   "Gwen Stacy", "Spidey Verse", "Doc Octavius", "Green Goblin"],
    "Spider-men": ["Tobey Maguire", "Andrew Garfield", "Tom Holland"],
    "Family Guy": ["Peter", "Lois", "Brian", "Stewey", "Meg", "Chris",
                   "Cleveland", "Joe", "Quagmire", "Pewtershmidt"]
}
# secret_word = random.choice(random_words).upper()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X",
            "Y", "Z", " ", "-"]
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
# print()
# print("How to win: Don't get this")
# print("—————————|——————————", end="")
# print("|\n         | \t\t\t|")
# print("         | \t\t\t|")
# print("\t   —————  \t\t|")
# print("\t  ( o o ) \t\t|")
# print("\t\t~~~\t\t\t|")
# print("    //———|———\\\\\t\t|")
# print("   /*\t |\t  *\\   \t|")
# print("\t\t |\t\t\t|")
# print("\t\t |\t\t\t|")
# print("\t  \\——|——/      \t|")
# print("\t\t\t\t\t|")
# print("\t\t\t\t\t|")


def play_game():
    s_word = random.choice(this_words).upper()
    word_completion = "_" * len(s_word)
    letters_guessed = []
    words_guessed = []
    guessed = False
    user_guess = ""
    # In the loop, I change the variable above to True
    # when the user guesses the secret word(s_word)
    lives = 0
    print("Let's Play Hangman")
    print('type "ENDGAME" to change word')
    print("Choose a genre:")
    print("|", end="")
    for i in my_categories.keys():
        print(" ", i, end=" |")
    print()
    random_word = ""
    genre = input("Genre: ").upper()
    # print categories of words
    if genre in my_categories:
        random_word = random.choice(my_categories[genre]).upper()

    # word_completion = "_" * len(random_word)
    print(hangman[lives])
    # print(word_completion, "\n")
    word_completion = ""
    word_completion = list(word_completion)
    for index, value in enumerate(random_word):
        if value == " ":
            word_completion.append(" ")
        elif str(value).isalpha():
            word_completion.append("_")
    word_completion = "".join(word_completion)
    if "" not in word_completion:
        print(word_completion, "\n")

    while not guessed and lives < 6:
        if lives == 5:
            print("Last life")
        user_guess = input("Please enter a letter or a word: ").upper()
        num = 0
        for some in range(len(user_guess)):
            for j in range(len(alphabet)):
                if user_guess[some] == alphabet[j]:
                    num += 1
        in_alphabet = False
        if num == len(user_guess):
            in_alphabet = True
        if len(user_guess) == 1 and user_guess in alphabet:
            if user_guess in letters_guessed:
                print()
                print(f"You already guessed {user_guess}")
            elif user_guess not in random_word:
                print()
                print(f"{user_guess} is not in the word")
                lives += 1
                letters_guessed.append(user_guess)
            else:  # Check if guess letter is in the word
                print()
                print(f"Nice, {user_guess} is in the word")
                letters_guessed.append(user_guess)
                update_word_completion = list(word_completion)
                # update_word_completion[lives] = user_guess
                indices = [i for i, letter in enumerate(random_word) if letter == user_guess]
                for index in indices:
                    update_word_completion[index] = user_guess
                word_completion = "".join(update_word_completion)
                # If the user already guessed the word this below will happen
                if "_" not in word_completion:
                    guessed = True
        elif len(user_guess) == len(random_word) and in_alphabet:
            if user_guess in words_guessed:
                print()
                print(f"You already guessed the word, {user_guess}")
            elif user_guess != random_word:
                print()
                print(f"{user_guess} is not the word")
                lives += 1
                words_guessed.append(user_guess)
            else:
                guessed = True
                word_completion = random_word
        else:
            print()
            print("Not a valid guess")
        print(hangman[lives])
        if word_completion == random_word:
            print("—" * len(word_completion))
        print(word_completion)
        if word_completion == random_word:
            print("—" * len(word_completion))
    # Outside the Loop
    if guessed:
        print("CONGRATS!!!\n‍👨🏿‍🦱👨🏿You beat Hangman 👨🏿‍🦱👨🏿‍🦱")
    else:
        print(f"It's too bad you ran out of tries.\nThe word was {random_word}! Maybe next time")
        print()


def main():
    play_game()
    play_again = input("Play Again? (Y/N): ").upper()
    print(), print()
    while play_again == "Y":
        play_game()
        play_again = input("Play Again? (Y/N): ").upper()
    return " "


print(main())
