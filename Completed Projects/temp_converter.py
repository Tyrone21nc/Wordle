"""
File: temp_converter_part2.py
Author: Romain Donfack Dzeinse
objective: It's the same as the last temperature converter, only difference is, there's now kelvin
"""

what_type = input("Do you want to convert from celsius or from fahrenheit: ").lower()
if what_type == "celsius":
    degree_in_celsius = float(input("Enter the degree you want to convert to fahrenheit: "))
    to_fahrenheit = (degree_in_celsius * 9 / 5) + 32
    print(to_fahrenheit)
elif what_type == "fahrenheit":
    degree_in_fahrenheit = float(input("Enter the degree you want to convert to celsius: "))
    to_celsius = (degree_in_fahrenheit-32) * 5/9
    print(to_celsius)


