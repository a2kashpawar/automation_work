```python
# This script takes a word or phrase from the user,
# then counts how many times each unique character appears in it,
# and finally visualizes these counts using hash marks.

# 1. Get input from the user.
# The input() function displays a prompt and waits for the user to type
# something and press Enter. The entered text is stored in `user_text`.
user_text = input("Enter a short word or phrase: ")

# 2. Prepare a dictionary to store character counts.
# A dictionary (dict) is a collection of key-value pairs.
# Here, each unique character will be a 'key', and its count will be the 'value'.
character_counts = {}

# 3. Iterate through each character in the user's input.
# The 'for' loop processes one character at a time from `user_text`.
for char in user_text:
    # Convert the character to lowercase to treat 'A' and 'a' as the same.
    # This makes the counting case-insensitive.
    lower_char = char.lower()

    # Check if the lowercase character is already a key in our dictionary.
    if lower_char in character_counts:
        # If it is, increment its existing count by 1.
        character_counts[lower_char] += 1
    else:
        # If it's a new character, add it to the dictionary with a count of 1.
        character_counts[lower_char] = 1

# 4. Print the character frequency visualization.
print("\n--- Character Frequency Breakdown ---") # A header for clarity.

# Loop through each key-value pair stored in the `character_counts` dictionary.
# The `.items()` method returns tuples of (key, value) for each entry.
for char, count in character_counts.items():
    # Create a simple visual "bar" using hash marks.
    # The '*' operator repeats a string. E.g., '#' * 3 results in "###".
    visual_bar = '#' * count

    # Print the character, its numerical count, and the visual bar.
    # f-strings (formatted string literals) are an easy way to embed
    # variables and expressions directly inside string literals.
    print(f"'{char}': {count} {visual_bar}")

# End of the script.
```
