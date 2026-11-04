```python
# A simple script to generate a dynamic, wavy pattern using characters chosen by the user.

# 1. Get input from the user for the two characters they want to use.
# The 'input()' function prompts the user and returns their text.
char1 = input("Enter the first character for your pattern (e.g., '#'): ")
char2 = input("Enter the second character for your pattern (e.g., '*'): ")

# 2. Get input for the length of each pattern segment.
# We use int() to convert the text input (which is always a string) into a whole number.
segment_length_str = input("How long should each repeating segment be? (e.g., 5): ")
segment_length = int(segment_length_str) # Convert the string to an integer

# 3. Get input for how many rows the pattern should have.
num_rows_str = input("How many rows should the pattern have? (e.g., 10): ")
num_rows = int(num_rows_str) # Convert the string to an integer

# Add an empty line for better visual separation before printing the pattern.
print("\nHere is your custom wavy pattern:\n")

# 4. Loop through each row to build and print the pattern.
# 'range(num_rows)' will generate numbers from 0 up to (but not including) num_rows.
for row_number in range(num_rows):
    # Determine the indentation for the current row to create a "wave" effect.
    # The modulo operator (%) gives the remainder of a division.
    # Here, 'row_number % 4' will cycle the indent from 0, 1, 2, 3, 0, 1, 2, 3...
    indent = row_number % 4

    # Start building the pattern string for the current row.
    # String multiplication (' ' * indent) creates a string of 'indent' spaces.
    row_pattern = " " * indent

    # Now, add the alternating characters to the pattern.
    # We'll print 3 segments per row to make sure the pattern is visible.
    for i in range(3): # This loop runs 3 times (for i=0, 1, 2)
        # Check if 'i' is an even number (0 or 2) using the modulo operator.
        if i % 2 == 0:
            # If 'i' is even, add the first character repeated 'segment_length' times.
            # String addition ('+=') appends to the existing string.
            row_pattern += char1 * segment_length
        else:
            # If 'i' is odd (only 1 in this case), add the second character repeated.
            row_pattern += char2 * segment_length

    # Print the completed pattern string for the current row.
    print(row_pattern)

# An encouraging message for the user after the pattern is printed.
print("\nExperiment with different characters and numbers to see new patterns!")
```
