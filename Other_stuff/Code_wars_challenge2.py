"""
Codewars challenge #2: The latest clock

Prompt: Write a function which receives 4 digits and returns the latest time of
day that can be built with those digits. The time should be in HH:MM format.
Examples:
digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59"

Notes
Result should be a valid 24-hour time, between 00:00 and 23:59.
Every input has a valid answer.
"""


def late_clock(a, b, c, d):
    late_time = [0, 0, 0, 0]
    all_nums = [a, b, c, d]
    if 1 in all_nums:
        late_time[0] = 1
    if 2 in all_nums:
        late_time[0] = 2




new = []
for i in range(4):
    number = int(input("enter a number: "))
    new.append(number)
a, b, c, d = new
print(a, b, c, d)
print(late_clock(a, b, c, d))
