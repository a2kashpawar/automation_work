# This is a fun little script that acts like a Magic 8-Ball!
# You ask it a question, and it gives you a random answer.

# First, we need to import the 'random' module.
# This module provides functions for generating random numbers and choices.
import random

# Here, we create a list of possible answers the Magic 8-Ball can give.
# A list is an ordered collection of items, enclosed in square brackets.
possible_answers = [
    "It is certain.",
    "Yes, definitely.",
    "Without a doubt.",
    "You may rely on it.",
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
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "No."
]

# We use the 'input()' function to ask the user for their question.
# The text inside 'input()' is the prompt shown to the user.
# The user's typed response is stored in the 'user_question' variable.
user_question = input("Ask the Magic 8-Ball a yes/no question: ")

# We use an 'if' statement to check if the user actually typed something for their question.
# An empty string is considered 'False' in Python.
if user_question:
    # If a question was typed (the string is not empty), we proceed.
    # 'random.choice()' is a function that picks one random item from a list.
    chosen_answer = random.choice(possible_answers)

    # Finally, we print the chosen answer to the console.
    # The '\n' creates a new line for better readability.
    print("\nMagic 8-Ball says:")
    print(chosen_answer)
else:
    # If the user didn't type a question (the string was empty), we tell them that.
    print("You didn't ask a question! Try again.")
