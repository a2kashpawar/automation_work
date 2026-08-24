```python
# A simple "Fortune Teller" script that uses your inputs!

import random # This module helps us pick a random element for our fortune

# --- Get information from the user ---

# Ask for the user's name and store it in a variable
user_name = input("Hello there! What's your name? ")

# Ask for a lucky number, storing it as text first
lucky_number_str = input("What's your favorite lucky number? ")

# Try to convert the lucky number string to an actual number (integer)
# If it's not a valid number, we'll just use a default value (7)
try:
    lucky_number = int(lucky_number_str)
except ValueError:
    print("Hmm, that wasn't a number. I'll use 7 as your lucky number!")
    lucky_number = 7

# Ask for a dream destination
dream_destination = input("Imagine a dream place (e.g., 'a moon base', 'an ancient forest'): ")

# Ask for a special talent
special_talent = input("What's a secret special talent you wish you had (e.g., 'flying', 'talking to animals')? ")

# --- Prepare fortune elements ---

# Create a list of possible "twists" for the fortune
fortune_twists = [
    "a surprising encounter",
    "a hidden challenge",
    "a moment of unexpected joy",
    "a valuable lesson learned",
    "a sudden stroke of luck"
]

# Pick one random twist from our list
chosen_twist = random.choice(fortune_twists)

# --- Generate and display the fortune ---

print(f"\n--- Your Custom Fortune, {user_name}! ---") # Use an f-string to easily insert the name

# Start building the fortune, combining user inputs
print(f"On a day when the stars align with your number {lucky_number},")
print(f"you will embark on an adventure to {dream_destination}.")

# Add a conditional statement based on the lucky number
if lucky_number % 2 == 0: # Check if the lucky number is even
    print(f"Your secret talent of {special_talent} will guide you through {chosen_twist} with ease.")
else: # If the lucky number is odd
    print(f"You will discover how your wish for {special_talent} helps you overcome {chosen_twist}.")

print("\nMay your path be filled with wonder!")
print("------------------------------------")
```
