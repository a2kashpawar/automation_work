```python
# Welcome to the Python Pet Name Generator!
# This script will ask you for your favorite color and a funny adjective,
# then combine them to create a unique and silly pet name.

print("Let's create a fun pet name for you!")
print("------------------------------------")

# Step 1: Ask the user for their favorite color.
# The 'input()' function pauses the script and waits for the user to type something,
# then returns whatever they typed as a string (text).
favorite_color = input("What's your favorite color? (e.g., 'Blue', 'Sparkly'): ")

# Step 2: Ask for a funny adjective.
# We store this in another variable. Variables are like containers for data.
funny_adjective = input("Give me a funny adjective! (e.g., 'Wobbly', 'Squishy'): ")

# Step 3: Create the pet name by combining the inputs.
# We use an f-string (formatted string literal) to easily insert variable values
# directly into a string. The 'title()' method makes the first letter of each word
# uppercase, which looks nice for names.
pet_name_suggestion = f"{funny_adjective.title()} {favorite_color.title()}kins"

# Step 4: Display the generated pet name to the user.
# The 'print()' function displays text (and variable values) on the screen.
print("\n") # This prints an empty line for better readability.
print("Your unique and wonderful pet name suggestion is...")
print("-------------------------------------------------")
print(f"       ⭐ {pet_name_suggestion}! ⭐")
print("\nEnjoy your new pet name!")
```
