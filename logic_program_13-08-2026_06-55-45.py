```python
# A simple script to reverse words you type!
# This helps beginners understand string manipulation and loops.

# First, we ask the user for some text.
# The 'input()' function pauses the script and waits for the user to type something and press Enter.
user_sentence = input("Type a sentence and I'll reverse each word: ")

# We'll store the reversed words in a list.
reversed_words = []

# Now, we split the user's sentence into individual words.
# The 'split()' method, without arguments, splits by whitespace (spaces, tabs, newlines).
words = user_sentence.split()

# We use a 'for' loop to go through each word in the 'words' list.
# This demonstrates iterating over a collection.
for word in words:
    # To reverse a word, we can use slicing with a step of -1.
    # [start:end:step]
    # Leaving start and end empty means from the beginning to the end.
    # -1 step means go backwards.
    reversed_word = word[::-1]
    
    # Add the reversed word to our list.
    # The 'append()' method adds an item to the end of a list.
    reversed_words.append(reversed_word)

# Finally, we join the reversed words back together into a single string.
# The 'join()' method is called on the string that will be used as a separator.
# Here, we use a space " " to put spaces between the reversed words.
final_reversed_sentence = " ".join(reversed_words)

# Print the original sentence for comparison.
print(f"\nYour original sentence was: '{user_sentence}'")

# Print the sentence with each word reversed.
# f-strings (formatted string literals) are a modern way to embed expressions inside string literals.
print(f"Here's your sentence with each word reversed: '{final_reversed_sentence}'")

# A little farewell message.
print("\nHope you enjoyed reversing words!")
```
