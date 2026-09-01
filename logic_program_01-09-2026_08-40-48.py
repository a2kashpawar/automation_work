```python
# This script creates a unique "nickname" by modifying a word you provide!

# 1. Ask the user to enter a word.
#    The 'input()' function waits for the user to type something and press Enter.
user_word = input("Enter a short word (like 'hello' or 'banana'): ")

# 2. Convert the word to lowercase for consistent processing.
#    '.lower()' is a string method that makes all characters lowercase.
user_word_lower = user_word.lower()

# 3. Check if the word is long enough to generate a good nickname.
#    'len()' tells us how many characters are in the string.
if len(user_word_lower) >= 3:
    # 4. Take the first two letters of the word.
    #    String slicing '[0:2]' means "start at index 0, up to (but not including) index 2".
    first_two_letters = user_word_lower[0:2]

    # 5. Take the last letter of the word.
    #    String indexing '[-1]' refers to the very last character.
    last_letter = user_word_lower[-1]

    # 6. Combine them with a fun suffix to create the unique nickname.
    #    The '+' operator concatenates (joins) strings.
    unique_nickname = first_two_letters + last_letter + "y-boo"

    # 7. Print the newly generated unique nickname.
    #    An f-string (formatted string literal) makes it easy to embed variables.
    print(f"Your unique word-nickname is: {unique_nickname.capitalize()}")
else:
    # 8. If the word is too short, provide a different, simpler nickname.
    print("That word is a bit too short for our special nickname generator!")
    print(f"But here's a cute nickname for '{user_word}': {user_word.capitalize()}kins!")

# End of script. Try running it multiple times with different words!
```
