```python
# This script creates a simple, fun "secret code" by shifting each letter of a word.
# It's a basic Caesar cipher, a great way to learn about loops and character manipulation!

# Ask the user for a word they want to encode.
# The 'input()' function gets text from the user.
original_word = input("Enter a word to encode (letters only): ").lower() # .lower() converts to lowercase for easier processing.

# Define the shift value. This determines how many places each letter moves.
# For example, a shift of 3 would turn 'a' into 'd', 'b' into 'e', etc.
shift_amount = 3

# We'll build our encoded word character by character.
encoded_word = ""

# Loop through each letter in the original word.
# A 'for' loop is perfect for iterating over sequences like strings.
for char in original_word:
    # Check if the character is an alphabet letter.
    # This avoids trying to shift spaces, numbers, or punctuation.
    if 'a' <= char <= 'z':
        # Get the numerical position of the letter in the alphabet (0 for 'a', 1 for 'b', etc.).
        # 'ord()' gives the ASCII value of a character.
        char_position = ord(char) - ord('a')

        # Apply the shift. We use the modulo operator (%) to "wrap around"
        # the alphabet, so 'z' shifted by 1 becomes 'a'.
        shifted_position = (char_position + shift_amount) % 26

        # Convert the shifted position back to a character.
        # 'chr()' converts an ASCII value back to a character.
        shifted_char = chr(shifted_position + ord('a'))

        # Add the shifted character to our encoded word.
        encoded_word += shifted_char
    else:
        # If it's not a letter, just add it directly without shifting.
        encoded_word += char

# Print the original and encoded words so the user can see the magic!
print(f"\nYour original word: {original_word}")
print(f"Your secret code:   {encoded_word}")
```
