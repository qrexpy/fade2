from random import randint
from os import system
from time import sleep

# Constants
RESET_CODE = "\033[0m"

# Utility functions
def hex_to_rgb(hex_color):
    """Convert a hex color string to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_ansi(r, g, b, char):
    """Convert RGB values to an ANSI-colored character."""
    return f"\033[38;2;{r};{g};{b}m{char}"

def apply_color(text, color_func):
    """Apply a color function to each line of text."""
    system("")  # Enable ANSI escape sequences on Windows
    faded = ""
    for line in text.splitlines():
        faded += color_func(line) + RESET_CODE + "\n"
    return faded

def apply_linear_gradient(text, color_map_func):
    """Apply a linear gradient across an entire text."""
    system("")  # Enable ANSI escape sequences on Windows
    faded = ""
    length = len(text)
    
    for i, char in enumerate(text):
        color = color_map_func(i, length)
        faded += rgb_to_ansi(*color, char)
        
    return faded + RESET_CODE

def apply_vertical_gradient(text, color_map_func):
    """Apply a gradient vertically, one color per line."""
    system("")  # Enable ANSI escape sequences on Windows
    faded = ""
    lines = text.splitlines()
    length = len(lines)
    
    for i, line in enumerate(lines):
        color = color_map_func(i, length)
        faded += rgb_to_ansi(*color, line) + RESET_CODE + "\n"
        
    return faded

# =======================================================
# HORIZONTAL GRADIENTS (character by character in a line)
# =======================================================

def blackwhite(text):
    """Apply a black to white gradient to the text."""
    def color_func(line):
        red = green = blue = 0
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(red, green, blue, char)
            if red < 255:
                red = green = blue = min(255, red + 20)
        return faded_line
    return apply_color(text, color_func)

def purplepink(text):
    """Apply a purple to pink gradient to the text."""
    def color_func(line):
        red = 40
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(red, 0, 220, char)
            if red < 255:
                red = min(255, red + 15)
        return faded_line
    return apply_color(text, color_func)

def greenblue(text):
    """Apply a green to blue gradient to the text."""
    def color_func(line):
        blue = 100
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(0, 255, blue, char)
            if blue < 255:
                blue = min(255, blue + 15)
        return faded_line
    return apply_color(text, color_func)

def pinkred(text):
    """Apply a pink to red gradient to the text."""
    def color_func(line):
        blue = 255
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(255, 0, blue, char)
            if blue > 0:
                blue = max(0, blue - 20)
        return faded_line
    return apply_color(text, color_func)

def purpleblue(text):
    """Apply a purple to blue gradient to the text."""
    def color_func(line):
        red = 110
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(red, 0, 255, char)
            if red > 0:
                red = max(0, red - 15)
        return faded_line
    return apply_color(text, color_func)

def water(text):
    """Apply a water-like gradient to the text."""
    def color_func(line):
        green = 10
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(0, green, 255, char)
            if green < 255:
                green = min(255, green + 15)
        return faded_line
    return apply_color(text, color_func)

def fire(text):
    """Apply a fire-like gradient to the text."""
    def color_func(line):
        green = 250
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(255, green, 0, char)
            if green > 0:
                green = max(0, green - 25)
        return faded_line
    return apply_color(text, color_func)

def brazil(text):
    """Apply a Brazil flag color gradient to the text."""
    def color_func(line):
        red = 0
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(red, 255, 0, char)
            if red < 200:
                red = min(200, red + 30)
        return faded_line
    return apply_color(text, color_func)

def random(text):
    """Apply a random color to each character in the text."""
    def color_func(line):
        faded_line = ""
        for char in line:
            faded_line += rgb_to_ansi(randint(0,255), randint(0,255), randint(0,255), char)
        return faded_line
    return apply_color(text, color_func)

# =======================================================
# LINEAR GRADIENTS (across the entire text)
# =======================================================

def linear_blackwhite(text):
    """Apply a linear black to white gradient across the entire text."""
    def color_map(i, length):
        gray = (255 * i) // length
        return (gray, gray, gray)
    
    return apply_linear_gradient(text, color_map) 

def linear_purplepink(text):
    """Apply a linear purple to pink gradient across the entire text."""
    def color_map(i, length):
        red = 40 + (215 * i // length)
        return (red, 0, 220)
    
    return apply_linear_gradient(text, color_map)

def linear_fire(text):
    """Apply a linear fire gradient across the entire text."""
    def color_map(i, length):
        green = 250 - (250 * i // length)
        return (255, green, 0)
    
    return apply_linear_gradient(text, color_map)
        
def linear_custom(starthex, endhex, text):
    """Apply a custom linear gradient to the text using provided hex colors."""
    start_rgb = hex_to_rgb(starthex)
    end_rgb = hex_to_rgb(endhex)
    
    def color_map(i, length):
        r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i // length
        g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i // length
        b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i // length
        return (r, g, b)
    
    return apply_linear_gradient(text, color_map)

# =======================================================
# VERTICAL GRADIENTS (line by line)
# =======================================================

def vertical_purplepink(text):
    """Apply a vertical purple to pink gradient to the text."""
    def color_map(i, length):
        red = 40 + (215 * i // length)
        return (red, 0, 220)
    
    return apply_vertical_gradient(text, color_map)

# New vertical gradient functions can be added here

# =======================================================
# RAINBOW EFFECTS
# =======================================================

def rainbow(text):
    """Apply a smooth rainbow gradient to the text."""
    def color_func(line):
        faded_line = ""
        length = len(line)
        if length == 0:
            return ""
            
        # Create a smooth rainbow transition
        # We'll use HSV color space and convert to RGB for smoother transitions
        import math
        
        def hsv_to_rgb(h, s, v):
            """Convert HSV color values to RGB."""
            h = float(h) / 360
            s = float(s) / 100
            v = float(v) / 100
            
            if s == 0.0:
                return (v, v, v)
                
            i = int(h * 6)
            f = (h * 6) - i
            p = v * (1 - s)
            q = v * (1 - s * f)
            t = v * (1 - s * (1 - f))
            
            i %= 6
            if i == 0:
                return (v, t, p)
            elif i == 1:
                return (q, v, p)
            elif i == 2:
                return (p, v, t)
            elif i == 3:
                return (p, q, v)
            elif i == 4:
                return (t, p, v)
            else:
                return (v, p, q)
        
        for i, char in enumerate(line):
            # Calculate hue value to create a smooth gradient across the line
            # Full rainbow is 360 degrees in HSV
            hue = int((i / length) * 360)
            
            # Get the RGB values from HSV
            r, g, b = hsv_to_rgb(hue, 100, 100)
            
            # Convert to 0-255 range
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            
            faded_line += rgb_to_ansi(r, g, b, char)
            
        return faded_line
    return apply_color(text, color_func)

# =======================================================
# ANIMATED EFFECTS
# =======================================================

def pulse(text, cycles=3, delay=0.1):
    """Create a pulsing animation effect with the given text."""
    for _ in range(cycles):
        for intensity in range(0, 100, 5):
            # Calculate RGB value
            r = int(255 * intensity / 100)
            g = int(100 * intensity / 100)
            b = int(255 * intensity / 100)
            
            # Clear and print
            print("\033[H\033[J", end="")  # Clear screen
            for line in text.splitlines():
                print(f"\033[38;2;{r};{g};{b}m{line}{RESET_CODE}")
            
            sleep(delay)
        
        for intensity in range(100, 0, -5):
            # Calculate RGB value
            r = int(255 * intensity / 100)
            g = int(100 * intensity / 100)
            b = int(255 * intensity / 100)
            
            # Clear and print
            print("\033[H\033[J", end="")  # Clear screen
            for line in text.splitlines():
                print(f"\033[38;2;{r};{g};{b}m{line}{RESET_CODE}")
            
            sleep(delay)

# Export public functions
__all__ = [
    # Horizontal gradients
    "blackwhite", "purplepink", "greenblue", "pinkred", "purpleblue", 
    "water", "fire", "brazil", "random",
    
    # Linear gradients
    "linear_blackwhite", "linear_purplepink", "linear_fire", "linear_custom",
    
    # Vertical gradients
    "vertical_purplepink",
    
    # Rainbow effects
    "rainbow",
    
    # Animated effects
    "pulse"
]