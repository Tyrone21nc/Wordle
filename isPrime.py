"""
    Author: Romain Dzeinse
    Date: 10/23/24
    Description: Determine if a number is a prime number, if not return the next prime number
"""


def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


if __name__ == "__main__":
    user_num = int(input("Enter a number: "))
    user_num += 1
    if is_prime(user_num):      # if the number is prime already
        print("The prime is this % d" % user_num)       # print this then
    else:       # if not prime, loop till you get prime
        while not is_prime(user_num):
            user_num += 1
        print("The next prime number is % d " % user_num)


