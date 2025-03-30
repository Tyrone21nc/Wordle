"""
File: temp_converter_part2.py
Author: Romain Donfack Dzeinse
objective: It's the same as the last temperature converter, only difference is, there's now kelvin
"""

from_what = input("Do you want to convert from \u001b[32mcelsius\033[0m or from \u001b[32mfahrenheit\033[0m or from "
                  "\u001b[32mkelvin\033[0m: ").lower()
to_convert_to = input("What do you want to convert to? ").lower()
far = "fahrenheit"
cel = "celsius"
kel = "kelvin"
if from_what == cel:
    degree_in_celsius = float(input(f"Enter the \033[1mdegree\033[0m you want to convert to {to_convert_to}: "))
    if to_convert_to == far:
        to_fahrenheit = (degree_in_celsius * 9 / 5) + 32
        print(f"\u001b[34m{to_fahrenheit} \033[1m°F")
    elif to_convert_to == kel:
        to_kelvin = 273.15 + degree_in_celsius
        print(f"\u001b[34m{to_kelvin} \033[1mK")
    elif from_what == to_convert_to:
        print("Can't convert to the same thing")
elif from_what == far:
    degree_in_fahrenheit = float(input(f"Enter the \033[1mdegree\033[0m you want to convert to {to_convert_to}: "))
    if to_convert_to == cel:
        to_celsius = (degree_in_fahrenheit-32) * 5/9
        print(f"\u001b[34m{to_celsius} \033[1m°C")
    elif to_convert_to == kel:
        to_kelvin = 255.372 + degree_in_fahrenheit
        print(f"\u001b[34m{to_kelvin} \033[1mK")
    elif from_what == to_convert_to:
        print("Can't convert to the same thing")
elif from_what == kel:
    degree_in_kelvin = float(input(f"Enter the \033[1mdegree\033[0m you want to convert to {to_convert_to}: "))
    if to_convert_to == cel:
        to_celsius = degree_in_kelvin - 273.15
        print(f"\u001b[34m{to_celsius} \033[1m°C")
    elif to_convert_to == far:
        to_fahrenheit = degree_in_kelvin - 459.67
        print(f"\u001b[34m{to_fahrenheit} \033[1m°F")
    elif from_what == to_convert_to:
        print("Can't convert to the same thing")
