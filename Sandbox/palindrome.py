"""
Author: Romain Dzeinse
Date: 6/27/24
File: palindrome.py
Objective: Write a program that checks if a string is a Palindrome (same front the front as from the back
ex: swims racecar 12321) using a two point approach (which is starting from the beginning and from the end
string: "swims"   first pointer would be the first "s", in the beginning and the second pointer would be the
second "s", at the end)
"""


def is_palindrome(string):
    """
    :param string: the string
    :return: a boolean value saying the string is a Palindrome or not
    """
    string = string.lower()
    first = 0
    last = len(string)-1

    for i in range(len(string)):
        if first != last:
            if string[first] != string[last]:
                return False
            else:
                first += 1
                last -= 1
    return True


def is_palindrome2(string):
    """
    With a while loop
    :param string: the string
    :return: a boolean value saying the string is a Palindrome or not
    """
    string = string.lower()

    if not string:
        return False

    palin = False
    first = 0
    last = len(string) - 1
    while string[first] == string[last]:
        if first == last:
            return True
        first += 1
        last -= 1
    else:
        return False


if __name__ == "__main__":
    my_strings = ["madam", "cheese", "civic", "people", "racecar", "12321", "kayak", ""]

    for word in my_strings:
        if is_palindrome2(word):
            print(f"\033[32m{word}\033[0m is a Palindrome")
        else:
            if not word:
                print(f"\033[31m{word}\033[0m is not a Palindrome")
            else:
                print(f"\033[31m{word}\033[0m is not a Palindrome")

