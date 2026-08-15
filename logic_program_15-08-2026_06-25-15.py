```python
# This script animates a simple word by displaying its letters one by one,
# then removing them one by one, creating a "typewriter" or "reveal" effect.

# Define the secret word we want to animate.
secret_word = "CODE"

# First, let's reveal the word letter by letter.
# We'll loop through each letter in the secret_word.
current_display = ""
for letter in secret_word:
    # Add the current letter to our display string.
    current_display += letter
    # Print the progressively growing word.
    print(current_display)

# Add a small separator for visual clarity.
print("---")

# Now, let's make the word disappear letter by letter.
# We'll loop from the full length down to zero.
# len(current_display) gives us the current length of the word ("CODE" is 4).
# range(start, stop, step): start from 4, go down to 0 (exclusive), step by -1.
for i in range(len(current_display), 0, -1):
    # Slice the string from the beginning up to 'i' characters.
    # For i=4, it's "CODE". For i=3, it's "COD", and so on.
    shrinking_display = current_display[:i]
    # Print the progressively shrinking word.
    print(shrinking_display)

# A final message.
print("Animation complete!")
```
