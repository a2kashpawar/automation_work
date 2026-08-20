```python
import random # Import the 'random' module to pick things randomly

# A list of different animal names
animals = ["cat", "dog", "cow", "duck", "sheep", "frog"]

# A list of sounds corresponding to each animal in the 'animals' list
sounds = ["meow", "woof", "moo", "quack", "baa", "ribbit"]

# Choose a random number (index) from 0 up to the number of animals minus 1
# This ensures we pick an index that exists in both lists
random_index = random.randint(0, len(animals) - 1)

# Get the animal at the chosen random index
chosen_animal = animals[random_index]

# Get the sound at the *same* chosen random index
chosen_sound = sounds[random_index]

# Print a question using an f-string (formatted string literal)
# f-strings let you easily embed variables directly into strings
print(f"What sound does a {chosen_animal} make?")

# Print the answer, making the sound uppercase for emphasis!
print(f"It goes '{chosen_sound.upper()}!'")

# A little closing message
print("\nHope you enjoyed your animal sound!")
```
