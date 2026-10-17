```python
import time

# This script creates a simple countdown timer.

# Get the desired countdown duration from the user.
# The input() function reads text, and int() converts that text into a whole number.
countdown_duration = int(input("Enter countdown duration in seconds: "))

# Display a starting message.
print("\n--- Countdown Initiated ---")

# Loop backwards from the specified duration down to 1.
# range(start, stop, step) generates numbers.
# We go from 'countdown_duration' down to 1 (exclusive of 0), decreasing by 1 each time.
for seconds_left in range(countdown_duration, 0, -1):
    # Print the remaining time on the same line using '\r' (carriage return).
    # This makes the output overwrite itself instead of printing new lines.
    # An f-string (f"...") is used for easy variable insertion into the string.
    print(f"Time remaining: {seconds_left} seconds", end='\r')
    # Pause the script's execution for 1 second.
    time.sleep(1)

# After the loop finishes, print the final message.
# The '\n' ensures the "Time's up!" message appears on a new line after the countdown.
print("\n--- Countdown Complete! Time's up! ---")
```
