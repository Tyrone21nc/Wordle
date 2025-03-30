"""
Write a program that only sums up all the ascending number in a given set of numbers
For example: You are given this set of number: 1,2,1,4,3,7,10 -> the ascending numbers are 1,2,4,7,10
Therefore the sum of the ascending numbers would be: 24
"""

number = input("Enter only numbers (No letters) -> quit to stop: ")
the_Nums = []
while number != "quit":
    the_Nums.append(int(number))
    number = input("Enter only numbers (No letters) -> quit to stop: ")

s = the_Nums[0]
for i in range(len(the_Nums)-1):
    if the_Nums[i] < the_Nums[i+1]:
        s += the_Nums[i+1]
print(s)
print()
print()
