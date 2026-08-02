```python
# This script generates a unique, magical "daily mantra" just for you!
# It combines your name with a random positive word and a special number.

import random # We need this to pick a random word

# --- Get input from the user ---
# The input() function asks the user for information.
user_name = input("What's your first name? ")
lucky_number_str = input("Enter a small lucky number (e.g., 1-9): ")

# --- Process the input ---
# Convert the lucky number from a string to an integer
# This allows us to do math with it later.
lucky_number = int(lucky_number_str)

# Define a list of positive words
# Lists are ordered collections of items.
positive_words = ["radiant", "brave", "joyful", "brilliant", "harmonious", "peaceful", "strong", "wise"]

# Choose a random word from our list
# random.choice() picks one item at random.
chosen_word = random.choice(positive_words)

# --- Create the unique mantra ---
# We'll combine parts of the user's input with our chosen word and a calculation.
# f-strings (formatted string literals) make it easy to embed variables directly.
# .capitalize() makes the first letter of the word uppercase.
# user_name[0] gets the first letter of the name.
# lucky_number * 3 does a simple multiplication.
daily_mantra = f"I am {chosen_word.capitalize()} {user_name[0].upper()}{lucky_number * 3}!"

# --- Display the mantra ---
print("\n--- Your Magical Daily Mantra ---")
print(daily_mantra)
print("Say it with confidence today! ✨")

```
