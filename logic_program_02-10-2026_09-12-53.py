```python
# This script asks for your name and then prints it backwards!

# Prompt the user to enter their name
# The input() function gets text from the user
user_name = input("What's your name? ")

# Reverse the string using string slicing
# [::-1] is a common Python idiom to reverse a sequence
reversed_name = user_name[::-1]

# Print the original name using an f-string (formatted string literal)
print(f"Hello, {user_name}!")

# Print the reversed name
print(f"Your name backwards is: {reversed_name}")

# Check if the original name is the same as the reversed name (a palindrome)
# .lower() converts the string to lowercase for case-insensitive comparison
if user_name.lower() == reversed_name.lower():
    print("That's interesting! Your name is a palindrome!")
else:
    print("Looks like your name isn't a palindrome.")
```
