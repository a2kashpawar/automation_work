```python
# A simple, interactive "Daily Affirmation Generator" for beginners!

import random # This line imports the 'random' module, which helps us pick things randomly.

# This is a list of positive affirmations. Lists are great for storing multiple items.
affirmations = [
    "I am capable of amazing things.",
    "My potential is limitless.",
    "I choose joy and gratitude today.",
    "Every day is a fresh start.",
    "I am worthy of all good things.",
    "Challenges help me grow stronger.",
    "I believe in myself and my abilities."
]

print("Welcome to your Daily Affirmation Generator!")
print("Let's brighten your day with a positive thought.")

# A loop that keeps offering affirmations until the user decides to quit.
while True:
    # random.choice() picks one random item from our 'affirmations' list.
    daily_affirmation = random.choice(affirmations)

    # print() displays text to the console. f-strings (like this one) let us embed variables easily.
    print(f"\nYour affirmation for today: \n>>> {daily_affirmation} <<<")

    # input() asks the user for text and stores it in the 'user_choice' variable.
    user_choice = input("Press Enter for another, or type 'q' to quit: ").lower()

    # An 'if' statement checks a condition. '.lower()' converts input to lowercase for easier comparison.
    if user_choice == 'q':
        print("Stay positive! Goodbye!")
        break # 'break' exits the 'while' loop, ending the program.
    # The 'else' block runs if the 'if' condition is false (i.e., user didn't type 'q').
    else:
        print("Great! Here's another one...")

```
