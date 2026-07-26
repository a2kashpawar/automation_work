```python
import random

# Ask the user for a number, which will be the length of their unique line.
length_str = input("Enter a number for your line's length (e.g., 10): ")

# Try to convert the user's input string to an integer.
try:
    length = int(length_str)
except ValueError:
    # If the input isn't a valid number, print a message and set a default length.
    print("That wasn't a valid number. Defaulting to 15.")
    length = 15

# Ensure the length is at least 1, otherwise, adjust it.
if length < 1:
    length = 1

# A list of simple characters to form the main part of the line.
base_chars = ['-', '=', '~', '.']
# A list of more interesting characters (emojis!) to be the "unique" part.
unique_chars = ['✨', '🌟', '💫', '⭐', '🎇', '💡']

# Randomly pick one character for the main line and one for the unique spot.
main_char = random.choice(base_chars)
unique_char = random.choice(unique_chars)

# Randomly decide where the unique character will appear within the line.
# It will be at any valid index from 0 up to (length - 1).
unique_position = random.randint(0, length - 1)

# Initialize an empty string to build our final line.
final_line = ""

# Loop through each position from 0 up to (length - 1).
for i in range(length):
    if i == unique_position:
        # If the current position is our chosen unique spot, add the unique character.
        final_line += unique_char
    else:
        # Otherwise, add the regular main character.
        final_line += main_char

# Add some empty lines for better visual separation.
print("\n")
# Print the unique line that was just created.
print(final_line)
# A little motivational message.
print("Keep being unique!\n")
```
