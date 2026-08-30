```python
# A unique Python script for beginners: The "Letter Shifter"

# This script takes a word and shifts each letter forward in the alphabet
# by a user-defined number, wrapping around from 'Z' to 'A'.

# First, we ask the user for a word.
# The 'input()' function gets text from the user.
original_word = input("Enter a word (e.g., 'hello' or 'PYTHON'): ")

# Next, we ask how many positions to shift each letter.
# We convert the input to an integer using 'int()'.
shift_amount_str = input("Enter a shift number (e.g., 1 for 'a'->'b', or 3 for 'a'->'d'): ")
# It's good practice to make sure the input is a valid number.
# For simplicity in a beginner script, we'll assume valid input for now.
shift_amount = int(shift_amount_str)

# We'll build the new word character by character.
shifted_word = ""

# Loop through each letter in the original word.
# 'for char in original_word:' iterates over each character directly.
for char in original_word:
    # Check if the character is an alphabet letter.
    if 'a' <= char <= 'z':
        # Convert character to its ASCII value (e.g., 'a' is 97).
        char_code = ord(char)
        # Apply the shift.
        # We subtract 'ord('a')' to make 'a' equal 0, 'b' equal 1, etc.
        # Then we add the shift, and use '%' (modulo) 26 to wrap around
        # (since there are 26 letters in the alphabet).
        # Finally, add 'ord('a')' back to get the new ASCII value.
        shifted_code = ((char_code - ord('a') + shift_amount) % 26) + ord('a')
        # Convert the new ASCII value back to a character.
        shifted_char = chr(shifted_code)
    elif 'A' <= char <= 'Z': # Handle uppercase letters similarly
        char_code = ord(char)
        shifted_code = ((char_code - ord('A') + shift_amount) % 26) + ord('A')
        shifted_char = chr(shifted_code)
    else:
        # If it's not a letter (e.g., a space, number, or symbol), keep it as is.
        shifted_char = char

    # Add the shifted (or original) character to our new word.
    shifted_word += shifted_char

# Print the original and the new, shifted word.
print(f"\nOriginal word: {original_word}") # f-string for easy formatting
print(f"Shifted word:  {shifted_word}")

print("\nTask complete! Try it with different words and shift numbers.")
```
