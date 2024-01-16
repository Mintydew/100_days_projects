from turtle import Turtle, Screen
import random
from colors import random_color

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("white")

# TODO: 1, Draw a square
# square = Turtle()
# square.shape("arrow")
#
# i = 0
# while i < 4:
#     if i != 3:
#         square.forward(100)
#         square.right(90)
#     else:
#         square.forward(100)
#
#     i += 1

# TODO: 2. Draw a Dashed Line (10px line then 10px gap 10 times.)
# paced_line = Turtle()
# paced_line.shape("arrow")
# paced_line.speed(2)
#
# for _ in range(15):
#     paced_line.forward(10)
#     paced_line.penup()
#     paced_line.forward(10)
#     paced_line.pendown()

# TODO: 3. Draw different shapes - Creation of shapes that have one more side than the previous shape until loop end
# TODO: Provide colors as well
# various_shapes = Turtle()
# various_shapes.speed(50)  # Faster speed as it takes a while for the turtle to finish
#
# various_shapes.penup()
# various_shapes.setpos(0, screen.window_height()/2) # Set position to top of screen
# various_shapes.pendown()
#
# for i in range(3, 50):
#     various_shapes.color(random.choice(colors_list))
#     for _ in range(i):
#         various_shapes.right(360/i)
#         various_shapes.forward(100)

# TODO: 4. Draw a random walk
walk = Turtle()
walk.pensize(20)
walk.speed(10)
directions = [0, 90, 180, 270]
# Reduce screen size a little bit to prevent turtle going beyond screen size visually
screen_width = screen.window_width() - 200
screen_height = screen.window_height() - 200
print(f"height: {screen_height} width: {screen_width}")


def random_path(cycles):
    for _ in range(cycles):
        random_rotation = 90 * (random.randint(1, 4))
        random_forward = random.randint(0, 100)

        walk.pencolor(random_color())
        walk.right(random_rotation)

        keep_on_screen(random_forward)


def keep_on_screen(movement_query):
    print(f"movement query: {movement_query}")
    if check_horizontal(movement_query) and check_vertical(movement_query):
        walk.forward(movement_query)

    if not check_horizontal(movement_query):
        if walk.heading() == 0:
            walk.setheading(180)
            print(walk.heading())
            walk.forward(movement_query)
        elif walk.heading() == 180:
            walk.setheading(0)
            print(walk.heading())
            walk.forward(movement_query)

    if not check_vertical(movement_query):
        if walk.heading() == 90:
            walk.setheading(270)
            print(walk.heading())
            walk.forward(movement_query)
        elif walk.heading() == 270:
            walk.setheading(90)
            print(walk.heading())
            walk.forward(movement_query)

    if not check_vertical(movement_query) and not check_horizontal(movement_query):
        walk.penup()
        walk.setpos(0, 0)
        walk.pendown()


def check_horizontal(movement_query):
    x, y = walk.position()
    if movement_query + abs(x) > screen_width / 2:
        print(f"x: {x} movement width +: {movement_query + x} movement width -: {movement_query - x}")
        return False
    return True


def check_vertical(movement_query):
    x, y = walk.position()
    if movement_query + abs(y) > screen_height / 2:
        print(f"y: {y} movement height +: {movement_query + y} movement height -: {movement_query - y}")
        return False
    return True


random_path(100)
screen.exitonclick()
