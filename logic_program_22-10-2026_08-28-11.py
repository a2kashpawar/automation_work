```python
import random # We need this module to shuffle our list later

# This script creates a simple "list mixer" or "random item picker".
# It lets you input several items, then randomly picks one for you.
# Great for deciding which chore to do, which movie to watch, etc.!

print("Welcome to the Random Item Picker!")
print("Enter items one by one. Type 'done' when you're finished.")

items_list = [] # Initialize an empty list to store all the items

# Start a loop to continuously ask for items until the user types 'done'.
while True:
    # Get input from the user for an item.
    user_input = input("Enter an item (or type 'done'): ")

    # Check if the user wants to stop adding items.
    if user_input.lower() == 'done': # .lower() makes the check case-insensitive
        break # Exit the while loop

    # Check if the input is not empty before adding it.
    if user_input:
        items_list.append(user_input) # Add the entered item to our list
    else:
        print("Oops! Please enter something or 'done'.")

# Check if the list has any items before trying to pick one.
if not items_list: # This condition is true if the list is empty
    print("You didn't enter any items to pick from. Goodbye!")
else:
    print("\nOkay, let's pick one for you...")

    # Use random.choice() to pick a single item randomly from the list.
    chosen_item = random.choice(items_list)

    print(f"The random choice is: '{chosen_item}'") # An f-string for clear output
    print("Hope that helps you decide!")

print("Thank you for using the Random Item Picker!")
```
