```python
# A unique little script that helps you build a custom text banner!

# Ask the user for their name or any short word they like
user_text = input("Enter your name or a short word: ")

# Ask for a character to use as a border
# This character will repeat to form the top and bottom lines
border_char = input("Now, enter a single character to use as a border (e.g., *, #, ~): ")

# Make sure the user entered at least one character for the border
# If not, we'll default to a star '*'
if not border_char:
    border_char = '*' # Default border character

# We only want the first character if the user typed more than one
border_char = border_char[0]

# Calculate the length of the user's text
text_length = len(user_text)

# Create the top and bottom border lines
# We add 4 to the length for padding around the word (2 spaces on each side)
# So, ' Hello ' would be 'length of " Hello "' + 4 = 7+4 = 11 characters long for the border
border_line_length = text_length + 4
top_bottom_border = border_char * border_line_length

# Print the complete banner!
print("\nHere's your personalized banner:")
print(top_bottom_border)            # The top border line
print(border_char + " " + user_text + " " + border_char) # The word with border and padding
print(top_bottom_border)            # The bottom border line

# A friendly farewell message
print("\nHope you like your unique banner!")
```
