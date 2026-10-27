# This script generates a simple "lucky number" from your name.

import random # We need this module for random number generation.

# Ask the user to input their name.
user_name = input("What is your name? ")

# Initialize a 'seed' value for our lucky number calculation.
# We start with the length of the name, which adds a unique touch.
lucky_seed = len(user_name)

# Now, let's iterate through each character in the user's name.
for char in user_name:
    # Add the ASCII (numerical) value of each character to our seed.
    # The 'ord()' function gets the numerical value of a character.
    lucky_seed += ord(char)
    # Add a bit of extra randomness to make it less predictable each run.
    lucky_seed += random.randint(1, 10) # Adds a random number between 1 and 10.

# To keep the lucky number in a friendly range (1-100),
# we use the modulo operator (%) and add 1.
# The modulo operator gives the remainder of a division.
final_lucky_number = (lucky_seed % 100) + 1

# Finally, print the personalized lucky number!
# We use an f-string for easy formatting.
print(f"Hello, {user_name}! Your lucky number for today is: {final_lucky_number}")

# Add a small, fun tip based on the generated number using conditional logic.
if final_lucky_number > 75:
    print("Wow, that's a very high lucky number! Expect great things!")
elif final_lucky_number < 25:
    print("A lower lucky number. Perhaps a good day for quiet reflection?")
else:
    print("A balanced lucky number. A good day for anything!")
