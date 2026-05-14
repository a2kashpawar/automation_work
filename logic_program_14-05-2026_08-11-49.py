```python
# A unique script to generate a simple emoji based on your mood!

# 1. Ask the user for their current feeling.
# The .lower() method makes the input case-insensitive (e.g., 'Happy' becomes 'happy').
current_mood = input("How are you feeling today? (e.g., happy, sad, surprised, thoughtful, winking): ").lower()

# 2. Initialize default emoji components.
# These will be used if the mood is not recognized.
left_eye = "o"
mouth = "-"
right_eye = "o"

# 3. Use conditional logic (if/elif/else) to change components based on the mood.
if current_mood == "happy":
    left_eye = ":"
    mouth = "D"
    right_eye = "" # For simplicity, some emojis don't need a distinct right eye character.
elif current_mood == "sad":
    left_eye = ":"
    mouth = "("
    right_eye = ""
elif current_mood == "surprised":
    left_eye = "o"
    mouth = "O"
    right_eye = "o"
elif current_mood == "thoughtful":
    left_eye = ":"
    mouth = "-"
    right_eye = "." # A period can represent thinking.
elif current_mood == "winking":
    left_eye = ";"
    mouth = ")"
    right_eye = ""
elif current_mood == "angry":
    left_eye = ">"
    mouth = "<"
    right_eye = ""
else:
    # If the mood is not recognized, print a message and use the default components.
    print("Hmm, I don't know that feeling. Here's a default emoji!")

# 4. Assemble the emoji using an f-string (formatted string literal).
# This is a modern and readable way to combine strings and variables.
final_emoji = f"{left_eye}{mouth}{right_eye}"

# 5. Print the generated emoji to the console.
print("\nHere's your custom emoji:")
print(final_emoji)

# A friendly reminder to the user.
print("\n(Run the script again to try a different mood!)")
```
