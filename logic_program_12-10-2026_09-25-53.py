```python
import random # Import the 'random' module to generate random numbers

# Print a welcome message to the user
print("Welcome to the Mystery Number Game!") 
print("I'm thinking of a number between 1 and 5...")

# Generate a random integer between 1 and 5 (inclusive)
secret_number = random.randint(1, 5) 

# Get the user's guess using input() and convert it to an integer
# The int() function is used to turn the text input into a whole number
try:
    user_guess = int(input("What's your guess? ")) 

    # Check if the user's guess matches the secret number
    if user_guess == secret_number:
        print("Congratulations! You guessed it!") # Message for a correct guess
    else:
        # Message for an incorrect guess, showing the correct number
        print(f"Nope! The secret number was {secret_number}.") 
except ValueError:
    # Handle cases where the user doesn't enter a valid number
    print("That's not a valid number! Please guess a whole number.")

print("Thanks for playing!") # Farewell message
```
