```python
# This script generates a simple, repeating text pattern based on user input.

# Ask the user for a single character they want to use in the pattern.
# The input() function gets text from the user.
pattern_char = input("Enter a single character (e.g., *, #, @): ")

# Ask the user for a small whole number to determine the pattern's size.
# The int() function converts the user's text input into a whole number.
pattern_size = int(input("Enter a small whole number (e.g., 5, 10): "))

print("\n--- Your Custom Pattern ---")

# --- Part 1: Expanding the pattern ---
# This loop will print lines of increasing length.
# range(1, pattern_size + 1) generates numbers from 1 up to and including pattern_size.
for i in range(1, pattern_size + 1):
    # Print the chosen character 'i' times.
    # String multiplication (pattern_char * i) repeats the string.
    print(pattern_char * i)

# --- Part 2: Contracting the pattern ---
# This loop will print lines of decreasing length, mirroring the expansion.
# range(pattern_size - 1, 0, -1) generates numbers from pattern_size-1 down to 1.
# The third argument, -1, tells range to count backwards.
for i in range(pattern_size - 1, 0, -1):
    # Print the chosen character 'i' times.
    print(pattern_char * i)

print("--- Pattern Complete! ---")
```
