"""
Author: Romain Donfack Dzeinse
Date: 12/24/23
Objective: To create a food ordering program
Inspiration: I like getting food from Los Pollos Hermanos, with my best pal, Jesse Pinkman
"""

TAB = "\t"
line = "|"
basic = "basic"
westside = "westside"
new_mexico = "new mexico"
albuquerque = "albuquerque"
south_value = "south valley"
taos = "taos"
menu = {}
los_pollos_hermanos = "Los Pollos Hermanos!"

print("Welcome to", los_pollos_hermanos), print()
see_menu = input("Press ENTER to see the menu: ")
if see_menu == "":
    print("This is the Pollos Burritos Menu!")

    menu = {
        "basic": 2.49,
        "westside": 2.79,
        "new mexico": 3.09,
        "albuquerque": 3.69,
        "south valley": 3.89,
        "taos": 3.69,
    }

    for i in menu:
        if i == basic:
            print(basic, ": $", menu.get(basic))
        elif i == westside:
            print(westside, ": $", menu.get(westside))
        elif i == new_mexico:
            print(new_mexico, ": $", menu.get(new_mexico))
        elif i == albuquerque:
            print(albuquerque, ": $", menu.get(albuquerque))
        elif i == south_value:
            print(south_value, ": $", menu.get(south_value))
        elif i == taos:
            print(taos, ": $", menu.get(taos))
    print()
    the_order = input("What would you like to eat? (QUIT if done ordering): ").upper()
    the_food = []
    the_cost = 0.00
# First time you want to order your food
    while the_order.upper() != "QUIT":
        if the_order in menu:
            the_food.append(the_order)
            the_cost += menu.get(the_order)
        else:
            while the_order not in menu:
                the_order = input("Enter valid food name! What would you like to eat?: ")
            if the_order in menu:
                the_food.append(the_order)
                the_cost += menu.get(the_order)
        the_order = input("What else would you like to eat? (QUIT if done ordering) ")
# Then ask if they want to pay yet
    print("Thank you very much for shopping at Los Pollos Hermanos.")
    print()
    print("You ordered: ")
    length = len(the_food)
    for i in range(len(the_food)):
        print(i+1, ": " + str(the_food[i]))
    print("Your balance is, ", "$" + str(the_cost))
    order_more = input("Will that be all? (yes or no): ")

    if order_more.lower() == "no":
        while order_more.upper() != "QUIT":
            order_more = input("What more would you like to eat? (QUIT to exit): ")
            if order_more in menu:
                the_food.append(order_more)
                the_cost += menu.get(order_more)
            else:
                tries = 5
                while order_more not in menu and tries > 0 and order_more.upper() != "QUIT":
                    order_more = input("Enter valid food name! What more would you like to eat? (QUIT again to exit): ")
                    if order_more in menu:
                        the_food.append(order_more)
                        the_cost += menu.get(order_more)
                    else:
                        tries -= 1
        the_order = input("Is there anything else you would like to eat? (QUIT if done ordering) ")

    elif order_more.lower() == "yes":
        print("Bye!"), print("Come back later")
    if order_more.upper() == "QUIT":
        for i in range(len(the_food)):
            print(i+length, ": " + str(the_food[i]))
        print("Your balance is, ", "$" + str(round(the_cost)))

    # This menu in a well formatted form
    # for i in range(2):
    #     print(line, TAB, TAB, TAB, "Pollos Burritos Menu", TAB, TAB, TAB, line)
else:
    print("Follow directions! No menu for you :O ")
    print()
    the_order = input("What would you like to eat? (QUIT if done ordering): ")
    if the_order.upper() != "QUIT":
        print("Nah, I'm just playing, I don't care what you want to eat. No food for you!!")


