```python
import time # Import the 'time' module to pause our script
import os   # Import the 'os' module to clear the console screen

# --- Settings for our pulsing message ---
message_text = "Python is Fun!" # The message we want to display
pulse_char = "*"               # The character used for the pulse animation
min_padding = 1                # Minimum number of spaces around the message
max_padding = 5                # Maximum number of spaces for the pulse effect
animation_speed = 0.1          # How fast the pulse animation plays (seconds per frame)

# --- Animation Logic ---

# Loop indefinitely to keep the animation running
while True:
    # Animate growing the pulse (padding increases)
    for padding in range(min_padding, max_padding + 1):
        # Create the left and right pulse string
        pulse_effect = pulse_char * padding
        
        # Combine the pulse, a space, the message, another space, and the pulse again
        # This forms our full animated string
        animated_line = f"{pulse_effect} {message_text} {pulse_effect}"
        
        # Print the current frame of the animation
        print(animated_line)
        
        # Pause for a short duration to make the animation visible
        time.sleep(animation_speed)
        
        # Clear the console screen for the next frame
        # 'cls' is for Windows, 'clear' is for macOS/Linux
        os.system('cls' if os.name == 'nt' else 'clear')

    # Animate shrinking the pulse (padding decreases)
    for padding in range(max_padding, min_padding - 1, -1): # Loop from max down to min
        # Create the left and right pulse string
        pulse_effect = pulse_char * padding
        
        # Combine the pulse, a space, the message, another space, and the pulse again
        animated_line = f"{pulse_effect} {message_text} {pulse_effect}"
        
        # Print the current frame of the animation
        print(animated_line)
        
        # Pause for a short duration to make the animation visible
        time.sleep(animation_speed)
        
        # Clear the console screen for the next frame
        os.system('cls' if os.name == 'nt' else 'clear')
```
