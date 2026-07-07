```python
# This script draws a simple ASCII art pyramid using a character you choose.

# Get a character from the user to build the pyramid.
# The input() function asks the user for text.
# The .strip() method removes any extra spaces from what the user types.
pyramid_char = input("Enter a single character to build your pyramid: ").strip()

# Check if the user entered nothing. If so, use a default character.
if not pyramid_char:
    print("No character entered. Using '*' as default.")
    pyramid_char = "*"
# If they entered more than one character, just take the first one.
elif len(pyramid_char) > 1:
    print(f"'{pyramid_char}' is too many characters. Using '{pyramid_char[0]}' instead.")
    pyramid_char = pyramid_char[0]

# This variable controls how many layers (rows) the pyramid will have.
num_layers = 5

print("\nHere is your pyramid:")

# This is a 'for' loop, which repeats a block of code a certain number of times.
# 'range(num_layers)' generates numbers from 0 up to (but not including) num_layers.
# So, 'i' will be 0, 1, 2, 3, 4 for a 5-layer pyramid.
for i in range(num_layers):
    # Calculate the number of leading spaces for the current row.
    # We want more spaces at the top, fewer at the bottom, to center the pyramid.
    # String repetition: " " * 3 creates "   ".
    spaces = " " * (num_layers - 1 - i)

    # Calculate the number of characters for the current row.
    # The first row (i=0) has 1 char, second (i=1) has 3 chars, etc.
    # The pattern is (2 * i) + 1 characters per row.
    chars = pyramid_char * ((2 * i) + 1)

    # Print the spaces followed by the characters for the current row.
    # An f-string (formatted string literal) allows embedding variables directly.
    print(f"{spaces}{chars}")

# A simple message at the end.
print("\nEnjoy your ASCII art!")
```
