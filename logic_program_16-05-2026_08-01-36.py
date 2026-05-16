```python
# This script creates a simple character-based pyramid.
# It asks the user for a single character and a height, then draws the pyramid using a loop.

# Ask the user to enter a single character they want to use for drawing.
# The `input()` function reads text typed by the user from the console.
draw_char = input("Enter a single character to draw with (e.g., *, #, or @): ")

# Ask the user for the height of the pyramid.
# The `input()` function always returns a string, so we convert it to an integer
# using `int()`. This is necessary for performing mathematical operations later.
pyramid_height = int(input("Enter the height of the pyramid (a small number like 1 to 10): "))

# Calculate the width of the base of the pyramid.
# This helps us correctly center each row.
# For a pyramid of height N, the base has 2*N - 1 characters.
base_width = 2 * pyramid_height - 1

# Loop through each level of the pyramid, starting from the top (level 1) to the base.
# `range(1, pyramid_height + 1)` generates numbers from 1 up to `pyramid_height` (inclusive).
for current_level in range(1, pyramid_height + 1):
    # Calculate the number of characters needed for the current row.
    # A pyramid row `current_level` has `2 * current_level - 1` characters.
    num_chars_in_row = 2 * current_level - 1

    # Calculate the number of spaces needed on each side to center the row.
    # We subtract the characters in the current row from the total `base_width`,
    # then divide by 2. `//` performs integer division (discards any remainder).
    num_spaces_on_side = (base_width - num_chars_in_row) // 2

    # Create the string for the current row.
    # String multiplication (`" " * N` or `char * N`) repeats a string N times.
    # The row consists of spaces on the left, then the drawing characters,
    # then implicit spaces on the right (handled by centering).
    row_string = (" " * num_spaces_on_side) + (draw_char * num_chars_in_row)

    # Print the completed row to the console.
    print(row_string)

# Print a final message to the user, indicating that the script has finished its task.
print("\nPyramid drawing complete! Hope you enjoyed the show.")
```
