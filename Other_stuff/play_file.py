import random
import time

if False:
    letters_list = ["S", "T", "O", "M", "R", "A"]
    print("\t\t\t\t\tWelcome to Wordscape")
    print("Rules:"
          "\n>>> Guess all possible words with the following letters"
          "\n>>> No 2 letter words"
          "\n>>> Word is in valid if it contains a letter not in the list"
          "\n>>> You are allowed to duplicate letters")


    def valid_word(guess):
        invalid_letters = []
        good_word = False
        for i in range(len(guess)):
            if guess[i] not in letters_list:
                invalid_letters.append(guess[i])

        if not invalid_letters:
            good_word = True
        return good_word


    def scramble_letters(new_letter_list):
        random.shuffle(new_letter_list)
        letters(new_letter_list)
        return new_letter_list


    def letters(the_letters):
        print("\t\t\t\t\t\t\t  \033[96m_______")
        for i in range(len(the_letters)):
            if i % 2 == 1 and i != 0:
                print("  ", end="")
                print(the_letters[i], "|\n", end="")
            else:
                print("\t\t\t\t\t\t\t", end="")
                print(" |", the_letters[i], end=" ")
        print(end="\t\t\t\t\t\t\t  ¯¯¯¯¯¯¯\033[0m")
        print()


    def all_guesses(u_guess, u_v_guess):
        return u_guess, u_v_guess


    def play_game():
        letters(letters_list)
        word = input("Guess a word from given letters(press enter to quit):\n<<< ").upper()
        user_guesses = []
        user_valid_guesses = []
        times_for_rotating_list = 0
        while len(word) > 2 and not "":
            is_it_good = valid_word(word)
            if is_it_good:
                if word not in user_guesses:
                    user_guesses.append(word)
                    if word not in user_valid_guesses:
                        user_valid_guesses.append(word)
                print(f"\033[38;2;57;255;20m{word} is valid\033[0m")
            else:
                if word not in user_valid_guesses:
                    print(f"\033[38;2;255;69;0m{word} is not valid\033[0m")
                    user_guesses.append(word)
            times_for_rotating_list += 1
            if times_for_rotating_list % 3 == 0:
                shuffle_or_nah = input("Do you want to shuffle the letters? (y/n): ").lower()
                if shuffle_or_nah == "y":
                    scramble_letters(letters_list)
            word = input("Guess a word from given letters(press enter to quit):\n<<< ").upper()
        guesses = all_guesses(user_guesses, user_valid_guesses)
        return guesses


    the_guesses = play_game()
    print("All your \033[38;2;57;255;20mvalid\033[0m guesses: ", end="")
    for i in range(len(the_guesses[1])):
        print(f"\033[38;2;57;255;20m{the_guesses[1][i]}\033[0m", end=" ")
    print()
    print("All valid guesses: ", end="")
    for i in range(len(the_guesses[1])):
        print(f"\033[38;2;57;255;20m{the_guesses[1][i]}\033[0m", end=" ")
    print()


    print("\033[38;2;255;0;0mGAME OVER\033[0m\033[0m")

    # print("\033[38;2;255;165;0mNeon green text\033[0m")















    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.plot(x, y, color='green')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Example Plot')
    # plt.show()


from tkinter import *

windows = Tk()
windows.title('An Image')

canvas = Canvas(windows, width=400, height=270)
canvas.pack()

image = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Say My Name BB scene.gif")
canvas.create_image(0, 0, anchor=NW, image=image)

windows.mainloop()


