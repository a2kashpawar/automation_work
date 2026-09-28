```python
# Simple Dice Roll - Are you feeling lucky?

# Import the 'random' module to generate random numbers.
# This module is built-in and helps us create unpredictable results.
import random

# Ask the user to press Enter to "roll" the dice.
# The input() function waits for the user to type something and press Enter.
input("Press Enter to roll the dice and see your lucky number!")

# Generate a random integer between 1 and 6 (inclusive).
# This simulates a standard six-sided dice roll.
dice_roll = random.randint(1, 6)

# Print the result of the dice roll using an f-string.
# F-strings are a great way to embed variables directly into strings.
print(f"\nYou rolled a {dice_roll}!")

# Use an 'if-else' statement to give a different message based on the roll.
# This introduces basic conditional logic, a core programming concept.
if dice_roll >= 4:
    print("Looks like a good roll! Maybe your luck is turning.")
else:
    print("Every number is a good number when you're having fun!")

# Try running this script multiple times to see different results!
```
