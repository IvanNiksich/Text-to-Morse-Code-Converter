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
              # "¿": "..-.-",     # Not really morse code?
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
              # " ": " "  # space is space
              " ": "/",   # Space symbol in Morse
              "#": "......",
              "%": "-----.-",
              "*": "-.-.-",
              "^": ".-.-.",
              "<": "-.--.",
              ">": "-.--.-",
              "{": "-.-..",
              "}": "-.-.-",
              "[": "-.-..",
              "]": "-.-.-",
              "\\": "-..-.",
              "|": ".-.-.-",
              "~": ".-...-",
              "`": ".-..-.",
              }

array_text_to_convert = []  # Initialize the array
array_morse_text = []


def get_text():
    # Get text to encode
    text_to_convert = input("Write the text you would like to convert and press enter.\n")

    # Transform text to uppercase
    text_to_convert = text_to_convert.upper()

    # Split text into chars and store them in an array
    for character in text_to_convert:
        array_text_to_convert.append(character)
    return None


def convert_text():
    for element in array_text_to_convert:
        try:
            array_morse_text.append(morse_dict[element])
            array_morse_text.append(" ")
        except KeyError:
            print(f"Sorry, '{element}' is not supported by this program. We only support ASCI symbols.")
            # Clear the arrays
            array_text_to_convert.clear()
            array_morse_text.clear()
            # Get a new text to convert
            get_text()
            convert_text()
            return None
    return None


# Program

# Get text to encode and process it
print("Hello, this is a text to morse code converter.\n")
get_text()

# Go through the array translating every char with the morse_dict and store the translation in a second array
convert_text()

# Join translated array into a string to print as the result
morse_text = "".join(array_morse_text)

# Look out for the " and ' conversion they might make a mess.
print(morse_text)
