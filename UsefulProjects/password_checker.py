"""
Author: Romain Dzeinse
Date: 06/7/24
Objective: Create an algorithm that validates passwords on making sure it includes all the required stuff
filename: password_checker.py
"""


def check_password(password):
    """
    This is the pseudocode:
    - Create function with parameters
    - Create variable for all the required things a password needs to have
    - Check if password is correct length
    - Check if password has numbers
    - Check if password has (an) uppercase letter(s)
    - Check if password has (a) lowercase letter(s)
    - Check if password has special characters
    - Check if password doesn't have any of the unallowed special characters
    :param password: this it the password attempt
    :return: return true, if it meets all req, or false if it doesn't meet at least one req
    """
    special_characters = "!@#$%^&*()"
    meets_req = False
    unallowed_spec_chars = " _+<>?:{}|\\"

    # Check if the password has at least 10 characters
    if len(password) >= 10:
        has_number = False

        # Go through the password string and if you encounter a number make has_number equal true and break
        for number in password:
            # If this character is a number make has_number = True and exit the for loop
            if number.isnumeric():
                has_number = True
                break

        # Go through password and when you see an uppercase letter, change
        # the value of variable below and break
        has_upper_case = False
        for u_case in password:
            if u_case.isupper():
                has_upper_case = True
                break

        # Go through password and when you see a lowercase letter, change to true and break
        has_lower_case = False
        for l_case in password:
            if l_case.islower():
                has_lower_case = True
                break

        # Go through password and when you see an unallowed character, change
        # the has_unallowed_char variable to True and break
        has_unallowed_char = False
        for char in password:
            if char in unallowed_spec_chars:
                has_unallowed_char = True
                break

        # In order for this function to return true, there needs to be:
        # 1.a number 2.an uppercase 3.a lowercase 4.and no unallowed special characters
        if has_number and has_upper_case and has_lower_case and not has_unallowed_char:
            return True
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    print("This is a password checker, please choose a password with these requirements:")
    print("1. a number\n" + "2. an uppercase\n" + "3. a lowercase\n" + "4. and no unallowed special characters")
    my_password = "Romain123!@"
    user_password = input("\nEnter a password: ")
    if check_password(user_password):
        print("\033[32mValid password!\033[0m")
    else:
        print("\033[31mInvalid password!\033[0m")
