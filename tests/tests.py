# COLORPIE by Alexander Abraham
# a.k.a. "THE BLACK UNICORN".
# Licensed under the MIT license.
# This is the script to run tests
# for "Color Pie".

# Imports all functions
# from the "Color Pie"
# library.
import colorpie
from colorpie import *

# References the "getColoredString" function, iterates on
# the "ansiPool" function, instantiates a colored string variable
# with the test string "Hello World!", and prints the test string
# in all available colors.
def testColorFetching():
    string = 'Hello World!'
    for key in ansiPool():
        if key == 'suffixOne' or key == 'suffixTwo' or key == 'prefix':
            pass
        else:
            result = getColoredString(string, ansiPool()[key])
            print(result)

# References the "printColoredString" function, iterates on
# the "ansiPool" function, and prints out "Hello World!" in
# all available colors.
def testColorPrinting():
    string = 'Hello World!'
    for key in ansiPool():
        if key == 'suffixOne' or key == 'suffixTwo' or key == 'prefix':
            pass
        else:
            printColoredString(string, ansiPool()[key])

# References the "getEmoji" function, iterates on
# the "emojiPool" function, instantiates an emoji
# unicode string variable and prints this string
# variable out.
def testEmojiFetching():
    for key in emojiPool():
        result = getEmoji(emojiPool()[key])
        print(result)

# References the "printEmoji" function, iterates on
# the "emojiPool" function, and prints out the emoji
# with unicode sequennce "key" from the value of
# the dictionary provided by the "emojiPool" function.
def testEmojiPrinting():
    for key in emojiPool():
        printEmoji(emojiPool()[key])

# Main function to be run
# when the script is called.
def main():
    testColorFetching()
    testColorPrinting()
    testEmojiFetching()
    testEmojiPrinting()

# Main entry point for the
# Python interpreter.
if __name__ == '__main__':
    main()
