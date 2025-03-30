"""
Author: Romain Donfack Dzeinse
Date: 1/21/24
Objective: Build a Hangman Game
Inspiration: I like playing Hangman and thought it would be fun to code it, and it has been.
"""
import random
from tkinter import *


windows = Tk()
windows.title("Name")

canvas = Canvas(windows, width=500, height=500)
canvas.pack()
def forHulk():
    Hulk = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Hulk)
    windows.mainloop()
def forCapA():
    CapA = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Captain America.png")
    canvas.create_image(0, 0, anchor=NW, image=CapA)
    windows.mainloop()
def forIronM():
    IronM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Iron Man.gif")
    canvas.create_image(0, 0, anchor=NW, image=IronM)
    windows.mainloop()
def forHawkE():
    HawkE = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hawkeye.gif")
    canvas.create_image(0, 0, anchor=NW, image=HawkE)
    windows.mainloop()
def forBlackW():
    BlackW = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Black Widow.gif")
    canvas.create_image(0, 0, anchor=NW, image=BlackW)
    windows.mainloop()

def forFalcon():
    Falcon = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Falcon.png")
    canvas.create_image(0, 0, anchor=NW, image=Falcon)
    windows.mainloop()
forFalcon()
def forThor():
    Thor = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Thor.png")
    canvas.create_image(0, 0, anchor=NW, image=Thor)
    windows.mainloop()
def forLoki():
    Loki = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Loki.png")
    canvas.create_image(0, 0, anchor=NW, image=Loki)
    windows.mainloop()
def forFlash():
    Flash = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Flash.png")
    canvas.create_image(0, 0, anchor=NW, image=Flash)
    windows.mainloop()
def forSuperM():
    SuperM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Superman.png")
    canvas.create_image(0, 0, anchor=NW, image=SuperM)
    windows.mainloop()
def forBatM():
    BatM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Batman.png")
    canvas.create_image(0, 0, anchor=NW, image=BatM)
    windows.mainloop()
def forWW():
    WW = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Wonder Woman.png")
    canvas.create_image(0, 0, anchor=NW, image=WW)
    windows.mainloop()
def forWolvE():
    WolvE = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Wolverine.png")
    canvas.create_image(0, 0, anchor=NW, image=WolvE)
    windows.mainloop()
def forCyborg():
    Cyborg = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Cyborg.png")
    canvas.create_image(0, 0, anchor=NW, image=Cyborg)
    windows.mainloop()
def forSuperG():
    SuperG = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Supergirl.png")
    canvas.create_image(0, 0, anchor=NW, image=SuperG)
    windows.mainloop()
def forMJW():
    MJW = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\MaryJaneWatson.png")
    canvas.create_image(0, 0, anchor=NW, image=MJW)
    windows.mainloop()
def forPeterP():
    PeterP = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Peter Parker.png")
    canvas.create_image(0, 0, anchor=NW, image=PeterP)
    windows.mainloop()
def forMay():
    May = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Aunt May.png")
    canvas.create_image(0, 0, anchor=NW, image=May)
    windows.mainloop()
def forMilesM():
    MilesM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Miles Morales.png")
    canvas.create_image(0, 0, anchor=NW, image=MilesM)
    windows.mainloop()
def forGwenS():
    GwenS = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\")
    canvas.create_image(0, 0, anchor=NW, image=GwenS)
    windows.mainloop()
def forSpideyV():
    SpideyV = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=SpideyV)
    windows.mainloop()
def forDocO():
    DocO = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=DocO)
    windows.mainloop()
def forGreenG():
    GreenG = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=GreenG)
    windows.mainloop()
def forTobeyM():
    TobeyM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=TobeyM)
    windows.mainloop()
def forAndrewG():
    AndrewG = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=AndrewG)
    windows.mainloop()
def forTomH():
    TomH = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=TomH)
    windows.mainloop()
def forTobeyM():
    TobeyM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=TobeyM)
    windows.mainloop()
def forTobeyM():
    TobeyM = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=TobeyM)
    windows.mainloop()
def forPeter():
    Peter = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Peter)
    windows.mainloop()
def forLois():
    Lois = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Lois)
    windows.mainloop()
def forBrian():
    Brian = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Brian)
    windows.mainloop()
def forStewey():
    Stewie = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Stewie)
    windows.mainloop()
def forMeg():
    Meg = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Meg)
    windows.mainloop()
def forChris():
    Chris = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Chris)
    windows.mainloop()
def forCleveland():
    Cleveland = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Cleveland)
    windows.mainloop()
def forJoe():
    Joe = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Joe)
    windows.mainloop()
def forQuagmire():
    Quagmire = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=Quagmire)
    windows.mainloop()
def forPewtershmidt():
    Pewtershmidt = PhotoImage(file="C:\\Users\\thier\\PycharmProjects\\Hulk.gif")
    canvas.create_image(0, 0, anchor=NW, image=forPewtershmidt())
    windows.mainloop()


def play_game():
    this_words = [
        "nigga", "boon dogs", "chess", "Marvel", "DC", "superheroes"
    ]
    my_categories = {
        "MARVEL": ["Hulk", "Captain America", "Iron Man", "Hawkeye", "Black Widow",
                   "Falcon", "Thor", "Loki"],
        "DC": ["Flash", "Superman", "Batman", "Wonder Woman", "Wolverine", "Cyborg",
               "Supergirl"],
        "SPIDER MAN": ["Mary Jane Watson", "Peter Parker", "May", "Miles Morales",
                       "Gwen Stacy", "Spidey Verse", "Doc Octavius", "Green Goblin"],
        "SPIDER MEN": ["Tobey Maguire", "Andrew Garfield", "Tom Holland"],
        "FAMILY GUY": ["Peter", "Lois", "Brian", "Stewey", "Meg", "Chris",
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
    """____________________________________________________________"""
    letters_guessed = []
    words_guessed = []
    guessed = False
    word_completion = ""
    # In the loop, I change the variable above to True
    # when the user guesses the secret word(s_word)
    lives = 0
    print("Let's Play Hangman")
    print("Choose a genre:")
    print("|", end="")
    for i in my_categories.keys():
        print(" ", i, end=" |")
    print()
    the_word = ""
    # Find a way to make the first letter of the genre guessed capitalized
    genre = input("Genre: ").upper()
    # print categories of words
    in_genre = True
    if genre in my_categories:
        the_word = random.choice(my_categories[genre]).upper()
    else:
        in_genre = False
    if in_genre:
        print(hangman[lives])
        word_completion = [""]
        for index, value in enumerate(the_word):
            if value == " ":
                word_completion.append(" ")
            elif str(value).isalpha():
                word_completion.append("_")
        word_completion = "".join(word_completion)
        print(word_completion)
    while not guessed and lives < 6 and in_genre:
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
            elif user_guess not in the_word:
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
                indices = [i for i, letter in enumerate(the_word) if letter == user_guess]
                for index in indices:
                    update_word_completion[index] = user_guess
                word_completion = "".join(update_word_completion)
                # If the user already guessed the word this below will happen
                if "_" not in word_completion:
                    guessed = True
        elif len(user_guess) == len(the_word) and in_alphabet:
            if user_guess in words_guessed:
                print()
                print(f"You already guessed the word, {user_guess}")
            elif user_guess != the_word:
                print()
                print(f"{user_guess} is not the word")
                lives += 1
                words_guessed.append(user_guess)
            else:
                guessed = True
                word_completion = the_word
        else:
            print()
            print("Not a valid guess")
        print(hangman[lives])
        if word_completion == the_word:
            print("—" * len(word_completion))
        print(word_completion)
        if word_completion == the_word:
            print("—" * len(word_completion))
        if the_word == "HULK":
            forHulk()
        # elif the_word == "CAPTAIN AMERICA":
        #     forCapA()
        # elif the_word == "IRON MAN":
        #     forIronM()
        # elif the_word == "HAWKEYE":
        #     forHawkE()
        # elif the_word == "BLACK WIDOW":
        #     forBlackW()
        # elif the_word == "FALCON":
        #     forFalcon()
        # elif the_word == "THOR":
        #     forThor()
        # elif the_word == "LOKI":
        #     forLoki()
        # elif the_word == "FLASH":
        #     forFlash()
        # elif the_word == "SUPERMAN":
        #     forSuperM()
        # elif the_word == "BATMAN":
        #     forBatM()
        # elif the_word == "WONDER WOMAN":
        #     forWW()
        # elif the_word == "WOLVERINE":
        #     forWolvE()
        # elif the_word == "CYBORG":
        #     forCyborg()
        # elif the_word == "SUPERGIRL":
        #     forSuperG()
        # elif the_word == "PETER PARKER":
        #     forPeterP()
        # elif the_word == "MAY":
        #     forMay()
        # elif the_word == "MILES MORALES":
        #     forMilesM()
        # elif the_word == "MARY JANE WATSON":
        #     forMJW()



    # Outside the Loop
    if guessed:
        print("CONGRATS!!!\n‍👨🏿‍🦱👨🏿You beat Hangman 👨🏿‍🦱👨🏿‍🦱")
    elif not in_genre:
        print()
        print("Game Over! The genre is not valid")
    else:
        print(f"It's too bad you ran out of tries.\nThe word was {the_word}! Maybe next time")
        print()


def main():
    play_game()
    return ""


# print(main())
play_again = input("Play again (y/n)")
while play_again == "y":
    play_game()
    play_again = input("Play again (y/n)")
else:
    print("Hope you had fun. Bye!!")
