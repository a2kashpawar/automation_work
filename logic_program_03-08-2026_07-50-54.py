```python
# This script creates a simple "Word Scrambler"!
# It asks you for a few words and then shuffles them into a new order.

import random # We need the 'random' module to shuffle things around

def word_scrambler():
    print("Welcome to the Word Scrambler!")
    print("Give me a few words, and I'll mix them up for you.")

    user_words = [] # This is an empty list where we'll store the words you type

    # We'll ask for up to 4 words.
    # The 'range(4)' means the loop will run for i=0, 1, 2, 3.
    for i in range(4):
        # f-strings are a neat way to put variables directly into strings.
        # i+1 makes the prompt say "Word #1", "Word #2", etc.
        word = input(f"Enter word #{i+1} (or just press Enter to stop): ")

        # If the user enters nothing (just presses Enter), we break out of the loop.
        if not word:
            break
        
        # Add the word the user typed to our list.
        user_words.append(word.strip()) # .strip() removes any extra spaces around the word

    # Check if the user actually entered any words.
    if not user_words:
        print("\nYou didn't enter any words. Nothing to scramble!")
        return # Exit the function if there are no words

    print("\nYour original words were:", user_words)

    # Now for the magic! 'random.shuffle()' rearranges the items in our list randomly.
    random.shuffle(user_words)

    # We can join the shuffled words back together to form a sentence.
    # The " " tells Python to put a space between each word.
    scrambled_sentence = " ".join(user_words)

    print("\nHere's your scrambled sentence:")
    print(scrambled_sentence)
    print("\nHope you enjoyed your word salad!")

# This line calls our function to start the script when you run it.
word_scrambler()
```
