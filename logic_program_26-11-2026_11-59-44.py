```python
import time # Import the 'time' module to allow pausing the script.

# Define a variable for our "pet" character.
pet_char = "(^o^)"

# Define a variable for how many steps our pet will "walk".
walk_steps = 15

print("Let's take our little pet for a walk!")
time.sleep(1) # Pause for 1 second.

# Loop a certain number of times to simulate walking.
for step in range(walk_steps):
    # Print multiple empty lines to make it look like the screen is clearing.
    # This pushes the previous pet position up, creating a movement effect.
    print("\n" * 10)

    # Print spaces before the pet to make it appear to move across the screen.
    # 'step' increases in each loop, so the pet moves further to the right.
    print(" " * step + pet_char)

    # Print a simple "ground" line beneath the pet.
    print("-" * (walk_steps + len(pet_char))) # Ground length adjusts with walk distance.

    # Pause for a short moment before the next step.
    # This creates the animation effect; without it, it would just flash the final position.
    time.sleep(0.15)

print("\nOur pet finished its walk! Say hello!")
# You can uncomment the line below if you want the user to press Enter to exit.
# input("Press Enter to say goodbye...")
```
