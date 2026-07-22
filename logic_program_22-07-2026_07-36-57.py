```python
# This script creates a simple, repeating pattern from your input!

# First, we ask the user for a single character or symbol.
# The 'input()' function gets text from the user.
user_symbol = input("Enter any single character or symbol: ")

# Next, we ask how many times they want the pattern to repeat.
# We use 'int()' to convert their text input into a whole number.
repeat_times = int(input("How many times should it repeat? (Enter a number): "))

# We can create a string that repeats a character by multiplying it!
# This line creates the actual pattern string.
pattern_line = user_symbol * repeat_times

# Now, let's print some decorative lines to make the output clear.
print("=" * 30) # Prints 30 equals signs

# This prints our generated pattern line.
print(pattern_line)

# Let's print it again, just for fun!
print(pattern_line)

# A little message for the user.
print("\nThat's your custom pattern!")

# Another decorative line to finish.
print("=" * 30)
```
