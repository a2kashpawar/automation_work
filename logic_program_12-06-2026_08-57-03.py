```python
# A simple script to help you practice typing!
# It will show you a word, and you try to type it correctly.

# First, let's get ready with some words to type.
# These are stored in a list.
words_to_practice = ["python", "beginner", "script", "coding", "challenge", "program"]

# We need the 'random' module to pick a word randomly.
import random

# Let's pick one word for you to type this round.
# random.choice() selects an item from a list.
chosen_word = random.choice(words_to_practice)

# Tell the user what to do.
print("\n--- Typing Practice ---")
print(f"Type the following word: '{chosen_word}'")

# Get the user's input.
# The input() function waits for the user to type something and press Enter.
user_typed_word = input("Your turn: ")

# Now, let's check if the user typed it correctly.
# We use an 'if-else' statement to make a decision.
if user_typed_word == chosen_word:
    # This code runs if the words match.
    print("Great job! You typed it correctly!")
else:
    # This code runs if the words do not match.
    # f-strings are a simple way to include variables directly in a string.
    print(f"Oops! You typed '{user_typed_word}', but the correct word was '{chosen_word}'.")
    print("Keep practicing!")

print("\n--- End of Practice ---")

# This script introduces:
# - Comments (lines starting with #) to explain code
# - Variables to store data (like words and user input)
# - Lists to store multiple items (our words_to_practice)
# - Importing modules (like 'random') to add functionality
# - random.choice() to select a random item from a list
# - input() to get text from the user
# - if/else statements for making decisions
# - print() to display messages to the user
# - f-strings for easy text formatting
```
