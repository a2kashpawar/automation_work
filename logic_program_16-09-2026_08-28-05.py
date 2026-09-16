```python
# Import the time module to add a delay
import time

# Define the number of steps for our text-based progress bar
total_steps = 25

# Character to represent the filled part of the bar
filled_char = '▓' # You can also use '█', '#', or any character

# Character to represent the empty part of the bar
empty_char = '░' # You can also use '-', '.', or ' '

# Loop through each step from 0 to total_steps
for step in range(total_steps + 1):
    # Calculate the current percentage of completion
    percentage = (step / total_steps) * 100

    # Create the filled portion of the progress bar
    # String multiplication repeats the character 'step' times
    filled_bar = filled_char * step

    # Create the empty portion of the progress bar
    # The remaining length is (total_steps - step)
    empty_bar = empty_char * (total_steps - step)

    # Combine the filled and empty parts into one bar string
    progress_bar = f"[{filled_bar}{empty_bar}]"

    # Print the progress bar and percentage.
    # '\r' (carriage return) moves the cursor to the beginning of the line,
    # overwriting previous output on the same line.
    # 'end=""' prevents print from adding a new line character,
    # keeping subsequent prints on the same line.
    print(f"\rAdvancing... {progress_bar} {percentage:.1f}%", end="")

    # Pause for a short duration to simulate work being done
    time.sleep(0.08)

# After the loop finishes, print a final message.
# The '\n' ensures the next output starts on a new line.
print("\nJourney complete!")
```
