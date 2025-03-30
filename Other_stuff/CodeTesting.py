import copy
def func(x, y):
    # base case
    if x < y:
        return x
    # recursive case
    else:
        return func(x - y, y)


# print(func(20, 5))  # 0
print(), print(), print()

x = [1, 2, 3]
y = [4, 5, 6]
z = y
y = x
x = z

x = [1, 2, 3]  # a different [1, 2, 3] list!
y = x
x.append(4)
y.append(5)
z = [1, 2, 3, 4, 5]  # a different list!
x.append(6)
y.append(7)
y = "hello"


def foo(lst):
    lst.append("hello")
    bar(lst)


def bar(myLst):
    print(myLst)


# foo(x)
# foo(z)


# input = [("Mary", 27), ("Joe", 30), ("Ruth", 43), ("Bob", 17), ("Jenny", 22)]
#
# youngPeople = []
#
# for (person, age) in input:
#     if age < 30:
#         youngPeople.append(person)
#     else:
#         print("HAHA " + person + " is too old!")
#
# print("There are " + str(len(youngPeople)) + " young people")


# printing all keys and their values in a dictionary all at once
# input1 = {"Mary": 27, "Joe": 30, "Ruth": 43, "Bob": 17, "Jenny": 22}

# for (person, age) in input1.items():
#     print(person, age)
# print()
# printing all indices in a list all at once, in a single for loop
# input2 = [("Mary", 27), ("Joe", 30), ("Ruth", 43), ("Bob", 17), ("Jenny", 22)]
# for person2, age2 in input2:
#     print(person2, age2)
#
# decade = {
#     "...cheese":["food\t"],
#     "cheese":[]
# }
# theLett = input("Enter a word: ")
# if "...cheese" == theLett or theLett == "cheese":
#     pass
# else:
#     print("The cheese is there")
# thing = decade.get("...cheese")
# print(thing[0], "Something else")
# def fib(n):
#
#     # base case n = 0
#     if n == 0:
#         return 0
#     # base case n = 1
#     elif n == 1:
#         return 1
#     # case n > 1
#     else:
#         return 1 + fib(n-1)
#
# print(fib(5))

# print(1 % 3)  # This will be 1 because 1 goes into 3 0 original_times with remainder 1
# print(2 % 3)  # This will be 2 because 2 goes into 3 0 original_times (2/3) with 2 remaining
# print(3 % 7)  # Same thing here. The remainder will be 3 because 3 goes into 7 0 original_times with 3 remaining

# my_dict = {
#     "Claire": 1,
#     "Eric": 0,
#     100: 3
# }
# if my_dict["Eric"]:
#     print(True)
# if "Eric" in my_dict:
#     print(False)

# other_dict = {
#     1: [1, 2, 3, 6, 7, 10],
#     2: 1,
#     3: 2,
# }
#
# print(len(other_dict[1]))
# print(len("Cheese"))
# print(type("Cheese"))
# print(type(str))
# print()
# a_list = []
# final_list = []
# for i in range(4):
#     a_list.append(i+1)
# final_list = [a_list, a_list, a_list]
# print(final_list)
# final_list[2][2] = 7  # -> that is the same as saying this: a_list[2] = 7 which would result in the same output
# print(final_list)
"""
To avoid changing every reference to a_list in final_list, you can import and use the copy module, like so (import at
 the top):
"""
# print("cheese", "cheese", "cheese", "cheese", "cheese", "cheese")
# print("_________________________________________")
# a_list = []
# final_list = []
# for i in range(4):
#     a_list.append(i + 1)
#
# # Create independent copies using copy.deepcopy()
# final_list = [copy.deepcopy(a_list) for i in range(3)]
#
# print(final_list)
# final_list[2][2] = 7
# print(final_list)

# def get_coordinates():
#     return (3, 4)
#
#
# x, y = get_coordinates()
# print(f"X: {x}, Y: {y}")
#
# # Tuples as dictionary keys
# coordinates_dict = {(1, 2): "Point A", (3, 4): "Point B"}
# print(coordinates_dict[(1, 2)])
#
# # Constant data
# PI = (3.14159,)
# radius = 5
# area = PI[0] * radius**2
# print(f"Area of the circle: {area}")

# my_string = "cheese"
# size_of_string = my_string.__sizeof__()
#
# print(f"Size of the string 'cheese': {size_of_string} bytes")

# word = "cheese", "other cheese"
# print(word)
# print(word[0], len(word[0]))
# print(word[1], len(word[1]))
# print(word[0][0], len(word[0][:5]))

# num_count = 92983
# print(len(str(num_count)))
# print(list(str(num_count)))
# num_count = list(str(num_count))
# length = len(num_count)
# for i in range(1, length+1):
#     print(num_count[length-i])

"""
Testing a lot of code here for the Will smith movie picker
"""
if True:
    no = "no"
    print("Welcome to this Will Smith Movie selector:")
    WS_movies = {
        "... - 1980": ["None"],
        "1980": ["None"],
        "1990": ["Where the Day Takes You", "Made in America", "Six Degrees of Separation", "Bad Boys\t", "Independence Day",
                 "Men in Black (MIB)", "Enemy of the State", "Wild Wild West\t", "", "", ""],
        "2000": ["The Legend of Bagger Vance", "Ali", "MIB 2", "A Closer Walk\t", "Bad Boys 2", "I Robot", "Shark Tale",
                 "Hitch\t", "The Pursuit if Happyness", "I am Legend", "Hancock", "Seven Pounds\t", ""],
        "2010": ["MIB 3", "After Earth", "Anchorman 2: The Legend Continues", "Winter's Tale\t", "Winter's Tale", "Focus",
                 "Concussion", "Suicide Squad\t", "Collateral Beauty", "Bright", "Aladin", "Gemini Man\t", "Spies In Disguise"],
        "2020": ["Bad Boys For Life", "King Richard", "Emancipation", "\t", "", "", "", "\t", "", "", ""],
    }


    for element, year in WS_movies.items():
        # make a variable with all the 2nd indices in it
        if year[0] == "None":
            pass
        print(element, year)
    print()

    """
    The big piece of code down here is to print the movie decade
    ____________________________________________________________
    """
    decade = input("What decade do you want the movie (like or 2000): ")
    if decade in WS_movies:
        the_decade = WS_movies.get(decade)
        if "... - 1980" == decade or decade == "1980":
            print(the_decade)
        else:
            slash = "\t"
            print()
            for i in range(len(the_decade)):
                if slash in the_decade[i]:
                    print(str(i+1) + ": " + the_decade[i])
                else:
                    print(str(i+1) + ": " + the_decade[i], end="\t      ")
    print()
    movie = int(input("Choose the movie you would like to watch by number -> like 1 or 2 or 3 ...: "))
    """
    The big piece of code up here is to print the movie decade
    ____________________________________________________________
    """

    if 0 < movie < 100:
        while movie in range(len(WS_movies[decade])+1):
            print("You requested for: " + (WS_movies[decade][movie - 1]))
            print()
            movie = input("Would you like to watch another movie, type no or the movie number: ")
            if movie.lower() == no:
                new_decade = input("would you like to watch a movie from a different decade? (yes or no) ")
                if new_decade.lower() == "yes":
                    decade = input("What decade do you want the movie in?: ")
                    if decade in WS_movies:
                        the_decade = WS_movies.get(decade)
                        if "... - 1980" == decade or decade == "1980":
                            print(the_decade)
                        else:
                            slash = "\t"
                            print()
                            for i in range(len(the_decade)):
                                if slash in the_decade[i]:
                                    print(str(i + 1) + ": " + the_decade[i])
                                else:
                                    print(str(i + 1) + ": " + the_decade[i], end="\t      ")
                    # Time to ask the new name of the movie again
                    print()
                    movie = int(input("Choose the movie you would like to watch by number -> like 1 or 2 or 3 ...: "))

            elif movie != no:
                print("Exceeded the range of movies for this decade(" + decade + ")")
                again_movie = input("Would you like to choose another movie in the same decade?: ").lower()
                if again_movie != "no":
                    pass
                else:
                    new_decade = input("Would you like to choose another decade? (yes or no): ")
                    if new_decade.lower() == "yes":
                        decade = input("What decade do you want the movie in?: ")
                        if decade in WS_movies:
                            the_decade = WS_movies.get(decade)
                            if "... - 1980" == decade or decade == "1980":
                                print(the_decade)
                            else:
                                slash = "\t"
                                print()
                                for i in range(len(the_decade)):
                                    if slash in the_decade[i]:
                                        print(str(i + 1) + ": " + the_decade[i])
                                    else:
                                        print(str(i + 1) + ": " + the_decade[i], end="\t      ")
                        # Time to ask the new name of the movie again
                        print()
                        movie = int(input("Choose the movie you would like to watch by number -> like 1 or 2 or 3 ...: "))
            else:
                movie = int(movie)










