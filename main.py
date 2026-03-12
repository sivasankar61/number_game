import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

guess = 0
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Try a lower number.")
    elif guess < number:
        print("Try a higher number.")
    else:
        print("Correct!")

print("You guessed the number", number, "in", attempts, "attempts.")