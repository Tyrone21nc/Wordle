"""
Author: Romain Dzeinse
Date: 05/6/24
Objective: Create dictionary or random words to use for Wordle with a Twist game
"""


def the_dict():
    words_dict = {
        "1": [
            [" ", "M", " ", "O", " "],
            ["B", "O", "M", "B", "S"],
            [" ", "N", " ", "X", " "],
            ["P", "E", "N", "I", "S"],
            [" ", "Y", " ", "N", " "], ],
        "2": [
            [" ", "X", " ", "X", " "],
            ["X", "X", "X", "X", "X"],
            [" ", "X", " ", "X", " "],
            ["X", "X", "X", "X", "X"],
            [" ", "X", " ", "X", " "], ],
        "3": [
            [" ", "P", " ", "P", " "],
            ["S", "L", "E", "E", "P"],
            [" ", "A", " ", "C", " "],
            ["S", "N", "E", "A", "K"],
            [" ", "K", " ", "N", " "]],
        "4": [
            [" ", "X", " ", "X", " "],
            ["X", "X", "X", "X", "X"],
            [" ", "X", " ", "X", " "],
            ["X", "X", "X", "X", "X"],
            [" ", "X", " ", "X", " "], ],
    }
    return words_dict


def select_dict(dict_number):
    lists = the_dict()
    return lists[dict_number]
