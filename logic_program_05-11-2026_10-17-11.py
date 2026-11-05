```python
# A simple script to help you pick a snack when you're indecisive!
# This uses basic Python features: lists, random choices, input, and print.

import random # We need this library to pick a random item from our list

# Create a list of possible snack ideas.
# A list is an ordered collection of items.
snack_options = [
    "apple slices",
    "a handful of almonds",
    "yogurt with berries",
    "rice cakes with avocado",
    "a banana",
    "whole-wheat crackers and cheese",
    "carrot sticks with hummus",
    "popcorn (air-popped)",
    "an orange",
    "a hard-boiled egg"
]

# Print a welcome message to the user.
print("Feeling hungry but can't decide what to snack on?")
print("Let me pick a healthy snack for you!")

# Ask the user to press Enter to get their snack.
# The input() function waits for user input.
input("Press Enter to reveal your recommended snack...")

# Use random.choice() to pick one item randomly from our snack_options list.
chosen_snack = random.choice(snack_options)

# Display the chosen snack to the user.
# An f-string (formatted string literal) is used here to easily embed variables.
print(f"\nYour recommended snack is: {chosen_snack.upper()}!")
print("\nEnjoy your snack!")

# End of the script.
```
