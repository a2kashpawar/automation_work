```python
import random

# --- Mystical Orb Weaver ---
# This script takes your favorite word and transforms it into a unique,
# "mystical" string by weaving in random elements.
# It's a fun way to see how strings and lists can be manipulated!

# 1. Ask the user for their favorite word
favorite_word = input("Enter your favorite word: ").strip().lower()

# 2. Define a list of mystical symbols or prefixes/suffixes
mystical_elements = ["~*", "@", "#", "$", "%", "^", "&", "*", "+", "="]
prefix_options = ["gla", "fyn", "zyl", "quix", "blis"]
suffix_options = ["ian", "ora", "nium", "ium", "a", "x"]

# 3. Choose a random mystical element, prefix, and suffix
random_element = random.choice(mystical_elements)
random_prefix = random.choice(prefix_options)
random_suffix = random.choice(suffix_options)

# 4. Scramble the middle part of the user's word for extra mystique
#    We ensure the word is long enough to have a middle to scramble.
if len(favorite_word) > 2:
    # Get the first and last characters
    first_char = favorite_word[0]
    last_char = favorite_word[-1]
    
    # Extract the middle part as a list of characters
    middle_chars = list(favorite_word[1:-1])
    
    # Shuffle the middle characters randomly
    random.shuffle(middle_chars)
    
    # Join them back into a string
    scrambled_middle = "".join(middle_chars)
    
    # Reconstruct the word with scrambled middle
    transformed_word = first_char + scrambled_middle + last_char
else:
    # If the word is too short, we just use it as is
    transformed_word = favorite_word

# 5. Combine everything to create the final unique string
#    We capitalize the result for a more pronounced "mystical" look.
unique_mystical_string = (
    f"{random_element}{random_prefix}"
    f"{transformed_word}{random_suffix}{random_element}"
).capitalize()

# 6. Display the generated mystical string to the user
print("\nBehold! Your unique mystical orb string is:")
print(f"--- {unique_mystical_string} ---")
print("\nMay it bring you wonder and delight!")
```
