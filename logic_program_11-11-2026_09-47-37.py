```python
# This script generates a unique "fortune" based on your favorite number!

# The 'input()' function asks the user for information and stores it.
# We use 'int()' to convert the user's text (a string) into a whole number (an integer).
favorite_number = int(input("Enter your favorite whole number: "))

# The modulo operator (%) gives us the remainder of a division.
# This helps us create different outcomes based on the number.
remainder = favorite_number % 3

# We use 'if', 'elif' (else if), and 'else' to create conditional logic.
# The 'print()' function displays text on the screen.

if remainder == 0:
    # If the number is perfectly divisible by 3 (remainder is 0)
    print(f"\nYour number {favorite_number} suggests: A new adventure awaits you very soon!")
elif remainder == 1:
    # If the remainder is 1 when divided by 3
    print(f"\nYour number {favorite_number} suggests: Today is a great day to learn something new!")
else: # remainder == 2
    # If the remainder is 2 (any other case, since it's % 3)
    print(f"\nYour number {favorite_number} suggests: Expect a pleasant surprise when you least expect it!")

# This script demonstrates input, type conversion, basic arithmetic, and conditional statements.
# Try running it multiple times with different favorite numbers!
```
