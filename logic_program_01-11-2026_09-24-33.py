```python
# This script creates a personalized "sign" for any word you type!

# First, we ask the user to type a word and store it in a variable called 'user_word'.
# The input() function waits for you to type something and press Enter.
user_word = input("Type a short word: ")

# Next, we figure out how long the word is.
# The len() function counts the number of characters in a string.
word_length = len(user_word)

# Now, we create a decorative border line.
# We want the border to be a bit longer than the word itself for padding.
# '*' * (word_length + 4) means repeat the '*' character 'word_length + 4' times.
# For example, if 'word_length' is 5, it will print '*' 9 times.
border_line = '*' * (word_length + 4)

# Print the top border line.
print(border_line)

# Print the word itself, surrounded by stars and spaces to make it centered in our "sign".
# An f-string (formatted string literal) makes it easy to embed variables directly.
# '* {user_word} *' will become something like '* HELLO *' if the word is HELLO.
print(f"* {user_word} *")

# Print the bottom border line, which is the same as the top one.
print(border_line)

# Try typing different words to see how the sign changes!
```
