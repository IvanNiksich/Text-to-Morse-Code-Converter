""" Task description:
You will use what you've learnt to create a text-based (command line) program that takes any String input and
converts it into Morse Code.
You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you don't
remember what a text-base program looks like.
Wikipedia Entry for Morse Code
The design, functionality, code style is all up to you. You're wearing the big-girl/big-boy pants now. So you get to
decide.

Reflection Time:
This is a place to journal your experience of completing this project. This will help you figure out how to improve as
a developer.
Write down how you approached the project. What was hard, what was easy. How might you improve for the next project?
What was your biggest learning from today? What would you do differently if you were to tackle this project again?
"""

# Include


# Definitions

morse_dict = {"A": ".-",
              "B": "-...",
              "C": "-.-.",
              "D": "-..",
              "E": ".",
              "F": "..-.",
              "G": "--.",
              "H": "....",
              "I": "..",
              "J": ".---",
              "K": "-.-",
              "L": ".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--..",
              "0": "-----",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              ".": ".-.-.-",
              ",": "--..--",
              "?": "..--..",
              "'": ".----.",    # Carefull here
              "!": "-.-.--",
              "/": "-..-.",
              "(": "-.--.",
              ")": "-.--.-",
              "&": ".-...",
              ":": "---...",
              ";": "-.-.-.",
              "=": "-...-",
              "+": ".-.-.",
              "-": "-....-",
              "_": "..--.-",
              '"': ".-..-.",    # Carefull here
              "$": "...-..-",
              "@": ".--.-.",
              " ": " "  # space is space
              }

array_text_to_convert = []  # Initialize the array

# Program

# Get text to encode
print("Hello, this is a text to morse code converter.\n")
text_to_convert = input("Write the text you would like to convert and press enter.\n")

# Transform text to uppercase
text_to_convert = text_to_convert.upper()

# Split text into chars and store them in an array
for character in text_to_convert:
    array_text_to_convert.append(character)

# Go through the array translating every char with the morse_dict and store the translation in a second array


# Join translated array into a string to print as the result
# Look out for the " and ' conversion they might make a mess.

print(array_text_to_convert)
