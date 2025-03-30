import csv

with (open("My_csv_file.csv") as file):
    the_data = file.read()
    the_data = the_data.split("\n")

print("\033[7m\033[41mPrinting the header\033[0m... ")
the_data[0] = the_data[0].split(",")
for i in range(len(the_data[0])):
    print("\033[7m|", the_data[0][i], end="  |\033[0m\n")
print()
print()
print("\033[7m\033[41mPrinting the remainders\033[0m... ")


def print_list_of_foods():
    color_count = 0
    final_len = len("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    colors = ["\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m", "\033[40m"]
    for i in the_data[1:]:
        i = i.split(",")
        another_counter = 0
        for j in i:
            word_len = final_len - len(j)
            words_space = " " * word_len
            if another_counter == 0:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(f"|{colors[color_count]}", j, end=f"{words_space}\033[0m|\n")
            elif another_counter == 3:
                print(f"|{colors[color_count]}", j, end=f"{words_space}\033[0m|\n")
                print("|___________________|")
                print()
            else:
                print(f"|{colors[color_count]}", j, end=f"{words_space}\033[0m|\n")
            another_counter += 1
        color_count += 1

        print()
    return ""


print(print_list_of_foods())


def draw_happy_face():
    color_count = 0
    other_len = len("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")

    colors = ["\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m", "\033[40m"]
    for i in the_data[1:2]:
        i = i.split(",")
        another_counter = 0
        for j in i:
            word_len = other_len - len(j)
            words_space = " " * word_len
            more_space = " " * len(j)
            if another_counter == 0:
                print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|                           |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                print(f"|{colors[color_count]}", more_space, end=f"{words_space}\033[0m|                     |{colors[color_count]}                      \033[0m|\n")
            elif another_counter == 3:
                print(f"|{colors[color_count]}", more_space, end=f"{words_space}\033[0m|                     |{colors[color_count]}                      \033[0m|\n")
                print("|___________________|                           |___________________|")
                print()
            else:
                print(f"|{colors[color_count]}", more_space, end=f"{words_space}\033[0m|                     |{colors[color_count]}                      \033[0m|\n")
            another_counter += 1
        color_count += 1

        print()
        print(f"                      \\{colors[0]}_______________________\033[0m/")
        print(f"                       \\{colors[0]}_|_|_|_|_|_|_|_|_|_|_\033[0m/")

        return ""


print(draw_happy_face())
