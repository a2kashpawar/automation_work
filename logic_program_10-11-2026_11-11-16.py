```python
# This script creates a fun, personalized "secret identity" based on your inputs!

# Import the 'random' module to use its functions for making choices.
import random

# Greet the user and ask for their favorite color.
# The input() function gets text (a string) from the user.
favorite_color = input("Hello there! What's your favorite color? ")

# Ask for their favorite animal.
favorite_animal = input("And what's your favorite animal? ")

# Ask for a lucky number. We'll convert it to an integer using int().
# This conversion is important if you want to do math with the number.
lucky_number_str = input("Finally, what's your lucky number? ")
lucky_number = int(lucky_number_str) # Convert the string input to an actual number

# Create a list of possible "secret power" endings.
# A list is an ordered collection of items, enclosed in square brackets [].
power_endings = [
    "of invisibility!",
    "to fly!",
    "to talk to animals!",
    "to create tasty snacks!",
    "of super speed!",
    "to control weather!",
    "to glow in the dark!",
    "to fix anything instantly!",
]

# Randomly choose one power ending from our list.
# random.choice() picks a random item from a list.
chosen_power = random.choice(power_endings)

# Generate a fun "secret name" by combining parts of their inputs.
# We use an f-string (formatted string literal) for easy combining.
# f-strings start with 'f' and allow variables inside curly braces {}.
# .capitalize() makes the first letter uppercase, .upper() makes all letters uppercase.
secret_name = f"The {favorite_color.capitalize()} {favorite_animal.upper()}-BOT"

# Create a "power level" based on their lucky number.
# The modulo operator (%) gives the remainder of a division.
# This ensures the power_level is always between 0 and 9.
power_level = lucky_number % 10

# Print the final results to the user!
print("\n--- Your New Secret Identity ---") # \n creates a new line for better formatting
print(f"Your Secret Name is: {secret_name}!")
print(f"You have the amazing superpower {chosen_power}")
print(f"And your power level is: {power_level} out of 9!")
print("\nRemember your identity and keep practicing Python!")
```
