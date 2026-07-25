```python
# This script scrambles words in a sentence by shuffling their inner letters.
# The first and last letters of each word always stay in their original positions.

import random # We need the 'random' module for its shuffle functionality.

def scramble_word(word_to_scramble):
    """
    Shuffles the inner letters of a given word.
    Example: 'python' might become 'ptonhy' or 'pyhton'.
    Words with 3 or fewer letters are not scrambled.
    """
    # If the word is too short (3 letters or less), scrambling doesn't make sense.
    if len(word_to_scramble) <= 3:
        return word_to_scramble

    # Store the first letter of the word.
    first_letter = word_to_scramble[0]
    # Store the last letter of the word.
    last_letter = word_to_scramble[-1]

    # Extract the middle part of the word.
    # [1:-1] means from the second character (index 1) up to,
    # but not including, the last character (index -1).
    middle_letters_list = list(word_to_scramble[1:-1])

    # Randomly rearrange the order of the characters in the 'middle_letters_list'.
    random.shuffle(middle_letters_list)

    # Join the shuffled middle characters back into a single string.
    shuffled_middle_string = "".join(middle_letters_list)

    # Combine the first letter, the shuffled middle part, and the last letter.
    scrambled_result = first_letter + shuffled_middle_string + last_letter
    return scrambled_result

# --- Main part of the script starts here ---

# Ask the user to type a sentence they want to scramble.
user_sentence = input("Enter a sentence you'd like to scramble: ")

# Split the input sentence into individual words.
# The .split() method without arguments splits by any whitespace (spaces, tabs, newlines).
words_in_sentence = user_sentence.split()

# Create an empty list to store our scrambled words.
scrambled_words_output = []

# Loop through each word obtained from the user's sentence.
for current_word in words_in_sentence:
    # Call our 'scramble_word' function for the current word.
    scrambled_version = scramble_word(current_word)
    # Add the scrambled word to our list.
    scrambled_words_output.append(scrambled_version)

# Join all the scrambled words back together into a single sentence.
# We use " " as the separator to put spaces between the words.
final_scrambled_sentence = " ".join(scrambled_words_output)

# Print a clear output to the user.
print("\n--- Scrambling Complete ---")
print(f"Original:  {user_sentence}") # Using an f-string for easy display.
print(f"Scrambled: {final_scrambled_sentence}")
```
