```python
# This script generates a unique, simple ASCII art pattern based on user input.

# Ask the user for a single character to build the pattern with.
# The 'input()' function gets text from the user.
pattern_char = input("Enter a single character for your pattern (e.g., #): ")

# Ask for the size of the pattern.
# We need to convert the input text into a whole number using 'int()'.
try:
    pattern_size = int(input("Enter the size of the pattern (a number, e.g., 7): "))
except ValueError:
    # If the user doesn't enter a valid number, set a default size.
    print("Invalid size entered. Using default size: 5.")
    pattern_size = 5

# Ensure the pattern character is just one character.
# If empty, default to '*'. If too long, use only the first character.
if not pattern_char:
    pattern_char = "*"
elif len(pattern_char) > 1:
    pattern_char = pattern_char[0] # Take only the first character

print("\nHere's your custom pattern:")

# Loop to create the top half of the diamond-like pattern.
# 'range(1, pattern_size + 1)' goes from 1 up to 'pattern_size'.
for i in range(1, pattern_size + 1):
    # Print leading spaces to center the pattern.
    # The number of spaces decreases as 'i' increases.
    print(" " * (pattern_size - i) + (pattern_char + " ") * i)

# Loop to create the bottom half of the diamond-like pattern.
# 'range(pattern_size - 1, 0, -1)' goes from 'pattern_size - 1' down to 1.
for i in range(pattern_size - 1, 0, -1):
    # Print leading spaces.
    print(" " * (pattern_size - i) + (pattern_char + " ") * i)

print("\nPattern generation complete!")
```
