```python
# Welcome, beginner programmer! This script will tell you a random "coding mantra".

# First, we need the 'random' module to pick a mantra randomly.
import random

# A list of simple coding mantras.
# Lists are ordered collections of items.
mantras = [
    "Keep it simple!",
    "Read the error messages!",
    "One step at a time!",
    "Don't be afraid to break it!",
    "Ask for help!",
    "Google is your friend!",
    "Practice makes progress!",
    "Write comments!",
    "Have fun coding!",
    "You've got this!"
]

# Get the total number of mantras available.
# len() is a function that returns the length of an object.
number_of_mantras = len(mantras)

# Choose a random index from 0 up to (number_of_mantras - 1).
# random.randint(a, b) returns a random integer N such that a <= N <= b.
random_index = random.randint(0, number_of_mantras - 1)

# Retrieve the mantra at the chosen random index.
# We use square brackets [] to access items in a list by their index.
your_mantra = mantras[random_index]

# Print the chosen mantra to the console.
# print() is used to display output.
print("Here's your coding mantra for the day:")
print("--------------------------------------")
print(your_mantra)
print("--------------------------------------")

# Encourage the user.
print("\nHappy coding!")
```
