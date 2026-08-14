```python
# A super simple "secret message" encoder/decoder.
# This uses a basic shift cipher (like Caesar cipher) for fun, not for real security!

# First, get the message from the user.
# The input() function gets text. .upper() converts it to all uppercase for simplicity.
original_message = input("Enter your secret message: ").upper()

# This is our "shift" value. Changing this number changes the code.
# A positive number shifts letters forward (e.g., A -> D).
shift_amount = 3

# We'll build the encoded message character by character in this empty string.
encoded_message = ""

# Loop through each character in the original message.
# A 'for' loop lets us process each item one by one.
for char in original_message:
    # Check if the character is an uppercase letter (A-Z).
    # We only want to encode letters, not spaces or punctuation.
    if 'A' <= char <= 'Z':
        # Convert the letter character to its ASCII (numerical) value.
        # Example: ord('A') is 65, ord('B') is 66.
        char_number = ord(char)
        
        # Apply the shift: add the shift_amount to the character's number.
        shifted_number = char_number + shift_amount
        
        # Handle "wrapping" around the alphabet.
        # If the shifted number goes past 'Z' (which is 90),
        # we need to loop it back to the beginning of the alphabet.
        if shifted_number > ord('Z'):
            shifted_number -= 26 # Subtract 26 (the number of letters) to wrap around.
        
        # Convert the shifted number back into a character.
        # Example: chr(68) is 'D'.
        encoded_char = chr(shifted_number)
    else:
        # If the character is not a letter, keep it as it is (e.g., spaces, numbers).
        encoded_char = char
    
    # Add the encoded (or unchanged) character to our full encoded message.
    # The '+=' operator adds the new character to the end of the string.
    encoded_message += encoded_char

# Print both the original and the newly encoded messages.
# f-strings (formatted string literals) are a nice way to embed variables.
print(f"\nOriginal Message: {original_message}")
print(f"Encoded Message:  {encoded_message}")

# CHALLENGE FOR YOU:
# How would you modify this script to DECODE a message,
# given the encoded message and the shift_amount?
# (Hint: You'd need to subtract instead of add, and handle wrapping the other way!)
```
