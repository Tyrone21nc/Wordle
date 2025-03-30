"""
Author: Romain Dzeinse
Date: 6/28/24
File name: second_largest.py
Objective: Given an array arr of size n, print the second-largest distinct element
from an array. If the second-largest element doesn't exist then return -1.

Example 1:
Input:
n = 6, arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the array is 35 and the second-largest element is 34.
Example 2:
Input:
n = 3, arr[] = {10, 5, 10}
Output: 5
Explanation: The largest element of the array is 10 and the second-largest element is 5.
"""


def sec_largest(n, arr):
    # counter = 0
    # s_largest = arr[0]
    #
    # if n < 2:
    #     return -1
    #
    # for i in range(1, n):
    #     current_lar = 0
    #     if arr[i] > s_largest:
    #         s_largest = arr[i]
    if n == 1:
        return -1

    m = max(arr)
    c = arr.index(m)
    del arr[c]
    return max(arr)


def palindrome_part2(word):
    first = 0
    last = len(word) - 1
    for i in range(len(word)):
        if word[first].isalpha():
            if word[last].isalpha():
                if word[first].lower() == word[last].lower():
                    first += 1
                    last -= 1
                else:
                    return False
            else:
                last += -1
        else:
            first += 1

    return True


def palindrome(s):
    # This is the best palindrome algorithm that works for all circumstances

    first = 0
    last = len(s)-1
    while first < last:
        while (not s[first].isalnum()) and first < last:
            first += 1

        while (not s[last].isalnum()) and first < last:
            last -= 1

        if s[first].lower() != s[last].lower():
            return False

        first += 1
        last -= 1

    return True


if __name__ == "__main__":
    b = [12, -10, 1, 10, 90, 1]
    a = len(b)
    # print(sec_largest(a, b))

    the_string = "A man, a plan, a canal: Panama"
    print(palindrome(".p"))


