import random

def GuessGame():
    randomly = random.randint(1,100)
    attempts = 0

    print("Hello, this is the Number Guessing Game!")
    print("I've chosen a random number between 1 and 100, can you guess it?")

    while True:
        try:
            num = int(input("Enter your guess here: "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if num < randomly:
            print("Too low! Try again.")
        elif num > randomly:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
GuessGame()