```python
# This script creates a simple "magic 8-ball" style fortune teller.
# It uses a list of responses and picks one randomly.

import random # The 'random' module is needed to pick a response randomly.

# Define a list of possible fortune responses.
fortunes = [
    "It is certain.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Signs point to yes."
]

# Ask the user to think of a question.
# The question itself isn't used, but it makes the interaction engaging.
input("Think of a yes/no question, then press Enter to reveal your fortune...\n")

# Use random.choice() to pick one item from the 'fortunes' list.
# This function is perfect for selecting a random element from a sequence.
chosen_fortune = random.choice(fortunes)

# Print the chosen fortune to the user.
# f-strings are used here for an easy way to embed variables into a string.
print(f"Your fortune is: {chosen_fortune}")

# End with a friendly message.
print("\nMay your day be filled with good fortunes!")
```
