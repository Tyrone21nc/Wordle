# This is a person class
class Person:
    # Below is sort of like the constructor in Java, it's a function. And the parameters are the
    # instance variables. Here we clarify what the instance variables are for when we actually
    # build the user/person below
    def __init__(self, age, weight, height, first_n, last_n):
        self.aga = age
        self.weight = weight
        self.height = height
        self.first_n = first_n
        self.last_n = last_n

    def person_walk(self):
        print()



# In the line below, we are making a Person object by the name of user.
# Now this Person object needs to include all the instance variables of the Person class,
# as we defined in the constructor like function above
user = Person(25, 80, 177, "Tyrone", "Brown")
# first_n is an instance of the Person class
print(user.first_n)








