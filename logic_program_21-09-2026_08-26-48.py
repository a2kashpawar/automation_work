```python
# This script creates a simple "Word Scrambler" game.
# It takes a word from the user and shuffles its letters.

import random # We need the 'random' module to shuffle letters.

print("--- Word Scrambler ---") # A friendly title for the game.

# Get a word from the user.
original_word = input("Enter a word to scramble: ").strip().upper()

# Ensure the user entered something.
if not original_word:
    print("No word entered. Exiting.")
else:
    # Convert the word into a list of characters.
    # For example, "HELLO" becomes ['H', 'E', 'L', 'L', 'O'].
    letters = list(original_word)

    # Use the random.shuffle() function to mix up the order of letters in the list.
    random.shuffle(letters)

    # Join the shuffled letters back together to form the scrambled word.
    # For example, ['L', 'O', 'H', 'E', 'L'] becomes "LOHLE".
    scrambled_word = "".join(letters)

    # Print the original and scrambled words.
    print(f"Original word: {original_word}")
    print(f"Scrambled word: {scrambled_word}")
    print("\nCan you unscramble it?") # A fun prompt for the beginner!
```
