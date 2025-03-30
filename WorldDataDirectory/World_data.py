import csv
with open("world_data.csv") as file:
    data = file.read().split("\n")
second = data[0]

first = second.split(",")
# print(first)
data = data[1:]
data.remove("")

for i in range(len(data)):
    data[i] = data[i].split(",")

print(data[0])


def type_indeces(the_first):
    indece_of_stuff = {}
    # For loop sets the indece to the word in a dictionary
    for i in range(len(the_first)):
        indece_of_stuff[the_first[i]] = i
    # After setting the word sans stuff, it now prints it below
    for i in indece_of_stuff.keys():
        print(f"{i}: {indece_of_stuff[i]}")


type_indeces(first)


def avg_age_of_men(the_data):
    sum_of_ages_for_men = 0
    total_num_of_men = 0
    for i in range(len(the_data)):
        for j in range(len(the_data[i])):
            if the_data[i][j] == "Male":
                total_num_of_men += 1
                sum_of_ages_for_men += int(the_data[i][0])
    avg = sum_of_ages_for_men/total_num_of_men
    return avg


def perc_of_ppl_wth_bach(the_data):
    # According to a Google Search, to calculate percentage of people with
    # a BS among a population, you need to:
    # Divide total num of ppl with BS by num of ppl ages 25 or higher
    with_bach = 0
    ppl_25yrs_or_older = 0
    for i in range(len(the_data)):
        for j in range(len(the_data[i])):
            if the_data[i][j] == "Bachelors":
                with_bach += 1
            if int(the_data[i][0]) >= 25:
                ppl_25yrs_or_older += 1
    percentage = round(with_bach / ppl_25yrs_or_older, 3)
    return percentage








