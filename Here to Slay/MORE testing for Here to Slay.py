# chess = [[], ["|       |Dragons Slayed:0 |       |"]]
big = [["-----------------------------------"],
       ["|Player:X |                      |"],
       ["|          |                      |"],
       ["|¯¯¯¯¯¯¯¯¯¯¯                      |"],
       ["|                                 |"],
       ["|       ___________________       |"],
       ["|       |Monsters Slayed:0 |      |"],
       ["¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"]]
chess = big[7]

print(chess)
split = chess[1][0].split(":")
print(f"this is split: {split}")
print(split)
split_again = split[1].split(" ")
# print(split_again)
split_again[0] = "\u001b[35m1\033[0m"
print(f"this is split again: {split_again}")
joined_split_again = " ".join(split_again)
print(f"this is joined split again: {joined_split_again}")
print(type(joined_split_again))
split[1] = joined_split_again
print(split)
new_split = [split[0] + split[1]]
print(new_split)
chess[1] = new_split
print(chess)


