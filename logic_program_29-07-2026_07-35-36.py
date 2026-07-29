```python
# Import the 'random' module to allow for random selections.
import random

# Create a list of possible responses for our "fortune teller".
fortunes = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Prompt the user to think of a question.
# The actual question isn't used by the program, just the interaction.
input("Think of a yes/no question, then press Enter to reveal your fortune: ")

# Use random.choice() to pick one fortune randomly from the 'fortunes' list.
chosen_fortune = random.choice(fortunes)

# Print the randomly selected fortune to the console.
print(chosen_fortune)
```
