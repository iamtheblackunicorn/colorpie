# COLOR PIE

***Make the snake discover the rainbow!***

![CI](https://github.com/iamtheblackunicorn/colorpie/actions/workflows/python.yml/badge.svg)

## ABOUT

Since I've never seen the point in making things uselessly complicated and I quite like printing colored strings
to the console in my applications, I decided to write a library that would let me do just that. I know projects like
***Colorama*** have already solved this problem and give people more options but this is for the simple folks among us.

## FEATURES

- Fast and easy to use!
- Simple project structure!
- Optimized for performance!
- Works on every platform!

## INSTALLATION

You should make sure you have the following tools installed:

- Python 3+
- Pip for Python 3+
- Git

If you have these installed, also make sure that they are on
your path.

To install the latest development version of ***Color Pie***, run this command in a command-line prompt:

```bash
$ pip install git+https://github.com/iamtheblackunicorn/colorpie#egg=colorpie
```

To install the latest stable release of ***Color Pie***, run this command in a command-line prompt:

```bash
$ pip install colorpie
```

## USAGE

To use ***Color Pie*** in your projects, simply import it like this:

```python
import colorpie
```

### COLORS

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

Please make sure that you call any of the colors listed below with a ***SMALL*** first letter. If you do not, an exception will be thrown.

Currently supported colors are:

- Red
- Magenta
- Cyan
- Green
- White
- Blue
- Black
- Yellow

### EMOJIS

If you want to use a certain emoji in your project, you may do so with the help of two methods!
The `getEmoji` method and the `printEmoji` method.

If you want to just place an emoji somewhere in a string, you can do this best by using the `getEmoji` method like this:

```python
from colorpie import getEmoji
myEmoji = getEmoji('catFace')
# There's a cat face emoji in this variable now.
```

If you want to just print an emoji somewhere, you can do this best by using the `printEmoji` method like this:

```python
from colorpie import printEmoji
printEmoji('catFace')
# A cat face emoji is printed.
```

For a complete list of the emoji name strings, check the table below:

#### Faces

- `grinningFace`
- `laughCry`
- `upsideDownFace`
- `heartsInFace`
- `smilingFace`
- `haloFace`
- `winkingFace`
- `kissingFace`
- `angryFace`
- `crazyFace`
- `thinkingFace`
- `naughtyface`

#### Animals

- `seeNoEvil`
- `animalGorilla`
- `windCloud`
- `sweatDroplets`
- `dogFace`
- `unicornHead`
- `catFace`
- `horseHead`
- `pandaFace`
- `bearFace`
- `tigerFace`

#### Symbols

- `redHeart`
- `blackHeart`
- `backArrow`
- `soonArrow`
- `topArrow`
- `infinitySign`
- `multiplySign`
- `plusSign`
- `divideSign`
- `minusSign`
- `tickSign`

#### Tools

- `kitchenKnife`
- `scissors`
- `bomb`
- `gun`
- `hammer`
- `wrench`
- `hammerAndWrench`
- `hammerAndPick`
- `pick`
- `woodSaw`
- `axe`

#### Pride

- `prideFlag`
- `transFlag`
- `rainbow`
- `peopleKissing`
- `party`
- `coupleHeart`
- `sparkles`
- `confetti`
- `maleBunnies`
- `kiss`

#### Art

- `yarn`
- `headPhones`
- `piano`
- `bowAndArrow`
- `paintBrush`
- `paintPalette`
- `sewingNeedle`
- `threadRoll`
- `syringe`
- `pill`

## CHANGELOG

### Version 1.0.0: Initial release

- initial release
- upload to GitHub

### Version 2.0.0: Documentation update

- Visual optimizations for PyPi
- Better and more in-depth documentation

### Version 3.0.0: The Emoji Update!

- This update brings a set of 66 select emojis in 6 categories to your terminal.
- Speed and documentation optimizations.

## NOTE

- ***Color Pie*** by Alexander Abraham a.k.a. "The Black Unicorn"
- Licensed under the MIT license.
