```python
# This script creates a simple, unique pattern using characters you choose!
# It's designed for beginners to explore input, loops, and string manipulation.

# 1. Ask the user for their favorite character or symbol.
#    The input() function waits for the user to type something and press Enter.
#    Whatever they type is stored as a string in the 'pattern_char' variable.
pattern_char = input("Enter a single character or symbol you like (e.g., *, #, @): ")

# 2. Ask the user how many rows tall they want their pattern to be.
#    We use int() to convert the user's input (which is always a string) into a whole number.
#    This number will control how many times our loop runs.
pattern_height = int(input("How tall should your pattern be (enter a small number, e.g., 5-10)? "))

# 3. Print a friendly message to introduce the pattern.
#    The '\n' creates a new line, making the output cleaner.
print("\nHere's your custom pattern:")

# 4. Use a 'for' loop to repeat an action.
#    The range(1, pattern_height + 1) generates a sequence of numbers:
#    1, 2, 3, ... up to 'pattern_height'.
#    'current_row' will take on each of these values one by one.
for current_row in range(1, pattern_height + 1):
    # 5. Inside the loop, we create the string for the current row.
    #    In Python, you can multiply a string by a number to repeat it!
    #    For example, '*' * 3 results in '***'.
    row_pattern = pattern_char * current_row

    # 6. Print the generated pattern for the current row.
    #    Each time the loop runs, a new line will be printed, building the pattern.
    print(row_pattern)

# 7. Add a closing message after the pattern is complete.
print("\nPattern created successfully! Experiment with different characters and heights.")
```
