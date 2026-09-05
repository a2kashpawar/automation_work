```python
# This script creates a simple "magic 8-ball" to answer your questions.

import random # Imports the 'random' module to pick a random answer.

# A list of possible answers the magic 8-ball can give.
possible_answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
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

# Ask the user to think of a question.
# The actual question text isn't used, only the act of asking.
input("Think of a yes/no question, then press Enter to shake the Magic 8-Ball...")

# Randomly select one answer from the 'possible_answers' list.
chosen_answer = random.choice(possible_answers)

# Print the chosen answer to the user.
print("\nMagic 8-Ball says:", chosen_answer)
```
