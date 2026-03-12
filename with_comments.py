# Import the random module to generate random numbers
import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)

# Variable to store user's guess
a = -1

# Variable to count number of attempts
guesses = 0

# Loop continues until the user guesses the correct number
while a != n:
    
    # Take input from the user
    a = int(input("Guess the number: "))
    
    # Increase the guess counter
    guesses += 1

    # Check if the guessed number is greater than the actual number
    if a > n:
        print("Enter a lower number please.")

    # Check if the guessed number is smaller than the actual number
    elif a < n:
        print("Enter a higher number please.")

# When the correct number is guessed, the loop ends
print(f"You guessed the number {n} correctly in {guesses} attempts.")


