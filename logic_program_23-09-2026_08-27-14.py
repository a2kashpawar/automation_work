```python
# Import the 'random' module to use its functions for picking random items
import random

# A list of items we might want to "collect" in our virtual backpack
possible_items = ["apple", "banana", "water bottle", "compass", "map", "flashlight", "rope", "sandwich"]

# The player's virtual backpack, starting empty
backpack = []

# Greet the player and explain the game
print("Welcome to the 'Pocket Scavenger' game!")
print("You'll find some items for your backpack.")
print("Let's see what you can collect!")

# Loop a few times to give the player chances to find items
for i in range(3): # This loop will run 3 times (for i=0, 1, 2)
    # Print the current round number (add 1 because 'i' starts at 0)
    print(f"\n--- Round {i + 1} ---")

    # Ask the user if they want to 'search' for an item
    # .lower() converts the input to lowercase for easier comparison
    action = input("Type 'search' to look for an item, or 'quit' to stop: ").lower()

    # Check the user's input
    if action == 'search':
        # Randomly choose an item from our 'possible_items' list
        found_item = random.choice(possible_items)

        # Add the found item to our backpack list
        backpack.append(found_item)

        # Tell the player what they found
        print(f"You searched and found a: {found_item}!")
        # Show the current contents of their backpack
        print(f"Your backpack now contains: {', '.join(backpack)}") # .join() makes a nice string from the list
    elif action == 'quit':
        # If the user wants to quit, break out of the loop early
        print("Quitting the game. Thanks for playing!")
        break # This keyword exits the current loop
    else:
        # If the user typed something else
        print("Invalid action. Please type 'search' or 'quit'.")

# After the loop finishes (either by completing all rounds or quitting)
# Print the final contents of the backpack
print("\n--- Game Over ---")
if backpack: # Check if the backpack is not empty
    print(f"Your final backpack contents: {', '.join(backpack)}")
    print(f"You collected a total of {len(backpack)} item(s).") # len() gives the number of items in the list
else:
    print("Your backpack is empty. Better luck next time!")
```
