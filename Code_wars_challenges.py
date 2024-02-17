"""
Codewars challenge #1: Multiples of 3 or 5

Prompt: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Finish the solution so that it returns the sum of all the multiples of
3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    the_sum = 0
    mult_of_3 = []
    mult_of_5 = []
    for i in range(number):
        if number < 0:
            return 0
        else:
            if i % 3 == 0:
                mult_of_3.append(i)
            elif i % 5 == 0:
                mult_of_5.append(i)
    print("Multiple of 3",  mult_of_3)
    print("Multiple of 5",  mult_of_5)
    final_mult_list = []
    for j in range(len(mult_of_3)):
        if mult_of_3[j] in mult_of_5:
            final_mult_list.append(mult_of_3[j])
        else:
            final_mult_list.append(mult_of_3[j])
    for k in range(len(mult_of_5)):
        if mult_of_5[k] not in final_mult_list:
            final_mult_list.append(mult_of_5[k])

    for l in range(len(final_mult_list)):
        the_sum += final_mult_list[l]

    return the_sum


# Second Solution below
def the_solution(number):
    the_sum = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            the_sum += i

    return the_sum


# Both solutions work, one is just faster
num = input("Enter a number (enter quit to stop): ")
while num != "quit":
    num = int(num)
    print("First function \t Second function")
    print(solution(num), "\t\t\t\t", the_solution(num))
    num = int(input("Enter a number (enter quit to stop): "))
else:
    print("End of code")

