```python
# This script generates a personalized, magical "fortune" based on your input!

# Ask the user for their first name.
name = input("What's your adventurer's name? ")

# Ask for their favorite magical artifact.
# This could be anything like "wand", "amulet", "cloak", etc.
artifact = input("And your most treasured magical artifact (e.g., 'wand', 'amulet', 'cloak')? ")

# Ask for a significant number.
# We'll try to convert it to an integer.
lucky_num_str = input("Finally, a significant number for your quest: ")

# Attempt to convert the input to a number.
# This introduces basic error handling for beginners.
try:
    lucky_number = int(lucky_num_str)
except ValueError:
    print("\nThat wasn't a valid number, so we'll use 7 instead!")
    lucky_number = 7 # Default if input is not a number

# Create a unique fortune using the collected information.
# We use f-strings for easy variable embedding and string methods like .upper() and .capitalize().
fortune = f"Brave {name.capitalize()}, your destiny unfolds! With your mighty {artifact.upper()}, you shall discover {lucky_number * 2} hidden secrets."

# Print the personalized fortune to the user.
print("\n--- Your Enchanted Scroll Reveals ---")
print(fortune)
print("--------------------------------------")

# A little closing message.
print("\nMay your path be filled with wonder!")
```
