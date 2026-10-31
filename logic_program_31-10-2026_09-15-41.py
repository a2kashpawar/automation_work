```python
import random # Import the 'random' module to use its functions for randomness

# Ask the user for their favorite color. This is an input from the user.
favorite_color = input("Enter your favorite color: ")

# Check if the user entered anything. If not, we'll use a default.
if not favorite_color:
    print("No color entered! Using 'blue' as default.")
    favorite_color = "blue"

# Generate a random "lucky number" between 1 and 100
lucky_number = random.randint(1, 100)

# Create a "secret phrase" by taking the first three letters of the color,
# then reversing the entire color, and adding the lucky number.
# This uses string slicing, string reversal, and f-strings.

# Get the first three letters of the color (or fewer if the color is short)
color_prefix = favorite_color[:3]

# Reverse the entire favorite color string
reversed_color = favorite_color[::-1]

# Combine everything into a unique "secret phrase" using an f-string (formatted string literal)
secret_phrase = f"Your secret phrase is: {color_prefix.upper()}-{reversed_color.lower()}-{lucky_number * 7}"

# Print the generated secret phrase to the console
print(secret_phrase)

# A little extra message for fun
print("\nRemember this phrase! It's... unique!")
```
