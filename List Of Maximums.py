"""
Create a function that takes a 2d list and returns a list of all the maxes of each sub-list:
For example: If I was given the 2d list: [[1,8,4,3],[8,1,9,2],[0,1,8,19],[0],[]] -> If the sub-list is
empty, the max is zero, if the sub-list only has zero, the max is zero
I would be returning: [8,9,19,0,0]
"""


def list_of_maxs(the_lists):
    if not the_lists:
        return 0
    else:
        my_max = the_lists[0]
        for i in range(len(the_lists) - 1):
            if my_max < the_lists[i + 1]:
                my_max = the_lists[i + 1]
        return my_max

list1 = list_of_maxs([1, 8, 4, 3])
list2 = list_of_maxs([8, 1, 9, 2])
list3 = list_of_maxs([0, 1, 8, 19])
list4 = list_of_maxs([0])
list5 = list_of_maxs([])
print(list1, list2, list3, list4, list5)
the_max = [list1, list2, list3, list4, list5]
print(the_max)
