```python
# Import the 'random' module to use its functions for generating random choices.
import random

# A list of simple, positive affirmations.
affirmations = [
    "You are capable of amazing things!",
    "Every day is a new opportunity to grow.",
    "Your efforts will lead to success.",
    "Believe in yourself and all that you are.",
    "You are stronger than you think.",
    "Great things are coming your way.",
    "Your unique perspective is valuable.",
    "You're doing great, keep going!"
]

# Print a welcoming header for the user.
print("✨ Daily Affirmation Generator ✨")
print("---------------------------------")

# Use the random.choice() function to pick one affirmation from the list.
# This function randomly selects a single element from a sequence (like a list).
chosen_affirmation = random.choice(affirmations)

# Print the selected affirmation to the console.
print("Here is your positive thought for the day:")
print(f"🌟 {chosen_affirmation} 🌟") # An f-string is a simple way to embed variables in a string.

print("---------------------------------")
print("Have a wonderful day! 😊")
```
