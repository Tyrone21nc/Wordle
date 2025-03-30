"""
Author: Romain Dzeinse
Date: 4/23/24
Objective: Call your Black Jack file in the file
"""

# The syntax of calling a function from another file to one file is here
# from file_name import the_function
from BlackJack import blackjack
# What this does, is it calls imports the blackjack function from the BlackJack file and prints it
print(blackjack())


# We could have decided to import the entire file too, like this:
import BlackJack
# What this does is it goes in the file we just imported, and then
# we use the dot notation to get the function name
print(BlackJack.blackjack())

