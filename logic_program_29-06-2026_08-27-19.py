# A unique script to explore ASCII values and characters!
# This script helps you understand how computers represent text.

# --- Part 1: Character to ASCII Value ---

# Get a single character from the user.
# The 'input()' function pauses the script and waits for user text.
user_char = input("Enter a single character (e.g., 'A', '!', '5'): ")

# Check if the user entered exactly one character.
# 'len()' returns the number of items in a sequence (like characters in a string).
if len(user_char) == 1:
    # Convert the character to its integer ASCII (ordinal) value.
    # 'ord()' is a built-in Python function that does this.
    char_ascii_value = ord(user_char)
    # Print the result using an f-string for easy formatting.
    print(f"The ASCII value of '{user_char}' is: {char_ascii_value}")
else:
    # If the input was not a single character, inform the user.
    print("Invalid input for character lookup. Please enter only one character.")


# Print a separator line for better readability between parts.
print("-" * 30)


# --- Part 2: ASCII Value to Character ---

# Get an integer ASCII value from the user.
user_ascii_str = input("Enter an ASCII integer value (e.g., 65 for 'A', 33 for '!'): ")

try:
    # Try to convert the user's input string to an integer.
    # 'int()' converts a string to an integer. This can fail if the input isn't a number.
    user_ascii_int = int(user_ascii_str)

    # Basic validation: check if the value is within common printable ASCII range.
    # ASCII values 32-126 usually represent visible characters.
    if 32 <= user_ascii_int <= 126:
        # Convert the integer ASCII value back to its character.
        # 'chr()' is a built-in Python function that does this.
        ascii_char = chr(user_ascii_int)
        # Print the result.
        print(f"The character for ASCII value {user_ascii_int} is: '{ascii_char}'")
    else:
        # Inform the user if the value is outside the common range.
        print("This ASCII value is outside the common printable range (32-126).")
        print("Python can handle broader Unicode, but we'll stick to common ASCII for this example.")

except ValueError:
    # Handle cases where the user didn't enter a valid number (e.g., typed "hello").
    # A 'ValueError' occurs when 'int()' can't convert the string.
    print("Invalid input for ASCII value lookup. Please enter a whole number.")

# A concluding message.
print("\nThank you for exploring ASCII with this script!")
