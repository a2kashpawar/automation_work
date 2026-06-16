```python
# This script takes a sentence and replaces certain words with emojis!

# A dictionary to map words to their corresponding emojis.
# Dictionaries store key-value pairs, perfect for lookups.
emoji_map = {
    "love": "❤️",  # If the word "love" is found, replace it with a red heart.
    "happy": "😊", # "happy" becomes a smiling face.
    "sad": "😔",   # "sad" becomes a pensive face.
    "hello": "👋", # "hello" becomes a waving hand.
    "dog": "🐶",   # "dog" becomes a dog face.
    "cat": "🐱"    # "cat" becomes a cat face.
}

# Get a sentence from the user.
# .lower() converts the entire input to lowercase, so "Love" still matches "love".
user_sentence = input("Type a sentence (e.g., 'I love my dog and feel happy'): ").lower()

# Split the sentence into individual words.
# .split() without arguments splits by any whitespace.
words_in_sentence = user_sentence.split()

# Create an empty list to store the words (or emojis) for our new sentence.
output_parts = []

# Loop through each word in the list of words from the user's sentence.
for word in words_in_sentence:
    # Check if the current word exists as a key in our emoji_map dictionary.
    if word in emoji_map:
        # If the word is found, add its corresponding emoji to our output list.
        output_parts.append(emoji_map[word])
    else:
        # If the word is not in our map, just add the original word.
        output_parts.append(word)

# Join all the items in the output_parts list back into a single string.
# " " is the separator used between the joined items.
converted_sentence = " ".join(output_parts)

# Print the final sentence with the emojis!
print("\nYour emoji sentence:")
print(converted_sentence)
```
