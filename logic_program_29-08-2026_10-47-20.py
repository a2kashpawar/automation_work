```python
# Import the 'random' module to pick things randomly from a list.
import random

# A list of fun and quirky fortune messages.
fortunes = [
    "A pleasant surprise awaits you today!",
    "You will make a new friend very soon.",
    "Expect the unexpected, in a good way!",
    "Your hard work will pay off handsomely.",
    "A new adventure is just around the corner.",
    "Someone is thinking of you fondly.",
    "The answer you seek will appear when you least expect it."
]

# Ask the user for their name to make the experience personal.
user_name = input("Hello, brave adventurer! What is your name? ")

# Pick one random fortune message from our list.
random_fortune = random.choice(fortunes)

# Print a personalized fortune message using an f-string for easy formatting.
print(f"\nGreetings, {user_name}! Your mystical fortune for today is:")
print(f"✨ {random_fortune} ✨")

# A little closing message.
print("\nMay your day be filled with wonder!")
```
