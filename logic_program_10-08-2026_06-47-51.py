```python
# This script helps you choose a fun activity for a short break!

import random # We need the 'random' module to pick an activity for us.

# Here's a list of quick, easy activities.
break_activities = [
    "Stretch for 5 minutes.",
    "Listen to one song.",
    "Drink a glass of water.",
    "Look out a window for 2 minutes.",
    "Do 10 jumping jacks.",
    "Write down one positive thought.",
    "Tidy up your immediate space.",
    "Pet your cat/dog (if you have one!)."
]

# Pick one random activity from our list.
chosen_activity = random.choice(break_activities)

# Tell the user what they should do!
print("--- Time for a quick break! ---")
print("How about you:")
print(f"- {chosen_activity}") # An f-string lets us easily put variables into our text.
print("-----------------------------")
print("Enjoy your short refresh!")
```
