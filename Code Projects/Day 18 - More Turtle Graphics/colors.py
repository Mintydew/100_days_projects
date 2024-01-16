import turtle as t
import random

# TODO 1: Adjust color mode
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple

