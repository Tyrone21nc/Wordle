import random

# A list of 5-letter words (this should be expanded in a real game)
words = ["apple", "grape", "berry", "mango", "peach", "lemon", "plumb"]

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'


def get_random_word():
    return random.choice(words)


def display_guess(guess, target):
    result = []
    for i in range(len(guess)):
        if guess[i] == target[i]:
            result.append(f"{GREEN}{guess[i]}{RESET}")  # Correct letter in correct position
        elif guess[i] in target:
            result.append(f"{YELLOW}{guess[i]}{RESET}")  # Correct letter in wrong position
        else:
            result.append(f"{RED}{guess[i]}{RESET}")  # Incorrect letter
    return " ".join(result)


def wordle():
    target_word = get_random_word()
    attempts = 6
    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")

    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 5 or guess not in words:
            print("Invalid word. Make sure it's a 5-letter word from the list.")
            continue

        print(display_guess(guess, target_word))

        if guess == target_word:
            print("Congratulations! You've guessed the word correctly.")
            break

        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{target_word}'.")


# Run the game
wordle()
