```python
# A quirky little decision helper!
# Ask it a 'yes' or 'no' question and see what it suggests.

import random # This line imports the 'random' module, which helps us pick things randomly.

# A list of possible, slightly unhelpful, answers.
# Lists are ordered collections of items. Here, they are text strings.
possible_outcomes = [
    "Definitely, if the moon is full!",
    "It's a strong 'maybe,' but check for squirrels first.",
    "The stars say no, unless you really want to.",
    "Consult the ancient scrolls (or your fridge).",
    "Only if you promise to dance a little jig.",
    "Why not? What's the worst that could happen?",
    "Better not risk it. Stay safe indoors.",
    "The universe is currently buffering. Try again later.",
    "If a cat crosses your path, then yes.",
    "Only after a good nap."
]

# Get a question from the user.
# The 'input()' function waits for the user to type something and press Enter.
# Whatever they type is stored in the 'user_question' variable.
user_question = input("Ask me a yes/no question (e.g., 'Should I eat that cookie?'): ")

# Pick a random answer from our list.
# 'random.choice()' selects one item randomly from a list.
decision = random.choice(possible_outcomes)

# Add a little extra flair based on the length of the question.
# 'len()' tells us how many characters are in a string.
# 'if', 'elif', 'else' are used for conditional logic.
if len(user_question) > 30: # If the question is quite long...
    print("\nHmm, that's a deep thought...") # Print a reflective comment.
    print(f"My cosmic sensors indicate: {decision}") # Print the chosen decision using an f-string for easy formatting.
elif len(user_question) < 15: # Else if the question is quite short...
    print("\nQuick question, quick answer...") # Print a snappy comment.
    print(f"The oracle whispers: {decision}")
else: # If the question length is somewhere in the middle...
    print("\nLet me ponder your query...") # Print a pondering comment.
    print(f"My circuits suggest: {decision}")

# A final encouraging message.
print("\nMay your decisions be... interesting!")
```
