"""
Author: Romain Dzeinse
Date: 06/7/24
Objective: Create an algorithm that validates passwords on making sure it includes all the required stuff
filename: password_checker.py
"""
import random


def generate_password(f_name):
    """
    This is the pseudocode:
    - First create the function with the appropriate parameters
    - create a variable named password to store all the password components
    - have random characters from first name
        - Then create a list with letters of the first name
        - Then get a set of 3, representing the number of characters in the f_name string;
            this is after the first round
        - The number of rounds is random from (2-4) between 2 and 3, not including 4
    - have random numbers (0-9)
        - Then randomly get 2 numbers from a numbers list
    - have random spec chars (!@#$%^&*())
        - Then randomly get 2 special characters from a spec char list
    - Then add all the random string characters from f_name, and then
        add the numbers, then ass the spec characters. That should be at least 10 characters

    :param f_name: the first name
    :return: this will return the generated password
    """
    password = ""
    random_set = random.choice(range(2, 4))
    for the_set in range(random_set):
        counter_for_upper_case = 0
        for i in range(3):
            random_fname = random.choice(f_name)
            if counter_for_upper_case == 0:
                random_fname = random_fname.upper()
            password += random_fname
            counter_for_upper_case += 1

    numbers = "1234567890"
    for i in range(2):
        random_num = random.choice(numbers)
        password += random_num

    special_characters = "!@#$%^&*()"
    for i in range(2):
        random_spec_char = random.choice(special_characters)
        password += random_spec_char

    return password


if __name__ == "__main__":
    print("This is a random password generator.\nWe just need your first name or nick-name\n")
    first_name = "romain"
    fname = input("Please enter your first name: ").lower()
    password_good = False
    while not password_good:
        if not fname:
            fname = "abcde"
        print(f"\033[32m{generate_password(fname)}\033[0m")
        like_password = input("Do you like your password (y/n): ").lower()
        if like_password == "y":
            password_good = True
            print("I'm glad to hear")
