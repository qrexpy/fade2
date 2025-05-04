# Fade2 🎨✨

A revamped version of [venaxyt's fade project](https://github.com/venaxyt/fade) with more features and improved stability. Fade2 allows you to add beautiful color gradients to your terminal text. 🌈

## Features 🚀

### Gradient Effects
- **Horizontal Gradients** - color transitions across each line
- **Linear Gradients** - smooth transitions across entire text
- **Vertical Gradients** - different colors for each line
- **Rainbow Effects** - smooth color spectrum transitions
- **Animated Effects** - dynamic color animations

### Technical Features
- Easy to use API
- Smooth color transitions using HSV color space
- Supports ANSI escape sequences on Windows
- Customizable gradient options

## Installation 📦

You can install Fade2 using pip:

```sh
pip install fade2
```

## Usage 🛠️

Here is an example of how to use Fade2 in your Python code:

```python
from fade2 import purplepink, rainbow, pulse

# Basic gradient
text = "Hello, World!"
colored_text = purplepink(text)
print(colored_text)

# Rainbow effect
rainbow_text = rainbow("""
    ╔═══════════════════════════╗
    ║  Smooth Rainbow Gradient  ║
    ╚═══════════════════════════╝
""")
print(rainbow_text)

# Animation effect (clears terminal)
pulse("This text will pulse with color!", cycles=2, delay=0.05)
```

## Function Reference 📚

### Horizontal Gradients

These functions apply a gradient across each line of text, character by character.

| Function | Description |
|----------|-------------|
| `blackwhite(text)` | Black to white gradient |
| `purplepink(text)` | Purple to pink gradient |
| `greenblue(text)` | Green to blue gradient |
| `pinkred(text)` | Pink to red gradient |
| `purpleblue(text)` | Purple to blue gradient |
| `water(text)` | Water-like blue gradient |
| `fire(text)` | Fire-like gradient |
| `brazil(text)` | Brazil flag colors gradient |
| `random(text)` | Random colors for each character |

### Linear Gradients

These functions apply a single gradient across the entire text.

| Function | Description |
|----------|-------------|
| `linear_blackwhite(text)` | Linear black to white gradient |
| `linear_purplepink(text)` | Linear purple to pink gradient |
| `linear_fire(text)` | Linear fire gradient |
| `linear_custom(starthex, endhex, text)` | Custom linear gradient using hex colors |

### Vertical Gradients

These functions apply different colors to each line.

| Function | Description |
|----------|-------------|
| `vertical_purplepink(text)` | Vertical purple to pink gradient |

### Rainbow Effects

| Function | Description |
|----------|-------------|
| `rainbow(text)` | Smooth rainbow color spectrum across text |

### Animated Effects

| Function | Description |
|----------|-------------|
| `pulse(text, cycles=3, delay=0.1)` | Creates a pulsing animation effect |

## Examples

### Rainbow Effect
```python
from fade2 import rainbow

banner = """
╔═══════════════════════════════════════════════╗
║                                               ║
║        Fade2 - Terminal Text Gradients        ║
║                                               ║
╚═══════════════════════════════════════════════╝
"""

print(rainbow(banner))
```

### Custom Linear Gradient
```python
from fade2 import linear_custom

# Blue to green gradient
text = "This is a custom gradient"
print(linear_custom("#0000FF", "#00FF00", text))
```

## License 📄

This project is licensed under the MIT License. See the LICENSE file for details.

## Author 👤

Created by [Qrexxed](https://github.com/qrexpy).

Enjoy using Fade2! 🎉
