```python
# Import the random module to use random functions
import random

# A list of possible answers for our "magic" script
# Lists are ordered collections of items
responses = [
    "Yes, definitely!",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good."
]

# Get a question from the user (optional, but makes it interactive)
# The input() function prompts the user for text
input("Ask a yes/no question to the cosmic predictor (then press Enter): ")

# Randomly choose one response from the 'responses' list
# random.choice() picks a random item from a given sequence
chosen_response = random.choice(responses)

# Print the chosen response to the console
# An f-string (formatted string literal) is used for easy embedding of variables
print(f"The cosmic predictor says: {chosen_response}")
```
