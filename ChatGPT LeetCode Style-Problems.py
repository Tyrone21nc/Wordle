"""
1: Two Sum:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""


def two_sum(int_array, target):
    for i in range(len(int_array)):
        for j in range(len(int_array)):
            total = int_array[i]
            if total == target:
                return "The target is:", target, "and the indices for the total are:", i
            total = int_array[i] + int_array[j]
            if total == target:
                return "The target is:", target, "and the indices for the total are: ", i, "and",  j
    return "No total for your target:", target


t_list = [1, 8, 7, 2, 1, 9, 3]
my_target = 7
print("The list is: " + str(t_list) + " and the target is: " + str(my_target))
print(two_sum(t_list, my_target))


"""
2. Reverse Integer:
Reverse the digits of an integer.
"""


def reverser(the_num):
    if len(str(the_num)) <= 1:
        return the_num
    else:
        print(the_num)
        the_num = list(str(the_num))
        the_length = len(the_num)
        for i in range(len(the_num)):
            print(the_num[the_length-i-1], end=" ")
    # print("Original order: " + the_num)
    print()
    return the_num


nums = 9785412547854
nums = str(nums)
print(reverser(nums))



