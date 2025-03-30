"""
    Author: Romain Dzeinse
    Date: 9/8/24
    Objective: Linear Search Algorithm
"""


def b_search(arr, low, high, target):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1

    return -1


if __name__ == "__main__":
    x = 15
    ar = [1, 3, 5, 8, 15, 25, 40, 102]
    print(f"array:   {ar}")
    print(f"target:  {x}")
    print(f"The target element \033[30m{x}\033[0m is in position \033[32m{b_search(ar, 0, len(ar)-1, x)}\033[0m")
