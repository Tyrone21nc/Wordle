print("\033[7mWelcome to your body!\033[0m")
with open("Food_forCSVfile/user_info.csv") as file:
    data = file.readlines()


def printing_user_stuff():
    heading = data[0].strip("\n").split(", ")
    heading.append("BMI")
    for i in range(len(data)):
        data[i] = data[i].strip("\n").split(", ")
    print()
    for i in data[1:]:
        for j in range(len(i) + 1):
            if j == 0:
                bmi = float(i[1]) // (float(i[2]) / 100) ** 2
                i.append(bmi)
            print(f"{heading[j]}: {i[j]}")
        print()
    return data


def what_you_eat():
    user_consumes = []
    food = []
    drink = []
    print("We are about to compute your meal")
    consume = input("What do you consume and drink in a day:\n"
                    "food.chicken drink.mountain dew\n>>> ")
    while "quit" not in consume:
        consume = consume.split(".")
        if len(consume) > 1:
            if "food" in consume:
                food.append(consume[1])
            elif "drink" in consume:
                drink.append(consume[1])
            if "food" in consume or "drink" in consume:
                user_consumes.append(consume[1])
        consume = input(">>> ")
    return food, drink, user_consumes


def get_names(the_data):
    names = []
    weights = []
    heights = []
    w_goals = []
    for i in the_data:
        for j in range(len(i)):
            if j == 0:
                names.append(i[j])
            elif j == 1:
                weights.append(i[j])
            elif j == 2:
                heights.append(i[j])
            elif j == 3:
                w_goals.append(i[j])

    return names, weights, heights, w_goals


for i in range(len(data)):
    data[i] = data[i].strip("\n").split(", ")

# fo, dr, use_con = what_you_eat()
stuff = a, b, c, d = get_names(data)
print()

# print(stuff)





# count = 0
# for n in a:
#     if count == 1 and n != "Person Name":
#         print(f"\033[7m{n}\033[0m", end=" ")
#     count += 1
# count = 0
# for w in b:
#     if count == 1 and w != "Weight(kg)":
#         print(f"\033[7m{w}\033[0m", end=" ")
#     count += 1
# count = 0
# for h in c[1:]:
#     if count == 1 and h != "Height(cm)":
#         print(f"\033[7m{h}\033[0m", end=" ")
#     count += 1
# count = 0
# for w_g in d[1:]:
#     if count == 1 and w_g != "Weight Goal":
#         print(f"\033[7m{w_g}\033[0m")
#     count += 1


import random

# Function to generate a random name
def generate_random_name():
    first_names = ['John', 'Alice', 'Bob', 'Emma', 'Michael', 'Sophia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random information about a person


def generate_random_info():
    age = random.randint(18, 80)
    country = random.choice(['USA', 'Canada', 'UK', 'Australia', 'Germany'])
    occupation = random.choice(['Engineer', 'Teacher', 'Doctor', 'Artist', 'Programmer'])
    return age, country, occupation

# Generate random name and information
# name = generate_random_name()


def display():
    # Display the table
    name = generate_random_name()
    age, country, occupation = generate_random_info()
    print("\033[7mPerson Information:\033[0m")
    print("+----------------+-------------------------------------+")
    print("|\033[7m\033[31mName            \033[0m| " + f"\033[31m{name.ljust(36)}\033[0m" + "|")
    print("|\033[7m\033[32mAge             \033[0m| " + f"\033[32m{str(age).ljust(36)}\033[0m" + "|")
    print("|\033[7m\033[33mCountry         \033[0m| " + f"\033[33m{country.ljust(36)}\033[0m" + "|")
    print("|\033[7m\033[34mOccupation      \033[0m| " + f"\033[34m{occupation.ljust(36)}\033[0m" + "|")
    print("+----------------+-------------------------------------+")


display()


def another_display():
    name = generate_random_name()
    age, country, occupation = generate_random_info()
    print("\033[7mPerson Information:\033[0m")
    print("+----------------+-------------------------------------+")
    print("|\033[7m\033[31mName            \033[0m| " + f"\033[7m\033[31m{name.ljust(36)}\033[0m" + "|")
    print("|\033[7m\033[32mAge             \033[0m| " + f"\033[7m\033[32m{str(age).ljust(36)}\033[0m" + "|")
    print("|\033[7m\033[33mCountry         \033[0m| " + f"\033[7m\033[33m{country.ljust(36)}\033[0m" + "|")
    print("|\033[7m\033[34mOccupation      \033[0m| " + f"\033[7m\033[34m{occupation.ljust(36)}\033[0m" + "|")
    print("+----------------+-------------------------------------+")


another_display()



