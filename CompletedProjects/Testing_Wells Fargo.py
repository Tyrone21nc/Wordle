chess = ["1234567890"]
# key = input("Enter a key: ")
# num = 0
# print(f"the length of key is {len(key)}")
# another_num = 0
# for i in range(len(key)):
#     if key[i] in chess[0] and another_num<1:
#         num += 1
#         another_num+=1
# else:
#     print("I didn't know a for loop could have an else statement")
# print(f"the number of numbers in the key is {num}")

print(len(chess[0]))
print("\n*3")
print("\u001b[33mI like chess")


from colorama import Fore, Back, Style

print(Fore.RED + 'This text is red')
print(Back.RED + 'This text has a green background')
print(Back.YELLOW + 'This text has a green background')
print(Style.RESET_ALL + 'Back to normal')


import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
my_list = [1, 2, 3, 4, 5]
print("[", end="")
for i in range(len(my_list)):
    if i < len(my_list)-1:
        print(my_list[i], end=" ")
print(f"{my_list[len(my_list)-1]}]")
