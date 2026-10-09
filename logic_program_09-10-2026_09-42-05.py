# A unique Python script to create a simple "wavy" text effect.

# Get some text input from the user.
user_text = input("Enter some text: ")

# Define how much the text will "wave" (maximum indentation).
max_wave_amplitude = 4

# Loop through each character in the user's input text.
# 'enumerate' gives us both the index (i) and the character (char).
for i, char in enumerate(user_text):
    # Calculate the current indentation level for the character.
    # The modulo operator (%) makes the wave pattern repeat.
    # It creates a sequence like: 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, ...
    wave_position = i % (max_wave_amplitude * 2)

    # Adjust the position to go back down after reaching the peak.
    if wave_position > max_wave_amplitude:
        indent_level = max_wave_amplitude * 2 - wave_position
    else:
        indent_level = wave_position

    # Create the leading spaces for the indentation.
    # String multiplication makes ' ' repeat 'indent_level' times.
    indent_spaces = " " * indent_level

    # Print the character with its calculated indentation.
    print(indent_spaces + char)
