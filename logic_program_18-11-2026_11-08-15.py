```python
# This script simulates a very simple "fortune teller" or "magic 8-ball".

# First, we need to import the 'random' module.
# This module provides functions to generate random numbers or make random selections.
import random

# Define a list of possible answers the oracle can give.
# A list is an ordered collection of items.
oracle_responses = [
    "It is certain.",
    "Yes, definitely.",
    "Without a doubt.",
    "Outlook good.",
    "You may rely on it.",
    "Ask again later.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Greet the user and ask for their question.
# The input() function waits for the user to type something and press Enter.
# The text inside input() is the prompt shown to the user.
user_question = input("Welcome, seeker! Ask the Mysterious Oracle your yes/no question: ")

# To make sure the user sees their question, we print it back.
print(f"You asked: '{user_question}'")

# Now, we use the random.choice() function to pick one answer randomly
# from our 'oracle_responses' list.
chosen_answer = random.choice(oracle_responses)

# Finally, print the Oracle's answer to the user.
# An f-string (formatted string literal) is used here to easily embed variables.
print(f"The Mysterious Oracle whispers: {chosen_answer}")

# A little closing message.
print("May your path be clear!")
```
