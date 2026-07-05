```python
# This is a simple Python script to reverse any word you type!

# Step 1: Ask the user to enter a word.
# The 'input()' function displays a message and waits for the user to type something.
# Whatever the user types is then stored in the 'original_word' variable.
original_word = input("Type a word and press Enter: ")

# Step 2: Reverse the word.
# Python has a very powerful and concise feature called 'string slicing' for this.
# The [::-1] syntax is a special slice that means:
# - Start at the beginning of the string (empty before the first colon).
# - Go to the end of the string (empty before the second colon).
# - Take every character, but step backwards (-1) through the string.
reversed_word = original_word[::-1]

# Step 3: Print both the original and the reversed word.
# The 'print()' function displays text on the screen.
# We use an f-string (formatted string literal) to easily embed variables
# directly into the text we want to print. The '\n' creates a new line for spacing.
print(f"\nYour original word: {original_word}")
print(f"Your reversed word: {reversed_word}")

# And that's it! Feel free to run the script again with a different word.
```
