```python
# Import the random module to generate a random number
import random

# --- The "Secret Spinner" Script ---

# 1. Get a word or phrase from the user
# The input() function asks the user for text and stores it in the 'original_text' variable.
original_text = input("Enter a short word or phrase to 'spin': ")

# 2. Generate a random 'spin' amount
# random.randint(min, max) generates a random integer within the specified range (inclusive).
# This number determines how much each character will "spin" or shift.
spin_amount = random.randint(1, 7) # Spin by 1 to 7 positions

# 3. Prepare an empty list to build the 'spun' (modified) text
spun_characters = []

# 4. Go through each character in the user's input
# A 'for' loop iterates over each item (character) in the 'original_text' string.
for char in original_text:
    # Convert the character to its ASCII (or Unicode) numerical value
    # ord() returns the integer that represents a character.
    char_code = ord(char)

    # Apply the 'spin' by adding the spin_amount to the character's code
    # This effectively shifts the character to a new one.
    spun_char_code = char_code + spin_amount

    # Convert the new numerical value back to a character
    # chr() returns the character that represents a given integer code.
    spun_char = chr(spun_char_code)

    # Add the newly spun character to our list
    spun_characters.append(spun_char)

# 5. Join all the characters in the list back into a single string
# The .join() method concatenates all strings in an iterable (like our list)
# using the string it's called on as a separator. Here, "" means no separator.
spun_text = "".join(spun_characters)

# 6. Display the original and the spun text, along with the 'spin key'
print("\n--- Your Spun Text ---")
print("Original:", original_text)
print("Spun Text:", spun_text)
# The 'spin_amount' is the key needed to "unspin" the text later.
print("Spin Key (to decode):", spin_amount)
print("----------------------")
```
