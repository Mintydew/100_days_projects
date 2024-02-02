from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_right():
    turn_angle = 90/4
    timmy.right(turn_angle)


def move_left():
    turn_angle = 90/4
    timmy.left(turn_angle)


def reset():
    timmy.reset()


screen.listen()

screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="D", fun=move_right)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="C", fun=reset)

screen.onkey(key="W".lower(), fun=move_forward)
screen.onkey(key="S".lower(), fun=move_backwards)
screen.onkey(key="D".lower(), fun=move_right)
screen.onkey(key="A".lower(), fun=move_left)
screen.onkey(key="C".lower(), fun=reset)

screen.exitonclick()