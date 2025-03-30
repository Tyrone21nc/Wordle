"""
Name: Romain Donfack Dzeinse
Date: 2/17/24
Objective: Build Wells Fargo Login and account page
"""
from colorama import Fore, Back, Style

all_accounts = {
    "username": "password",
    "name": "random",
    "Romain2Dzeinse": "password123",
}


def show_logo():
    print("\u001b[1m\u001b[33m\u001b[41;1m\\    /\\    /  |—————/  |        |         |¯¯¯¯¯¯¯\033[0m")
    print("\u001b[1m\u001b[33m\u001b[41;1m \\  /  \\  /   |———     |        |         \\—————\\ \033[0m")
    print("\u001b[1m\u001b[33m\u001b[41;1m  \\/    \\/    |—————\\  |—————/  |—————/   _______|\033[0m")
    print("\t\t\t\t\t\tWELLS FARGO             ")


show_logo()
print(f"\033[0;30m\u001b[1m\t\t\t\t{Back.RED}\t\t\t  \033[0;30m\u001b[1m{Back.YELLOW} Login{Back.RED}\t\t\t\t \033[0m")
print(f"\033[0;30m\u001b[1m\t\t\t\t{Back.RED}|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\033[0m")
username = input(f"\033[0;30m\u001b[1m\t\t\t\t{Back.RED}|\t\t\t\033[0;30m\u001b[1m{Back.YELLOW}Username:\033[0m{Back.RED}\t\t\t\t\033[0m{Back.RED}|\033[0m\n\t\t\t\t{Back.RED}|\t\t\t\t--> ")
print(end=f"\033[0;30m\u001b[1m\033[0m\t\t\t\t{Back.RED}|\t\t\t\t\t\t\t\t\t|\033[0m")
print()
password = input(f"\033[0;30m\u001b[1m\t\t\t\t{Back.RED}|\t\t\t\033[0;30m\u001b[1m{Back.YELLOW}Password:{Back.RED}\t\t\t\t|\033[0m\n\t\t\t\t\033[0;30m\u001b[1m{Back.RED}|\t\t\t\t--> ")
print(end=f"\033[0;30m\u001b[1m\t\t\t\t{Back.RED}\033[0;30m\u001b[1m|___________________________________|\033[0m")
print()
save_u = input("\t\t\t\t\u001b[1mSave username?(y/n): ")
set_up_biometric = input("\t\t\t\t\u001b[1mSet up a Biometric sign-on?(y/n): ")


def add_biometrics():
    uppercase_alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    numbers = ["0123456789"]
    biometrics = ["Save a key", "Save a combination", "Save answer to a question"]
    biometrics_types = {
        "Save a key": "user will enter a key with a strict format",
        "Save a combination": "user will save two numbers and one word",
        "save answer to a question": ["list of questions", "question1", "question2", "question3"]
    }

    save_a_key_req = ["8 characters long", "must have a number", "must have a capital letter",
                      "must have a special character !@#$%^&*()_"]
    # valid_key = False
    special_characters = ["!@#$%^&*()_"]

    if set_up_biometric.lower() == "y":
        print("|", end="\t")
        for i in range(len(biometrics)):
            print(biometrics[i], end="\t|\t")
        which_biometric = input("\nWhich one do you want to do(1-3)? ")
        if which_biometric == "1":
            which_biometric = biometrics[0]
            print(f"Now that you have selected Save a key, here are the requirements:\n", end="")
            for i in range(len(save_a_key_req)):
                print(f"•  {save_a_key_req[i]}")
            print()
            save_key = input("Enter a key to save: ")
            if len(save_key) >= 8:
                # If password contains at least 8 characters
                count_numbers = 0
                for k in range(len(save_key)):  # Go through every character in save_key
                    if save_key[k] in numbers[0] and count_numbers < 1:  # If it has a number
                # If it contains at least 1 number
                        count_numbers += 1
                        count_alphabet = 0
                        for i in range(len(save_key)):
                            if save_key[i] in uppercase_alphabet[0] and count_alphabet < 1:  # if it's uppercase
                                # If it has a capital letter
                                count_special_char = 0
                                for j in range(len(save_key)):
                                    count_alphabet += 1
                                    if save_key[j] in special_characters[0] and count_special_char < 1:
                                        count_special_char += 1
                                        print("key is valid✅")
                                        biometrics_types[which_biometric] = save_key
                                    # if it has spec char
                                    else:
                                        if special_characters == 2:
                                            print("Add a special character")
                            else:
                                if count_alphabet == 2:
                                    print("Add a capital letter")
                    else:
                        if count_numbers == 2:
                            print("Add a number")
            else:
                print("Make sure password is 8 or more characters long")
    times = 0
    for key, value in biometrics_types.items():
        # if times > 2:
        print(f"key:{key}  value:{value}")
            # times += 1


if username not in all_accounts.keys():
    if save_u.lower() == "y":
        all_accounts[username] = password
    add_biometrics()


else:
    print("cheese")
    print(all_accounts)
    add_biometrics()









