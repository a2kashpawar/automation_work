```python
# This script helps you create a decorative "echo" of your favorite word!

# First, we ask the user for a word they like.
# The 'input()' function pauses the script and waits for the user to type something.
favorite_word = input("Enter your favorite word: ")

# Next, we ask for a number to decide how many times to "echo" it.
# 'input()' always returns text (a string), so we convert it to an integer using 'int()'.
echo_count_str = input("How many times should it echo? (Enter a number, e.g., 3): ")

# We should try to handle cases where the user doesn't enter a valid number.
# For simplicity in a beginner script, we'll assume valid input for now,
# but in real code, you'd use a 'try-except' block.
echo_count = int(echo_count_str)

# Now, we create a border character based on the first letter of their word.
# This makes the output unique to their input!
# '[0]' gets the first character of the string.
border_char = favorite_word[0].upper()

# We calculate the length needed for the top and bottom borders.
# This makes the border fit nicely around the word.
border_length = len(favorite_word) + 4 # Add 4 for padding spaces and border chars

# The 'print()' function displays text on the console.
# We multiply the border character by the border_length to create the top border.
print(border_char * border_length)

# We use a 'for' loop to repeat the "echo" of the word.
# 'range(echo_count)' generates numbers from 0 up to (but not including) echo_count.
for i in range(echo_count):
    # 'f-strings' (formatted string literals) are a modern way to embed variables directly into strings.
    # We add spaces around the word and the border character at each end.
    print(f"{border_char}  {favorite_word}  {border_char}")

# Finally, we print the bottom border, mirroring the top one.
print(border_char * border_length)

# A simple farewell message using the word they chose.
print(f"Hope you enjoyed echoing '{favorite_word}'!")
```
