# This script takes a word and prints it out as a growing pyramid, then shrinking, forming a diamond shape.

# 1. Ask the user for a word.
# The 'input()' function gets text from the user.
# The entered text is stored in the 'user_word' variable.
user_word = input("Please enter a word: ")

# 2. Print the word, letter by letter, growing longer.
# We use a 'for' loop to repeat actions.
# 'range(len(user_word))' creates a sequence of numbers from 0 up to (but not including) the length of the word.
# For example, if 'user_word' is "HELLO" (length 5), 'i' will be 0, 1, 2, 3, 4.
for i in range(len(user_word)):
    # 'user_word[:i+1]' is a "string slice".
    # It takes a part of the string from the beginning (index 0) up to (but not including) 'i+1'.
    # On the first loop (i=0), it prints 'user_word[:1]' which is the first letter.
    # On the second loop (i=1), it prints 'user_word[:2]' which is the first two letters, and so on.
    print(user_word[:i+1])

# 3. Print the word, letter by letter, shrinking shorter.
# We start from the second-to-last letter and go backwards down to the first letter.
# 'range(len(user_word) - 1, 0, -1)' means:
# - Start at 'len(user_word) - 1' (e.g., if word is 5 letters, start at index 4).
# - Stop before '0' (so the loop goes down to 1, meaning index 1).
# - Step by '-1' (count downwards).
for i in range(len(user_word) - 1, 0, -1):
    # Again, we use a string slice.
    # On the first loop (e.g., i=4), it prints 'user_word[:4]' (first four letters).
    # It continues shrinking until it prints 'user_word[:1]' (the first letter).
    print(user_word[:i])
