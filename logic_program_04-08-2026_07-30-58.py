```python
# This is a short, interactive Python script for beginners!
# It's a simple "Magic 8-Ball" style program.

import random # We need the 'random' module to pick a random answer.

# --- Step 1: Welcome and get the user's question ---
print("Welcome to the Super Simple Decision Maker!")
print("Ask me any yes/no question, and I will give you an answer.")

# We use input() to get text from the user.
user_question = input("What is your question? (Press Enter when done) \n") # The \n makes a new line for typing.

# --- Step 2: Prepare a list of possible answers ---
# A list is a collection of items, enclosed in square brackets [].
possible_answers = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
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

# --- Step 3: Pick a random answer ---
# random.choice() selects one item randomly from a list.
chosen_answer = random.choice(possible_answers)

# --- Step 4: Display the answer ---
# We print the chosen answer back to the user.
print("\n--- The Decision Maker says ---") # \n adds an empty line above for better readability.
print(chosen_answer)
print("-------------------------------")

# --- Step 5: A friendly goodbye ---
print("\nThanks for using the Super Simple Decision Maker!")
```
