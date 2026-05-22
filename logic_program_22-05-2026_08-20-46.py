```python
# A unique, short Python script for a beginner!

# This script creates a simple "magic word scrambler".
# It takes a word from the user and rearranges its letters in a playful way.

import random # We need the 'random' module to shuffle letters.

# 1. Ask the user for a word.
# The 'input()' function gets text from the user.
original_word = input("Enter a word to scramble: ")

# 2. Convert the word into a list of its letters.
# This makes it easy to shuffle them around.
letters = list(original_word)

# 3. Use the 'random.shuffle()' function to mix up the letters.
# This modifies the 'letters' list in place.
random.shuffle(letters)

# 4. Join the shuffled letters back into a new word.
# The '.join()' method combines elements of a list into a string.
scrambled_word = "".join(letters)

# 5. Print the original and the scrambled word.
# f-strings (formatted string literals) are a nice way to embed variables.
print(f"\nOriginal word: {original_word}")
print(f"Scrambled word: {scrambled_word}")

# Try entering your name or a favorite animal to see it scrambled!
# Each time you run it with the same word, it might scramble differently.
```
