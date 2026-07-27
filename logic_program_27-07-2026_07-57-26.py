```python
# Import the 'random' module to allow us to make random choices later.
import random

# A list of different 'fortune cookie' messages.
# Each item in this list is a string (text).
fortune_messages = [
    "A journey of a thousand miles begins with a single step.",
    "The early bird catches the worm.",
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "It is better to light a single candle than to curse the darkness.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "You will have a great day today!",
    "Good things come to those who wait.",
    "Live as if you were to die tomorrow. Learn as if you were to live forever."
]

# Greet the user and explain the purpose of the script.
print("Welcome to your daily Python Fortune Cookie!")
print("Let's see what wisdom awaits you...")

# The input() function pauses the program and waits for the user to press Enter.
# We use it here to give the user a chance to read the greeting before getting their fortune.
input("Press Enter to crack open your fortune cookie!")

# random.choice() picks one random item from the 'fortune_messages' list.
chosen_fortune = random.choice(fortune_messages)

# Print the chosen fortune message to the user.
print("\n--- Your Fortune ---")
print(chosen_fortune)
print("--------------------")

# A concluding message.
print("\nHave a wonderful day!")
```
