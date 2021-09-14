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
def testFetching():
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
def testPrinting():
    string = 'Hello World!'
    for key in ansiPool():
        if key == 'suffixOne' or key == 'suffixTwo' or key == 'prefix':
            pass
        else:
            printColoredString(string, ansiPool()[key])

# Main function to be run
# when the script is called.
def main():
    testFetching()
    testPrinting()

# Main entry point for the
# Python interpreter.
if __name__ == '__main__':
    main()
