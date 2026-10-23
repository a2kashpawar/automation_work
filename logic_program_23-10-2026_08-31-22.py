```python
# Script: Your Unique Daily Affirmation Generator

# This script generates a unique, positive affirmation for you!
# It combines random elements to create a fresh message each time it runs.

import random # This line imports the 'random' module, which helps us pick things randomly.

# Define lists of words to create our affirmations.
# Each list holds different types of words (adjectives, verbs, nouns).
adjectives = ["powerful", "creative", "joyful", "resilient", "wise", "brilliant", "calm", "fantastic", "strong"]
verbs = ["achieve", "inspire", "grow", "discover", "embrace", "manifest", "radiate", "succeed", "flourish"]
nouns = ["potential", "journey", "dreams", "future", "presence", "happiness", "success", "strength", "wisdom"]
outcomes = ["easily", "with grace", "every day", "effortlessly", "with confidence", "now", "always"]

# --- Let's pick a random word from each list! ---

# random.choice() picks one item at random from a list.
random_adjective = random.choice(adjectives)
random_verb = random.choice(verbs)
random_noun = random.choice(nouns)
random_outcome = random.choice(outcomes)

# --- Now, let's assemble our affirmation! ---

# We'll use an f-string (formatted string literal) to combine our words
# into a coherent sentence. This is a modern way to embed variables in strings.
affirmation = f"Today, I am {random_adjective}. I will {random_verb} my {random_noun} {random_outcome}."

# --- Finally, print the generated affirmation! ---

print("--- Your Daily Affirmation ---")
print(affirmation)
print("------------------------------")
print("\nRemember to believe in yourself!")
```
