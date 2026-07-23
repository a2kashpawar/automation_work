```python
# This script will create a personalized "secret message" based on your input!

# 1. Ask the user for a secret word or phrase.
secret_phrase = input("Enter your secret word or phrase: ")

# 2. Ask for a simple number to use as an "encryption key".
# We use int() to convert the input (which is text) into a whole number.
shift_key = int(input("Enter a small whole number (e.g., 1, 2, 3) for the secret key: "))

# 3. Create an empty string to store our "encoded" message.
encoded_message = ""

# 4. Loop through each character in the secret phrase.
for char in secret_phrase:
    # Check if the character is an alphabet letter.
    if 'a' <= char <= 'z':
        # Convert character to its ASCII number, shift it, and convert back.
        # '% 26' ensures it wraps around 'z' back to 'a' if it goes too far.
        shifted_char_code = (ord(char) - ord('a') + shift_key) % 26 + ord('a')
        encoded_message += chr(shifted_char_code)
    elif 'A' <= char <= 'Z':
        # Do the same for uppercase letters.
        shifted_char_code = (ord(char) - ord('A') + shift_key) % 26 + ord('A')
        encoded_message += chr(shifted_char_code)
    else:
        # If it's not a letter (like space, number, or symbol), keep it as is.
        encoded_message += char

# 5. Print the original and the "secret" message.
print(f"\nYour original message: {secret_phrase}")
print(f"Your secret code (with key {shift_key}): {encoded_message}")

# 6. Add a fun ending message.
print("\nRemember your key to decode it!")
```
