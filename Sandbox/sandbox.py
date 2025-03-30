"""
Author: Romain Dzeinse
Date: 5/24/24
Objective: Test code
"""


def make_triangle():
    for i in range(5):
        for j in range(i):
            if j == 3:
                print("*", end="")
            print("*", end="")
        print()


# def reverse_string(string, n):
#     new_string = ""
#     if len(string) == n:
#         for i in range(len(string)):
#             new_string += string[len(string)-1-i]
#     return new_string

def reverse_string(string, n):
    new_string = ""
    # if len(string) == n:
    #     for i in range(len())


if __name__ == "__main__":
    make_triangle()
    my_string = "chess"
    my_n = 5
    my_string = reverse_string(my_string, my_n)
    print(my_string)
