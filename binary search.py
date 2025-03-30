"""
Author: Romain Dzeinse
Date: 04/12/24
Objective: I will be creating a binary search algorithm
Plan: Go through a SORTER list and find your number by constantly splitting the
list in half and checking if the value is either on the left or right side of the list
        return its position
"""


def binary_search(given_list, the_num):
    mid = len(given_list) // 2
    first_half = given_list[:mid]
    second_half = given_list[mid:]
    if the_num in given_list[:mid]:
        for i in range(len(first_half)):
            if the_num == first_half[i]:
                return f"the position is {i} in first sub-list"
    elif the_num in given_list[mid:]:
        for i in range(len(second_half)):
            if the_num == second_half[i]:
                return f"the position is {i} in second sub-list"
    return "Not in either sub-lists"


my_list = [1, 4, 5, 7, 8, 9]
num = 4
pos_of_num = binary_search(my_list, num)
print(pos_of_num)

"""
Author: Romain Dzeinse
Date: 04/12/24
Objective: Here I will be writing a linear search algorithm
Plan: Go through a NON SORTED list and check every indices in it to see if it matches the given number
        return its position
"""


def linear_search(the_list, the_num):
    for i in range(len(the_list)):
        if the_num == the_list[i]:
            return i


list2 = [1, 4, 7, 8, 2, 4, 2, 3, 6, 9]
num2 = 3
position_of_num = linear_search(list2, num2)
print(position_of_num)

import string