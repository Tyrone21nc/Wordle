"""
Author: Romain Dzeinse
Date: 6/28/24
File name: missing_in_array.py
Objective: Given an array arr of size n which contains elements in range from 0 to n-1, you need to find
all the elements occurring more than once in the given array. Return the answer in ascending order.
If no such element is found, return list containing [-1].

Note: Try and perform all operations within the provided array. The extra (non-constant) space needs
to be used only for the array to be returned.
Examples:
Input: arr[] = {0,3,1,2}, n = 4
Output: -1
Explanation: There is no repeating element in the array. Therefore, output is -1.

Input: arr[] = {2,3,1,2,3}, n = 5
Output: 2 3
Explanation: 2 and 3 occur more than once in the given array.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
"""


def duplicate2(n, arr):
    # This is my best attempt if we cannot use the sorted function
    first_num = arr[0]
    already_seen = [first_num]
    duplicate_list = []
    for i in range(1, n):
        if arr[i] not in already_seen:
            already_seen.append(arr[i])
        else:
            duplicate_list.append(arr[i])
            length = len(duplicate_list)
            if len(duplicate_list) > 1:
                if duplicate_list[length-2] > duplicate_list[length-1]:
                    temp = duplicate_list[length-2]
                    duplicate_list[length-2] = duplicate_list[length-1]
                    duplicate_list[length-1] = temp


    if not duplicate_list:
        return -1
    return duplicate_list


def duplicate(n, arr):
    # If I am allowed to use the sorted function sorting(), this is my answer

    first_num = arr[0]
    already_seen = [first_num]
    duplicate_list = []
    for i in range(1, n):
        if arr[i] not in already_seen:
            already_seen.append(arr[i])
        else:
            duplicate_list.append(arr[i])
            length = len(duplicate_list)
            if len(duplicate_list) > 1:
                duplicate_list.sort()
    if not duplicate_list:
        return -1
    return duplicate_list


if __name__ == "__main__":
    b = [5, 0, 5, 3, 3, 1, 2, 2]
    c = []
    d = []
    a = len(b)
    print(duplicate2(a, b))


