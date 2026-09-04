```python
# This script creates a simple, silly password idea based on user input!

# Ask the user for a few words.
# The 'input()' function gets text from the user.
favorite_color = input("What's your favorite color? ")
animal_name = input("Give me the name of an animal: ")
lucky_number_str = input("What's your lucky number? ")

# Try to convert the lucky number to an integer.
# This makes sure we can do math with it later.
# If it's not a number, it will still be a string for the password.
try:
    lucky_number = int(lucky_number_str)
    # Add a little twist to the number
    transformed_number = lucky_number * 3 + 7
except ValueError:
    # If the input wasn't a number, just use it as is.
    transformed_number = lucky_number_str

# Combine the words and number into a unique password idea.
# f-strings (f"...") are a modern way to embed variables directly into strings.
password_idea = f"{favorite_color.capitalize()}{animal_name.upper()}@{transformed_number}!"

# Print the generated password idea for the user.
print("\nHere's a unique password idea for you:")
print(password_idea)

# Remember, this is just for fun and learning!
# For real passwords, always use strong, random combinations.
```
