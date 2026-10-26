```python
import random # This line imports the 'random' module, which helps us pick things randomly.

# --- Welcome and Setup Your Custom Answers ---
print("🌟 Custom Fortune Teller 🌟")
print("Let's first create your own set of magical answers for the fortune teller!")

# This is an empty list where we will store all the answers you provide.
user_answers = []

# This 'while' loop will keep asking you for answers until you type 'done'.
while True:
    answer_text = input("Type an answer (e.g., 'Yes!', 'Maybe.', 'Outlook hazy.') or 'done' to finish: ")

    # Check if the user wants to stop adding answers.
    if answer_text.lower() == 'done': # .lower() makes input like "DONE", "Done", "done" all work.
        if not user_answers: # This checks if the list of answers is still empty.
            print("You need to provide at least one answer to start! Please try again.")
            continue # Go back to the beginning of the loop to ask for more answers.
        break # If answers exist, exit this loop.

    # Check if the user typed an empty answer (just spaces or nothing).
    elif answer_text.strip() == '': # .strip() removes any spaces from the start/end of the text.
        print("Empty answers aren't very magical! Please type something meaningful.")
        continue # Go back to the beginning of the loop.

    else:
        # If the input is a valid answer, add it to our list.
        user_answers.append(answer_text)
        print(f"'{answer_text}' added to your magic answers!") # f-string for easy printing.

print("\n--- Your Custom Fortune Teller is Ready! ---")
print("Ask a question, and it will pick one of your personalized answers.")

# --- Main Loop for Asking Questions ---
# This 'while' loop will keep running, allowing you to ask multiple questions.
while True:
    question = input("\nAsk your question (or type 'quit' to exit): ")

    # Check if the user wants to quit the game.
    if question.lower() == 'quit':
        print("Thanks for playing! May your custom fortunes be bright! ✨")
        break # Exit the main loop, ending the program.

    # If the user typed an empty question, remind them.
    if question.strip() == '':
        print("Please ask a real question to get an answer!")
        continue # Go back to the beginning of the loop.

    # Use 'random.choice()' to pick one answer randomly from our 'user_answers' list.
    selected_answer = random.choice(user_answers)

    # Print the user's question and the randomly selected answer.
    print(f"You asked: '{question}'")
    print(f"The Custom Fortune Teller says: {selected_answer}")
```
