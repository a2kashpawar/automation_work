```python
# This script helps you think of a simple, unique pet name by combining two ideas!

def generate_pet_name(animal_type, favorite_snack):
    """
    Combines parts of an animal type and a favorite snack to create a new pet name.
    It takes the first two letters of the animal and the last two letters of the snack.
    """
    # Ensure inputs are strings and not too short
    if not isinstance(animal_type, str) or len(animal_type) < 2:
        animal_part = "An" # Default if animal_type is invalid
    else:
        animal_part = animal_type[:2].capitalize() # Get first two letters, capitalize them

    if not isinstance(favorite_snack, str) or len(favorite_snack) < 2:
        snack_part = "ack" # Default if favorite_snack is invalid
    else:
        snack_part = favorite_snack[-2:].lower() # Get last two letters, make them lowercase

    return animal_part + snack_part # Combine the parts into a new name

# --- Main part of the script ---

print("Welcome to the Pet Name Generator 3000!")
print("Let's create a unique name for your imaginary pet.")

# Get input from the user
user_animal = input("What kind of animal do you like? (e.g., 'Dog', 'Cat', 'Dragon'): ")
user_snack = input("What's a favorite snack of yours? (e.g., 'Cookie', 'Apple', 'Pizza'): ")

# Generate the pet name using our function
new_pet_name = generate_pet_name(user_animal, user_snack)

# Display the unique name
print(f"\nBased on your choices, a unique pet name could be: {new_pet_name}!")
print("Hope you like your new friend!")

```
