```python
# This script creates a simple "daily affirmation generator".
# It asks for your name and then provides a personalized, random affirmation.

import random # We need the 'random' module to pick a random affirmation.

# Define a list of positive affirmations.
affirmations = [
    "You are capable of amazing things today!",
    "Believe in yourself and all that you are.",
    "Your potential is limitless.",
    "Embrace the journey and trust the process.",
    "You are worthy of happiness and success.",
    "Every day is a new opportunity to shine."
]

# Ask the user for their name to personalize the affirmation.
user_name = input("Hello! What's your name? ")

# Choose a random affirmation from our list.
daily_affirmation = random.choice(affirmations)

# Print the personalized affirmation.
# We use an f-string (formatted string literal) for easy variable insertion.
print(f"\n✨ Hello, {user_name}! Here is your affirmation for today: ✨")
print(f"'{daily_affirmation}'")
print("\nHave a wonderful day!")
```
