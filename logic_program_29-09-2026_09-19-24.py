```python
import random # Import the 'random' module to pick random items from a list

# Define a list of possible "subjects" for our micro-story
subjects = ["The curious cat", "A forgotten teacup", "The secret button", "A tiny robot", "The old oak tree"]

# Define a list of possible "actions"
actions = ["discovered a hidden path", "whispered a strange name", "found a shimmering key", "learned to fly", "baked a truly enormous cookie"]

# Define a list of possible "outcomes" or "details"
outcomes = ["under the moonlight.", "just before sunrise.", "in a dusty attic.", "with a sprinkle of stardust.", "while humming a forgotten tune."]

# Randomly choose one item from each list
chosen_subject = random.choice(subjects)
chosen_action = random.choice(actions)
chosen_outcome = random.choice(outcomes)

# Combine the chosen parts into a single, short story using an f-string
# f-strings are a modern way to embed variables directly inside string literals.
micro_story = f"{chosen_subject} {chosen_action} {chosen_outcome}"

# Print a friendly message and then the generated micro-story
print("--- Your Whimsical Micro-Story ---")
print(micro_story)
print("----------------------------------\n")

# This line waits for the user to press Enter before the script finishes.
# It's useful when running from a terminal so the output doesn't disappear immediately.
input("Press Enter to imagine the rest...")
```
