```python
# This script generates a tiny, unique "word soup" based on your input!

# First, we ask the user for a word and store it in a variable called 'noun'.
# The input() function gets text from the user.
noun = input("Please type a plural noun (e.g., 'shoes', 'clouds'): ")

# Next, we ask for an adjective (a descriptive word).
# We'll store this in the 'adjective' variable.
adjective = input("Now, give me a silly adjective (e.g., 'fuzzy', 'bouncy'): ")

# Then, we ask for a verb that ends with '-ing'.
# This will be stored in the 'verb_ing' variable.
verb_ing = input("And finally, a verb ending in '-ing' (e.g., 'singing', 'flying'): ")

# We'll ask for a number. The int() function converts the text input into a whole number.
lucky_number = int(input("Pick a small, whole number (e.g., 3, 7): "))

# Now, let's create a unique phrase using all the inputs!
# We use an f-string (formatted string literal) to easily embed variables into the text.
# The '{noun.upper()}' converts the user's noun to ALL CAPS before inserting it.
phrase_part1 = f"Beware the {adjective} {noun.upper()}!"

# Let's add a numerical twist based on the lucky number.
# The multiplication '*' operator repeats the string.
phrase_part2 = f"They are always {verb_ing} " + ("super " * lucky_number) + "loudly."

# Finally, we print the complete, whimsical word soup!
print("\n--- Your Custom Word Soup! ---")
print(phrase_part1)
print(phrase_part2)
print("----------------------------")

# Try running this script multiple times with different words!
```
