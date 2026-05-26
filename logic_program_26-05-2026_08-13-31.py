```python
import random # Import the 'random' module to use its shuffling capabilities

# Display a welcome message to the user
print("Welcome to the 'Pocket Decision Maker'!")
print("Having trouble making a simple choice? Let me help!")

# Get the first option from the user
option1 = input("Enter your first option: ")

# Get the second option from the user
option2 = input("Enter your second option: ")

# Create a list containing the two options provided by the user
choices = [option1, option2]

# Use random.choice() to pick one item randomly from the 'choices' list
chosen_option = random.choice(choices)

# Print the randomly selected decision to the user
print(f"\nMy decision is: {chosen_option}")

# Offer a concluding friendly message
print("Hope that helped simplify your day!")
```
