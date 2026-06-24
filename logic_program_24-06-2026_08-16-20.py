```python
# This script creates a simple "text-growing" animation from user input.
# It demonstrates basic input, loops, and string slicing.

# Ask the user to enter any word or short phrase
user_text = input("Enter a word or phrase: ")

# Add a blank line for better visual separation
print()

# Loop through the user's text, character by character
# 'i' will represent the current length of the text to display
for i in range(1, len(user_text) + 1):
    # Slice the original text from the beginning up to 'i' characters
    # Then print the growing piece of text
    print(user_text[:i])

# Add another blank line at the end
print()

# Print the full text as a final flourish
print("That's your full text!")
```
