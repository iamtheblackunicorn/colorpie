# COLOR PIE :art: :pie:

***Make the snake discover the rainbow!*** :art: :pie:

![CI](https://github.com/iamtheblackunicorn/colorpie/actions/workflows/python.yml/badge.svg)

## ABOUT :books:

Since I've never seen the point in making things uselessly complicated and I quite like printing colored strings
to the console in my applications, I decided to write a library that would let me do just that. I know projects like
***Colorama*** have already solved this problem and give people more options but this is for the simple folks among us.

## FEATURES :test_tube:

- fast and easy to use
- simple project structure
- optimized for performance

## INSTALLATION :inbox_tray:

You should make sure you have the following tools installed:

- Python 3+
- Pip for Python 3+
- Git

If you have these installed, also make sure that they are on
your path. To install ***Color Pie***, run this command in a command-line prompt:
```bash
$ pip install git+https://github.com/iamtheblackunicorn/colorpie#egg=colorpie
```

## USAGE :hammer:

To use ***Color Pie*** in your projects, simply import it like this:

```python
import colorpie
```

To get a string of a certain color from an existing string use the library's functions like this:

```python
from colorpie import getColoredString
myColoredString = getColoredString('Hello World!', 'red')
```

To print a string of a certain color from an existing string use the library's functions like this:

```python
from colorpie import printColoredString
printColoredString('Hello World!', 'red')
```

Currently supported colors are:

- Red
- Magenta
- Cyan
- Green
- White
- Blue
- Black
- Yellow

## CHANGELOG :black_nib:

### Version 1.0.0: Initial release

- initial release
- upload to GitHub

## NOTE :scroll:

- ***Color Pie*** :art: :pie: by Alexander Abraham :black_heart: a.k.a. "The Black Unicorn" :unicorn_head:
- Licensed under the MIT license.
