# Import the 'random' module to allow the script to make random choices.
import random

# Define lists of words for different parts of a sentence.
# Beginners learn about variables and basic data structures like lists.
characters = ["A mischievous imp", "The grumpy old wizard", "A shiny new robot", "A curious cat", "A brave astronaut"]
actions = ["discovered", "chased", "whispered to", "built", "explored"]
items = ["a hidden key", "the last slice of pizza", "a glowing crystal", "an ancient map", "a broken time machine"]
locations = ["in a forgotten attic", "under a starry sky", "atop a giant mushroom", "inside a secret laboratory", "by the calm lake"]

# Randomly select one element from each list.
# This demonstrates using 'random.choice()' to pick an item from a list.
chosen_character = random.choice(characters)
chosen_action = random.choice(actions)
chosen_item = random.choice(items)
chosen_location = random.choice(locations)

# Combine the chosen words into a complete sentence using an f-string.
# F-strings are a user-friendly way to embed variables directly into strings.
story_prompt = f"{chosen_character} {chosen_action} {chosen_item} {chosen_location}."

# Print the generated story prompt to the console.
# This shows the user the output of the script.
print("Here's your unique story idea:")
print(story_prompt)
