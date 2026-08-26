```python
# magic_fortune.py - Your mystical digital guide!

import random # This line imports the 'random' module, which allows us to pick a random item.

# Here's a list (an ordered collection) of different fortunes.
# Each fortune is a string (text surrounded by quotes).
fortunes = [
    "A surprising discovery awaits you.",
    "The stars align for a new adventure.",
    "Expect the unexpected, but be prepared for it.",
    "Your creative spirit will lead the way.",
    "Seek wisdom, not just knowledge.",
    "A new friend is closer than you think.",
    "Don't postpone joy.",
    "Trust your intuition today.",
    "Good things come to those who act.",
    "Tomorrow holds a pleasant surprise.",
    "A small gesture will bring great happiness.",
]

# This line asks the user to type something and press Enter.
# We don't actually use their input, but it makes the program interactive.
input("Ponder your question, then press Enter to reveal your fortune: ")

# random.choice(fortunes) picks one random string from our 'fortunes' list.
chosen_fortune = random.choice(fortunes)

# Finally, this line prints the randomly chosen fortune to the screen.
print("\nYour digital oracle reveals:") # '\n' adds a new line for better formatting.
print(chosen_fortune)

# The program finishes here!
```
