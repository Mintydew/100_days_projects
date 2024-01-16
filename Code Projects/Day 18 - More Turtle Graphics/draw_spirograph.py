import turtle as t
from random import randint

screen = t.Screen()
drawer = t.Turtle()
drawer.speed(0) # Fastest speed
t.colormode(255)
drawer.hideturtle()


def randomize_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return r, g, b


def circle_drawing(limit):
    for _ in range(0, limit):
        turn_degree = 360 / limit
        current_heading = drawer.heading()

        drawer.circle(150)
        drawer.pencolor(randomize_color())
        drawer.setheading(current_heading + turn_degree)


circle_drawing(100)
screen.exitonclick()

