from random import randint
from os import system
from time import sleep

def apply_color(text, color_func):
    system("")
    faded = ""
    for line in text.splitlines():
        faded += color_func(line) + "\033[0m\n"
    return faded

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def blackwhite(text):
    def color_func(line):
        red = green = blue = 0
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;{red};{green};{blue}m{char}"
            if red < 255:
                red = green = blue = min(255, red + 20)
        return faded_line
    return apply_color(text, color_func)

def purplepink(text):
    def color_func(line):
        red = 40
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;{red};0;220m{char}"
            if red < 255:
                red = min(255, red + 15)
        return faded_line
    return apply_color(text, color_func)

def greenblue(text):
    def color_func(line):
        blue = 100
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;0;255;{blue}m{char}"
            if blue < 255:
                blue = min(255, blue + 15)
        return faded_line
    return apply_color(text, color_func)

def pinkred(text):
    def color_func(line):
        blue = 255
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;255;0;{blue}m{char}"
            if blue > 0:
                blue = max(0, blue - 20)
        return faded_line
    return apply_color(text, color_func)

def purpleblue(text):
    def color_func(line):
        red = 110
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;{red};0;255m{char}"
            if red > 0:
                red = max(0, red - 15)
        return faded_line
    return apply_color(text, color_func)

def water(text):
    def color_func(line):
        green = 10
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;0;{green};255m{char}"
            if green < 255:
                green = min(255, green + 15)
        return faded_line
    return apply_color(text, color_func)

def fire(text):
    def color_func(line):
        green = 250
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;255;{green};0m{char}"
            if green > 0:
                green = max(0, green - 25)
        return faded_line
    return apply_color(text, color_func)

def brazil(text):
    def color_func(line):
        red = 0
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;{red};255;0m{char}"
            if red < 200:
                red = min(200, red + 30)
        return faded_line
    return apply_color(text, color_func)

def random(text):
    def color_func(line):
        faded_line = ""
        for char in line:
            faded_line += f"\033[38;2;{randint(0,255)};{randint(0,255)};{randint(0,255)}m{char}"
        return faded_line
    return apply_color(text, color_func)

def linear_blackwhite(text):
    system("")
    faded = ""
    length = len(text)
    for i, char in enumerate(text):
        gray = (255 * i) // length
        faded += f"\033[38;2;{gray};{gray};{gray}m{char}"
    faded += "\033[0m"
    return faded

def linear_purplepink(text):
    system("")
    faded = ""
    length = len(text)
    for i, char in enumerate(text):
        red = 40 + (215 * i // length)
        faded += f"\033[38;2;{red};0;220m{char}"
    faded += "\033[0m"
    return faded

def linear_fire(text):
    system("")
    faded = ""
    length = len(text)
    for i, char in enumerate(text):
        green = 250 - (250 * i // length)
        faded += f"\033[38;2;255;{green};0m{char}"
    faded += "\033[0m"
    return faded

def linear_custom(starthex, endhex, text):
    system("")
    start_rgb = hex_to_rgb(starthex)
    end_rgb = hex_to_rgb(endhex)
    faded = ""
    length = len(text)
    for i, char in enumerate(text):
        r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i // length
        g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i // length
        b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i // length
        faded += f"\033[38;2;{r};{g};{b}m{char}"
    faded += "\033[0m"
    return faded

def vertical_purplepink(text):
    system("")
    faded = ""
    lines = text.splitlines()
    length = len(lines)
    for i, line in enumerate(lines):
        red = 40 + (215 * i // length)
        faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
    return faded

__all__ = [
    "blackwhite", "purplepink", "greenblue", "pinkred", "purpleblue", "water", "fire", "brazil", "random",
    "linear_blackwhite", "linear_purplepink", "linear_fire", "linear_custom", "vertical_purplepink"
]