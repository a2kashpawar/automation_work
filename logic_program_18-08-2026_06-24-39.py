```python
# This script generates a simple text art pattern based on your input!

# 1. Get input from the user.
# We ask for a single character that will be used to build the pattern.
# The 'input()' function waits for the user to type something and press Enter.
pattern_char = input("Enter a single character for your pattern (e.g., *, #, @): ")

# We then ask for the maximum width/length of the pattern.
# 'input()' always returns a string, so we use 'int()' to convert it to a whole number.
max_length_str = input("Enter the maximum length for the pattern (a number, e.g., 5, 10): ")
max_length = int(max_length_str)

print("\n--- Your Custom Pattern ---")

# 2. Create the "growing" part of the pattern.
# A 'for' loop is used to repeat a block of code a specific number of times.
# 'range(1, max_length + 1)' generates numbers from 1 up to 'max_length' (inclusive).
for current_length in range(1, max_length + 1):
    # In Python, you can multiply a string by an integer to repeat it!
    # Example: "*" * 3 results in "***"
    print(pattern_char * current_length)

# 3. Create the "shrinking" part of the pattern (makes it symmetrical).
# 'range(max_length - 1, 0, -1)' starts from 'max_length - 1', goes down to 1,
# and '-1' means it decrements by 1 in each step.
for current_length in range(max_length - 1, 0, -1):
    print(pattern_char * current_length)

print("--- Pattern Complete ---")

# This script demonstrates:
# - Getting user input ('input()')
# - Converting data types ('int()')
# - Using variables
# - Repeating actions with a 'for' loop
# - String multiplication (a neat Python feature!)
```
