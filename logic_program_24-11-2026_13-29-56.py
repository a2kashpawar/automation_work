```python
# This script generates a simple, repeating pattern of characters.
# It's a fun way to see how loops and string manipulation work in Python.

# First, we choose the character that will make up our pattern.
# Try changing this to '#', '!', or even '^_^ ' to see different results!
pattern_char = "@"

# Next, we decide how many times the pattern should repeat on each line.
# This controls the "width" of the growing part of our pattern.
max_repeats = 5

# We use a 'for' loop to create the "growing" part of the pattern.
# The 'range(1, max_repeats + 1)' generates numbers from 1 up to 'max_repeats'.
for count in range(1, max_repeats + 1):
    # Inside the loop, we print our 'pattern_char' multiplied by 'count'.
    # This makes each line longer than the last.
    print(pattern_char * count)

# After the growing part, we use another 'for' loop for the "shrinking" part.
# The 'range(max_repeats - 1, 0, -1)' generates numbers from 'max_repeats - 1' down to 1.
# The '-1' at the end means it counts downwards.
for count in range(max_repeats - 1, 0, -1):
    # Again, we print the character multiplied by 'count'.
    # This time, each line gets shorter.
    print(pattern_char * count)

# You've created a dynamic, symmetrical pattern!
# Experiment with 'pattern_char' and 'max_repeats' to customize your art.
```
