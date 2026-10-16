```python
import random

# Define a list of silly adjectives
adjectives = [
    "Wobbly", "Giggling", "Fluffy", "Sparkly", "Sneezing",
    "Grumpy", "Chubby", "Squeaky", "Bouncing", "Dizzy",
    "Zany", "Quirky", "Blubbering", "Squishy", "Goofy"
]

# Define a list of fun, unexpected nouns
nouns = [
    "Panda", "Ninja", "Pickle", "Unicorn", "Sock",
    "Potato", "Robot", "Banana", "Cloud", "Goblin",
    "Toaster", "Waffle", "Penguin", "Sprinkle", "Noodle"
]

# Randomly select one adjective from the list
chosen_adjective = random.choice(adjectives)

# Randomly select one noun from the list
chosen_noun = random.choice(nouns)

# Combine the chosen adjective and noun to create a unique silly name
silly_name = f"{chosen_adjective} {chosen_noun}"

# Print the generated silly name to the console
print("Your unique silly name is:")
print(silly_name)
```
