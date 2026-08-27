```python
# This script creates a simple, personalized "hello" message with a little flair!

# First, we ask the user for their name using the 'input()' function.
# The text inside 'input()' is what the user sees as a prompt.
user_name = input("What's your name? ")

# We choose a special character to use for decoration.
decorator = "*"

# We calculate the length of the user's name.
# We add 6 to ensure there's enough space around the name for the decorator and padding.
# (2 for decorators + 2 spaces before name + 2 spaces after name)
banner_length = len(user_name) + 6

# Now, we create the top and bottom lines of our banner.
# We multiply the 'decorator' character by 'banner_length' to repeat it.
banner_line = decorator * banner_length

# Print the top line of the banner.
print(banner_line)

# Print the user's name, surrounded by the decorator and spaces.
# We use an f-string (formatted string literal) for easy variable insertion.
print(f"{decorator}  {user_name}  {decorator}")

# Print the bottom line of the banner.
print(banner_line)

# Finally, print a friendly, personalized greeting.
# We use string concatenation (+) here to join parts of the message.
print("\nWelcome to Python, " + user_name + "!")
```
