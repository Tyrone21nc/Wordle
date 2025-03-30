import random


def missing_number(array, n):
    # code here
    # some = list(range(1, number + 1))
    random_num = random.choice(array)
    array.remove(random_num)
    print(f"missing number {random_num}")
    num = 0
    for i in range(len(array) - 1):
        if array[i] not in list(range(1, n+1)):
            num = array[i]
            print("Cheese")
        print(array[i])
    print()
    return num


number = 5
my_list = list(range(1, number+1))
# print(my_list)
# random_num = random.choice(my_list)
# my_list.remove(random_num)
# print(f"From the list ->{my_list}, the missing number is {random_num}")
print(missing_number(my_list, number))


