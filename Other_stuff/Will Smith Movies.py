"""
Author: Romain Donfack Dzeinse
Date: 1/16/24
Objective: To create a list of Will Smith Movies and organize them by year type
Inspiration: I like Will Smith
"""


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
movie = int(input("Choose the movie you would like to watch by number like 1 or 2 or 3 ...: "))


decade2 = ""
again_movie = ""
if 0 < movie < 100:
    while movie in range(len(WS_movies[decade])+1):  # or (again_movie == "yes" or decade2 != decade):
        if movie in range(len(WS_movies[decade])+1):
            print("You requested for: " + (WS_movies[decade][movie-1]))
        print()
        movie = input("Any other movie you would like to watch? (1  or 2 or 3): ")
        # if movie.lower() == "no":
        #     int(movie)
        #     movie = -1
        # else:
        #     int(movie)
    else:
        print("Exceeded the range of movies for this decade("+decade+")")
        again_movie = input("Would you like to choose another movie in the same decade?: ").lower()
        if again_movie != "no":
            pass
        else:
            decade2 = input("Would you like to choose another decade?: ")






