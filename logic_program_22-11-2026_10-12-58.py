```python
# This is a "Secret Code Generator" script for beginners.
# It takes a word from you and scrambles it into a simple 'secret' code.

import random # We need the 'random' module to shuffle the letters.

print("Welcome to the Secret Code Generator!")
print("I can take any word and turn it into a simple, scrambled code.")

# Ask the user for a word to encode.
# input() waits for the user to type something and press Enter.
original_word = input("Please type a word you want to encode: ")

# Convert the word into a list of characters.
# This makes it easy to shuffle the letters.
list_of_letters = list(original_word)

# Shuffle the list of letters randomly.
# random.shuffle() rearranges the items in a list in a random order.
random.shuffle(list_of_letters)

# Join the shuffled letters back together to form a new string.
# "".join() combines all elements of a list into a single string.
# The "" means it joins them without any character in between.
secret_code = "".join(list_of_letters)

# Print the original word and its secret code.
print(f"\nYour original word was: '{original_word}'") # f-strings are a modern way to format strings.
print(f"Your secret code is:   '{secret_code}'")

print("\nKeep your secret code safe!")
# End of the script.
```
