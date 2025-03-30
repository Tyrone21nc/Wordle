"""
Name: Romain Donfack Dzeinse
Date: 2/17/24
Objective: Build Wells Fargo Login and account page
"""


all_accounts = {
    "username": "password",
    "Romain2Dzeinse": "password123",
}
alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
numbers = ["0123456789"]
biometrics = ["Save a key", "Save a combination", "Save answer to a question"]
biometrics_types = {
    "Save a key": "user will enter a key with a strict format",
    "Save a combination": "user will save two numbers and one word",
    "save answer to a question": ["list of questions","question1","question2","question3"]
}

save_a_key_req = ["8 characters long", "must have a number", "must have a capital letter",
                  "must have a special character !@#$%^&*()_"]
special_characters = "!@#$%^&*()_"

def show_logo():
    print("\u001b[1m\u001b[33m\u001b[41;1m\\    /\\    /  |—————/  |        |         |¯¯¯¯¯¯¯\033[0m")
    print("\u001b[1m\u001b[33m\u001b[41;1m \\  /  \\  /   |———     |        |         \\—————\\ \033[0m")
    print("\u001b[1m\u001b[33m\u001b[41;1m  \\/    \\/    |—————\\  |—————/  |—————/   _______|\033[0m")
    print("\\             ")
    print("\\             ")
    print("\\")
    print("\\")
    print("\\")
    print("\\")
    print("\\")


show_logo()
print("\t\t\t\t\t\t\t\t\u001b[1mLogin")
print("\t\t\t\t|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
username = input("\t\t\t\t|\t\t\tUsername:\t\t\t\t|\n\t\t\t\t|\t\t\t\t--> ")
print(end="\t\t\t\t|\t\t\t\t\t\t\t\t\t|")
print()
password = input("\t\t\t\t|\t\t\tPassword:\t\t\t\t|\n\t\t\t\t|\t\t\t\t--> ")
print(end="\t\t\t\t|___________________________________|")
print()
save_u = input("\t\t\t\t\u001b[1mSave username?(y/n): ")
set_up_biometric = input("\t\t\t\t\u001b[1mSet up a Biometric sign-on?(y/n): ")

if username not in all_accounts.keys():
    if save_u.lower() == "y":
        all_accounts[username] = password

else:
    print("cheese")
    print(all_accounts)
    if set_up_biometric.lower() == "y":
        print("|", end="\t")
        for i in range(len(biometrics)):
            print(biometrics[i], end="\t|\t")
        which_biometric = input("\nWhich one do you want to do(1-3)? ")
        if which_biometric == "1":
            print(f"Now that you have selected Save a key, here are the requirements:\n", end="")
            for i in range(len(save_a_key_req)):
                print(f"•  {save_a_key_req[i]}")
            print()
            save_key = input("Enter a key to save: ")
            if len(save_key) >= 8:
                # If password contains at least 8 characters
                for k in range(len(save_key)):  # Go through every character in save_key
                    if save_key[k] in numbers:  # If it has a number
                # If it contains at least 1 number
                        for i in range(len(alphabet)):
                            if save_key[i] in alphabet:  # if it's uppercase
                # If it has a capital letter
                                for j in range(len(save_key)):
                                    count = 0
                                    if save_key in special_characters:
                                        count += 1
                                        if count == 1:
                                            print("Password is valid✅")
                # if it has spec char
                                else:
                                    print("Add a special character")
                            else:
                                print("Add a capital letter")
                    else:
                        print("Add a number")
            else:
                print("Make sure password is 8 or more characters long")


print()







