```python
# This short script generates a simple, personalized text banner.
# It's a great way to see how Python handles strings and user input!

import sys # We'll use this module for a slight pause at the end

# 1. Get the main text for the banner from the user.
# The 'input()' function waits for the user to type something and press Enter.
banner_text = input("Enter your text for the banner: ")

# 2. Get a single character that will be used for the banner's border.
# We take only the first character typed to keep the border consistent.
border_char_raw = input("Enter a single character for the border (e.g., *, #, =): ")
border_char = border_char_raw[0] if border_char_raw else '-' # Use '-' if user enters nothing

# 3. Calculate the total width of the banner.
# We add 4 to the text length: 2 characters for the border and 2 spaces on each side.
banner_width = len(banner_text) + 4

# 4. Print the top border line.
# Python allows multiplying a string by an integer to repeat it!
print(border_char * banner_width)

# 5. Print the line containing the user's text.
# An f-string (formatted string literal) is an easy way to embed variables into strings.
print(f"{border_char} {banner_text} {border_char}")

# 6. Print the bottom border line (same as the top).
print(border_char * banner_width)

# 7. Add a small interactive touch: a short pause before exiting.
# This makes the output stay visible for a moment in some environments.
print("\nYour custom banner is displayed!")
input("Press Enter to exit...") # Wait for user to press Enter
sys.exit() # Gracefully exit the script
```
