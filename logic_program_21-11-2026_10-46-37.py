```python
# This script creates a simple "digital fortune cookie" with a random message!

import random # This line imports the 'random' module, which helps us pick things randomly.

# Here's a list of possible "fortunes".
# Lists are ordered collections of items, enclosed in square brackets [].
fortunes = [
    "You will discover a hidden talent today.",
    "A new opportunity awaits you around the corner.",
    "Your kindness will be rewarded soon.",
    "Expect the unexpected, in a good way!",
    "Success comes to those who are persistent.",
    "Take a moment to appreciate the small joys.",
    "A wise decision will be made by you.",
    "Your creativity will inspire others."
]

# We also have a list of "lucky numbers".
lucky_numbers = [7, 13, 21, 33, 42, 55, 68, 88]

# Now, let's pick a random fortune from our list.
# random.choice() selects one item randomly from a list.
chosen_fortune = random.choice(fortunes)

# And pick a random lucky number.
chosen_number = random.choice(lucky_numbers)

# Let's decide if this is a "super lucky" day randomly.
# random.randint(a, b) picks a random integer between a and b (inclusive).
# If the number is 1, it's super lucky!
is_super_lucky_day = (random.randint(1, 3) == 1) # This will be True about 1/3 of the time.

# Time to display our fortune cookie!
print("--- Your Digital Fortune Cookie ---")
print("") # Prints an empty line for spacing.

# Print the main fortune message.
print(f"Fortune: {chosen_fortune}") # f-strings (formatted string literals) allow embedding variables easily.

# Print the lucky number.
print(f"Your lucky number today: {chosen_number}")

# Now, let's add a special message if it's a super lucky day.
# An 'if' statement checks a condition. If True, the code inside runs.
if is_super_lucky_day:
    print("✨ EXTRA LUCKY DAY! ✨ Seize the opportunity!")
else: # 'else' means if the 'if' condition was False, this code runs instead.
    print("Have a wonderful day!")

print("")
print("---------------------------------")

# This script teaches you about:
# - Importing modules (`import random`)
# - Lists (`[]`) for storing multiple items
# - Variables for storing different types of data (strings, integers, booleans)
# - Random selection (`random.choice()`, `random.randint()`)
# - Conditional logic (`if`, `else`)
# - Printing formatted output (`print()`, f-strings)
```
