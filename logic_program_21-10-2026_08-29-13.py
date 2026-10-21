```python
# This script generates a simple, encouraging message randomly!

import random # We use the 'random' module to pick a message randomly.

# Here's a list of positive messages. Feel free to add your own!
encouraging_messages = [
    "You're doing great!",
    "Keep up the fantastic work!",
    "Every line of code is progress!",
    "Don't be afraid to experiment!",
    "Coding is a superpower!",
    "You've got this!",
]

# The random.choice() function picks one item from the list at random.
chosen_message = random.choice(encouraging_messages)

# Now, we print the message to the console.
print("--- A little message for you ---")
print(chosen_message)
print("------------------------------")

# Try running this script a few times to see different messages!
```
