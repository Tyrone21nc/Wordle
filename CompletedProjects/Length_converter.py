"""
File: length_converter.py
Author: Romain Donfack Dzeinse
objective: Converting centimeters to inches and vice versa
"""

if __name__ != "main":
    from_what = input("What do you want to convert from (feet or centimeters): ").lower()
    f = "feet"
    centi = "centimeters"
    if from_what == f:
        value_of_feet = float(input("What is the value in feet x.y  ->>5.09->>5.02: "))
        to_centimeters = round(value_of_feet * 30.48, 1)
        print(f"{to_centimeters} cm")
    elif from_what == centi:
        value_of_centi = float(input("What is the value in centimeters: "))
        to_feet = round(value_of_centi / 30.48, 2)
        print(f"{to_feet} ft")



