```python
# This script acts as a simple digital fortune teller.

import random # We need this to pick random answers.

def get_fortune():
    """Returns a random fortune from a predefined list."""
    # This is a list of possible fortunes.
    fortunes = [
        "A pleasant surprise awaits you soon.",
        "Your hard work will pay off in unexpected ways.",
        "Embrace new opportunities; they hold great potential.",
        "Someone special is thinking of you.",
        "Today is a good day to learn something new.",
        "Seek joy in the small moments.",
        "Patience is key to your next success.",
        "A creative idea will spark your imagination."
    ]
    # random.choice picks one item randomly from the list.
    return random.choice(fortunes)

# --- Main part of the script ---

print("Welcome, seeker of wisdom!")
print("Ask a yes/no question in your mind, then press Enter to reveal your fortune.")

# This line waits for the user to press the Enter key.
input("Press Enter to receive your fortune...")

# Call our function to get a random fortune.
your_fortune = get_fortune()

# Print the result to the user using an f-string for easy formatting.
print("\nYour fortune is:")
print(f"✨ {your_fortune} ✨")

print("\nMay your path be clear!")
```
