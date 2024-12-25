# Fade2 🎨✨

A revamped version of [venaxyt's fade project](https://github.com/venaxyt/fade) with more features and improved stability. Fade2 allows you to add beautiful color gradients to your terminal text. 🌈

## Features 🚀

- Multiple color gradient functions:
  - `blackwhite`
  - `purplepink`
  - `greenblue`
  - `pinkred`
  - `purpleblue`
  - `water`
  - `fire`
  - `brazil`
  - `random`
  - `linear_blackwhite`
  - `linear_purplepink`
  - `linear_fire`
  - `linear_custom`
  - `vertical_purplepink`
- Easy to use
- Supports ANSI escape sequences on Windows

## Installation 📦

You can install Fade2 using pip:

```sh
pip install fade2
```

## Usage 🛠️

Here is an example of how to use Fade2 in your Python code:

```python
from fade2 import purplepink

text = "Hello, World!"
colored_text = purplepink(text)
print(colored_text)
```

## Functions 📚

### 

apply_color(text, color_func)



Applies a color function to the given text.

### 

blackwhite(text)



Applies a black and white gradient to the text.

### 

purplepink(text)



Applies a purple to pink gradient to the text.

### 

greenblue(text)



Applies a green to blue gradient to the text.

### 

pinkred(text)



Applies a pink to red gradient to the text.

### 

purpleblue(text)



Applies a purple to blue gradient to the text.

### 

water(text)



Applies a water-like gradient to the text.

### 

fire(text)



Applies a fire-like gradient to the text.

### 

brazil(text)



Applies a Brazil flag color gradient to the text.

### 

random(text)



Applies a random color gradient to the text.

### 

linear_blackwhite(text)



Applies a linear black to white gradient to the text.

### 

linear_purplepink(text)



Applies a linear purple to pink gradient to the text.

### 

linear_fire(text)



Applies a linear fire gradient to the text.

### 

linear_custom(starthex, endhex, text)



Applies a custom linear gradient to the text using the provided start and end hex colors.

### 

vertical_purplepink(text)



Applies a vertical purple to pink gradient to the text.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for details.

## Author 👤

Created by [Qrexxed](https://github.com/qrexpy).

Enjoy using Fade2! 🎉