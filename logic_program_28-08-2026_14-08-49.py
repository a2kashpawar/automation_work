# This script mixes two primary colors (red, yellow, blue) to form a new color.

# Get the first color from the user, converting it to lowercase for easy comparison.
color1 = input("Enter the first primary color (red, yellow, or blue): ").lower()

# Get the second color from the user, also converting it to lowercase.
color2 = input("Enter the second primary color (red, yellow, or blue): ").lower()

# Check if the two input colors are the same.
if color1 == color2:
    print("Mixing the same color doesn't create a new one!")
# Check if the combination is Red and Yellow (or Yellow and Red).
elif (color1 == "red" and color2 == "yellow") or \
     (color1 == "yellow" and color2 == "red"):
    print("Red and Yellow mix to make Orange!")
# Check if the combination is Red and Blue (or Blue and Red).
elif (color1 == "red" and color2 == "blue") or \
     (color1 == "blue" and color2 == "red"):
    print("Red and Blue mix to make Purple!")
# Check if the combination is Yellow and Blue (or Blue and Yellow).
elif (color1 == "yellow" and color2 == "blue") or \
     (color1 == "blue" and color2 == "yellow"):
    print("Yellow and Blue mix to make Green!")
# If the input colors are not recognized primary colors or a known mix.
else:
    print("Hmm, I only know how to mix Red, Yellow, and Blue primary colors!")
