```python
# This script creates a simple "Magic 8-Ball" style fortune teller.
# It will ask you to think of a question and then give you a random answer.

import random # We need the 'random' module to pick a random answer.

# A list (a collection of items) of possible answers the fortune teller can give.
possible_answers = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Prompt the user to think of a question.
# The input() function waits for the user to type something and press Enter.
# In this case, we just use it to pause the script until the user is ready.
input("Think of a yes/no question in your mind, then press Enter for your answer...")

# Use random.choice() to pick one random item from our 'possible_answers' list.
chosen_answer = random.choice(possible_answers)

# Print the chosen answer to the console.
print("\nYour answer is:") # The '\n' creates a new line before the text.
print(chosen_answer)

print("\nMay your future be bright!") # A friendly closing message.
```
