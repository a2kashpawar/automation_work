```python
# This script generates a simple, personalized "daily vibe" based on your name.

import random # We need the 'random' module to pick a random number.

# Ask the user for their name.
user_name = input("Hello there! What's your name? ")

# Generate a random "lucky number" between 1 and 100.
lucky_number = random.randint(1, 100)

# Create a list of short, positive fortunes or "vibe" messages.
fortunes = [
    "Today holds a delightful surprise!",
    "Your creativity will shine brightly.",
    "A new opportunity is just around the corner.",
    "Share your joy, and it will multiply.",
    "Embrace challenges; they lead to growth.",
    "Kindness is your superpower today.",
    "Listen to your intuition; it knows the way."
]

# Pick a fortune based on the length of the user's name.
# Using the modulo operator (%) ensures we always get a valid index for the 'fortunes' list,
# regardless of how long the name is.
chosen_fortune = fortunes[len(user_name) % len(fortunes)]

# Print a personalized message with the lucky number and fortune.
print(f"\nWelcome, {user_name}!") # The '\n' creates a new line for better readability.
print(f"Your lucky number for today is: {lucky_number}")
print(f"Here's a little vibe for you: {chosen_fortune}")
print("\nHave a wonderful day!") # Another new line at the end.
```
