```python
# This script takes a sentence and reverses each word individually,
# while keeping the original order of the words in the sentence.

# Get a sentence from the user as input
# The input() function reads a line from the user
original_sentence = input("Please enter a sentence: ")

# Split the sentence into a list of words
# The .split() method, when called without arguments, splits by any whitespace
words = original_sentence.split()

# Create an empty list to store the words after they've been reversed
reversed_words_list = []

# Loop through each word in the 'words' list
for word in words:
    # Reverse the current word using string slicing
    # [::-1] creates a reversed copy of the string
    reversed_word = word[::-1]
    # Add the newly reversed word to our list
    reversed_words_list.append(reversed_word)

# Join the list of reversed words back into a single string (a new sentence)
# The ' ' between .join() means a space will be placed between each word
final_reversed_sentence = ' '.join(reversed_words_list)

# Print the original sentence and the new sentence with reversed words
print("\nOriginal sentence:")
print(original_sentence)
print("\nSentence with each word reversed:")
print(final_reversed_sentence)
```
