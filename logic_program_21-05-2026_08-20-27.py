```python
# This script tells you a 'fortune' based on a secret number.
# It's a fun way to learn about user input and basic logic!

# First, let's ask the user for a number.
# We use int() to convert their text input into a whole number.
try:
    user_number = int(input("Enter a whole number between 1 and 10: "))
except ValueError:
    print("That's not a valid number! Please try again.")
    # We'll just exit if they don't enter a number, keeping it simple.
    exit()

# Now, let's use some 'if/elif/else' statements to give a different message
# based on their number. This is called conditional logic.

print("\n--- Your Fortune ---")

if user_number == 7:
    print("You picked the lucky number 7! Expect good news soon!")
elif user_number == 1:
    print("Number 1! You are destined for greatness and new beginnings.")
elif user_number % 2 == 0: # The '%' is the modulo operator, it gives the remainder.
                           # If remainder is 0, it's an even number.
    print("An even number! Your path is balanced and steady.")
elif user_number % 2 != 0: # If remainder is not 0, it's an odd number.
    print("An odd number! Prepare for exciting, unexpected adventures!")
else:
    # This 'else' catches any other numbers, though with the previous checks,
    # it might only run if someone inputs text and the try-except isn't perfect,
    # or if the number is outside 1-10 but still an integer.
    print("Every number has its charm. Keep exploring!")

print("--- End of Fortune ---")

# This is a simple script that demonstrates:
# - Getting input from the user (input())
# - Converting input to a number (int())
# - Handling potential errors (try-except)
# - Making decisions based on values (if/elif/else)
# - Using arithmetic operators (%, ==, !=)
```
