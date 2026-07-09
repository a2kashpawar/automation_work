```python
# This script creates a tiny, interactive "echo machine" for a favorite thing!

# 1. Ask the user for their favorite hobby.
# The input() function waits for the user to type something and press Enter.
favorite_hobby = input("What is one of your favorite hobbies? ")

# 2. Ask for a short, enthusiastic word related to that hobby.
enthusiastic_word = input(f"Now, think of a short, exciting word about '{favorite_hobby}': ")

# 3. Ask how many times to "echo" the enthusiastic word.
# input() always returns a string, so we use int() to convert it to a number.
repeat_times_str = input(f"How many times should we echo '{enthusiastic_word}'? (Enter a number, e.g., 3): ")
repeat_times = int(repeat_times_str) # Convert string to an integer

# 4. Print a header for the output.
print("\n--- Your Hobby Echo ---")
print(f"Hobby: {favorite_hobby}")

# 5. Use a loop to print the enthusiastic word multiple times.
# The range() function generates numbers from 0 up to (but not including) repeat_times.
for i in range(repeat_times):
    # f-strings (formatted string literals) make it easy to embed variables.
    # The `i+1` makes the count start from 1 instead of 0.
    print(f"  {i+1}. {enthusiastic_word.upper()}!") # .upper() makes the word uppercase for emphasis

# 6. Add a closing message.
print("-----------------------\n")
print("Keep enjoying your hobby!")
```
