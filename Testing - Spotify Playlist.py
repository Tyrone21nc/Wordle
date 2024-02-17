string = "name"
other_string = "I love black men"
the_max = 20
remaining = the_max - (len(string) + len(other_string))
print(remaining)
string = list(string)
for i in range(remaining):
    string.append(" ")
print(string)
print("|", end="")
all_nums = 0
for i in range(len(string)):
    print(string[i], end="")
    all_nums += 1
for j in range(len(other_string)):
    print(other_string[j], end="")
    all_nums += 1
print("|")
print(all_nums)
print(len(string) + len(other_string))
print(f"There are {remaining} spaces")








