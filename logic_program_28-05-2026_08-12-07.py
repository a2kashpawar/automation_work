```python
# This script creates a simple "secret word" by replacing vowels with numbers!
# It's a fun way to see how you can change text in Python.

# Step 1: Ask the user to type in a word.
# The 'input()' function pauses the script and waits for the user to type something,
# then it stores that text in a variable called 'original_word'.
original_word = input("Enter a word to make it secret: ")

# Step 2: Convert the word to lowercase for consistent replacements.
# This means 'Apple' and 'apple' will both be processed the same way.
# The '.lower()' method creates a new string with all characters in lowercase.
working_word = original_word.lower()

# Step 3: Now, we'll replace each vowel with a number.
# The 'replace()' method looks for a specific character (first argument)
# and swaps it with another character (second argument) throughout the string.
# It returns a NEW string, so we reassign it back to 'working_word' each time.
working_word = working_word.replace('a', '1') # Replace 'a' with '1'
working_word = working_word.replace('e', '2') # Replace 'e' with '2'
working_word = working_word.replace('i', '3') # Replace 'i' with '3'
working_word = working_word.replace('o', '4') # Replace 'o' with '4'
working_word = working_word.replace('u', '5') # Replace 'u' with '5'

# Step 4: Display the original and the new "secret" word to the user.
# We use an f-string (formatted string literal) for easy printing.
# Anything inside curly braces {} within an f-string gets replaced by the variable's value.
print(f"\nYour original word was: {original_word}")
print(f"Your secret word is:    {working_word}")

# You've just made a simple text transformer!
```
