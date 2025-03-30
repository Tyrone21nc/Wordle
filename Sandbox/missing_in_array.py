"""
Author: Romain Dzeinse
Date: 6/28/24
File name: missing_in_array.py
Objective: Given an array of size n-1 such that it only contains distinct integers in the range of 1 to n.
Return the missing element.
Ex1:
Input: n = 5, arr[] = {1,2,3,5}
Output: 4
Explanation : All the numbers from 1 to 5 are present except 4.
Ex2:
Input: n = 2, arr[] = {1}
Output: 2
Explanation : All the numbers from 1 to 2 are present except 2.
"""


def missing_num2(num_list):
    if not num_list:
        return 1
    elif len(num_list) == 1:
        return 2
    else:
        first = 0
        next_num = 1
        missing_nms = 0
        for i in range(len(num_list)-1):
            difference = num_list[next_num] - num_list[first]
            if difference > 1:
                missing_nms = num_list[first] + 1
            first += 1
            next_num += 1

        return missing_nms


def missing_num(n, num_list):
    if not num_list:
        if n:
            return n
        else:
            return
    elif len(num_list) == 1:
        if num_list[0] != n:
            return n
    else:
        first = 0
        next_num = 1
        length = len(num_list)
        if num_list[length-1] == n:
            for i in range(length - 1):
                difference = num_list[next_num] - num_list[first]
                if difference > 1:
                    return num_list[first] + 1
                first += 1
                next_num += 1
        else:
            return n


if __name__ == "__main__":
    a = [1, 2, 3, 5]
    b = [1]
    c = 2
    print(missing_num(c, b))

