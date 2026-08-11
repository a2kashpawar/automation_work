```python
# This script draws a simple, growing pattern using characters!

# You can change this number to make the pattern bigger or smaller.
pattern_height = 5

# We use a 'for' loop to repeat actions for each line of our pattern.
# 'range(pattern_height)' will give us numbers from 0 up to 'pattern_height - 1'.
for line_number in range(pattern_height):
    # Calculate how many leading spaces are needed for this line.
    # We want fewer spaces as the 'line_number' increases.
    # ' ' * N repeats the space character N times.
    leading_spaces = " " * (pattern_height - 1 - line_number)

    # Calculate how many stars are needed for this line.
    # We want more stars as the 'line_number' increases (odd numbers: 1, 3, 5...).
    # '*' * N repeats the star character N times.
    stars_on_line = "*" * (2 * line_number + 1)

    # Now, combine the spaces and stars, then print them to form one line of the pattern.
    # The '+' operator joins the two strings together.
    print(leading_spaces + stars_on_line)

# Experiment by changing the 'pattern_height' variable at the top!
# What happens if you change '*' to another character like '#' or '$'?
```
