```python
# Import the 'random' module to pick items randomly from a list
import random

# A list of positive adjectives to describe good qualities
adjectives = ["Amazing", "Brilliant", "Creative", "Determined", "Fantastic", "Inspiring", "Radiant", "Vibrant"]

# A list of encouraging actions or states
actions = ["Embrace", "Cultivate", "Nurture", "Discover", "Unleash"]

# A list of positive concepts or aspects of oneself
concepts = ["your potential", "your strength", "your creativity", "your unique self", "your inner wisdom"]

# Randomly choose one adjective from the 'adjectives' list
chosen_adjective = random.choice(adjectives)

# Randomly choose one action verb from the 'actions' list
chosen_action = random.choice(actions)

# Randomly choose one concept from the 'concepts' list
chosen_concept = random.choice(concepts)

# Construct a motivational message using an f-string (formatted string literal)
# f-strings allow you to embed variables directly inside string literals by placing 'f' before the opening quote.
message = f"You are an {chosen_adjective} individual! Today, {chosen_action} {chosen_concept}."

# Print the generated motivational message to the console
print(message)
```
