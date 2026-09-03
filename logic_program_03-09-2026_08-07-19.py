```python
# This script draws a unique pyramid pattern using a chosen character.
# It's a great way for beginners to learn about loops and string manipulation!

# 1. Define the character we want to use for our pyramid.
# You can change this to almost any character like '@', '#', 'o', or 'X'.
pyramid_char = "*"

# 2. Decide how many levels (rows) our pyramid will have.
# Try changing this number to make the pyramid taller or shorter!
total_levels = 7

# This is a 'for' loop. It means "repeat the code inside this loop
# for each number in the sequence from 1 up to 'total_levels'".
# 'current_level' will be 1, then 2, then 3, and so on, up to 7.
for current_level in range(1, total_levels + 1):
    # 3. Calculate how many spaces are needed before the characters
    # to make the pyramid appear centered.
    # For example, if total_levels is 7 and current_level is 1,
    # we need 6 spaces: (7 - 1) = 6.
    num_leading_spaces = total_levels - current_level

    # 4. Calculate how many 'pyramid_char' characters are needed for this level.
    # For current_level=1, it's 1 char.
    # For current_level=2, it's 3 chars (2*2 - 1).
    # For current_level=3, it's 5 chars (2*3 - 1).
    num_chars_in_row = (2 * current_level) - 1

    # 5. Create the complete line for this level.
    # We use string multiplication: " " * 6 makes "      " (6 spaces)
    # and pyramid_char * 1 makes "*"
    line_to_print = (" " * num_leading_spaces) + (pyramid_char * num_chars_in_row)

    # 6. Print the created line to the console.
    print(line_to_print)

# Congratulations! You've created a unique text art pyramid.
# Feel free to experiment by changing the 'pyramid_char' and 'total_levels' variables!
```
