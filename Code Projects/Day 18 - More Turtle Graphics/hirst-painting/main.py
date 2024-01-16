import turtle

from color import colors_list
from turtle import Turtle, Screen
import random

# TODO: Create Hirst dot painting - 20 dot size with 50 gap. 10 x 10 board.
hirst = Turtle()
screen = Screen()
turtle.colormode(255)

hirst.speed(0)

screen.setup(1000, 1000)

# start_width = screen.window_width() / 9
# start_height = screen.window_height() / 6
#
hirst.penup()
hirst.goto(-215, -150)


def allocate_dots():
    for _ in range(0, 10):
        prior_start = hirst.pos()

        for _ in range(0, 10):
            hirst.pencolor(random.choice(colors_list))

            hirst.dot(20)
            hirst.penup()
            hirst.fd(50)
            hirst.pendown()

        hirst.penup()
        hirst.goto(prior_start)
        hirst.setheading(90)
        hirst.fd(50)
        hirst.setheading(0)
        hirst.pendown()


allocate_dots()
hirst.hideturtle()
screen.exitonclick()