# COLORPIE by Alexander Abraham
# a.k.a. "THE BLACK UNICORN".
# Licensed under the MIT license.
# This is the main module file.

# We need this import
# to determine the
# platform being used.
import os

# This function contains
# a dictionary of all
# ANSI sequences we need, to build
# colored strings.
def ansiPool():
    pool = {
      'prefix':'\033[1;',
      'suffixOne':'m',
      'suffixTwo':'\033[0m',
      'red':'31',
      'magenta':'35',
      'cyan':'36',
      'green':'32',
      'white':'37',
      'blue':'34',
      'black':'30',
      'yellow':'33'
    }
    return pool

# This function makes the console
# also accept ANSI sequenced strings.
def setup():
    if os.name == 'nt':
        from ctypes import windll
        kernel = windll.kernel32
        kernel.SetConsoleMode(
          kernel.GetStdHandle(-11), 7
        )
    else:
        pass

# This function returns  a colored string.
def getColoredString(string, color):
    setup()
    result = ansiPool()['prefix'] + color + ansiPool()['suffixOne'] + string + ansiPool()['suffixTwo']
    return result

# This function prints a colored string.
def printColoredString(string, color):
    setup()
    result = getColoredString(string,color)
    print(result)
