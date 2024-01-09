from turtle import Turtle, Screen, forward

# Turtle is a module that provides a graphic interface using Python of a item such as a turtle to move.
timmy = Turtle()

my_screen = Screen()
timmy.shape("turtle")
timmy.color("CornflowerBlue")
timmy.forward(100)
print(timmy.position())

print(my_screen.canvheight)
my_screen.exitonclick()  # Allows our program to continue running until we click the screen
