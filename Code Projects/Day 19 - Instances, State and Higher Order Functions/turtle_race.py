from turtle import Turtle, Screen
import random

is_race_on = False
is_prompt_ok = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
turtle_locations = [(-230, -100), (-230, -50), (-230, 0), (-230, 50), (-230, 100), (-230, 150)]
rolled_numbers = []
turtle_dict = {}

while not is_prompt_ok:
    user_bet = screen.textinput(title="Make your bet",
                                prompt=f"Which turtle will win the race? Enter a color: {colors}")
    user_bet = user_bet.lower()

    if user_bet not in colors:
        is_prompt_ok = False
    else:
        is_prompt_ok = True

for i in range(0, 6):
    random_number = random.choice([i for i in range(0, 6) if i not in rolled_numbers])
    rolled_numbers.append(random_number)

    turtle_name = f"turtle_{i}"

    turtle_dict[turtle_name] = Turtle(shape="turtle")
    turtle_dict[turtle_name].penup()
    turtle_dict[turtle_name].color(colors[random_number])

for turtle in turtle_dict:
    x, y = turtle_locations.pop()
    turtle_dict[turtle].goto(x, y)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_dict:
        if turtle_dict[turtle].xcor() > 230:
            is_race_on = False

            print(turtle_dict[turtle].pencolor())
            winning_turtle = turtle_dict[turtle].pencolor()
            turtle_dict[turtle].right(720)  # Make the winning turtle do a cute little spin
            if winning_turtle == user_bet:
                print(f"You've won. The winner is {winning_turtle}")
            else:
                print(f"You've lost.... The winner is {winning_turtle}")

        rand_distance = random.randint(0, 10)
        turtle_dict[turtle].forward(rand_distance)


screen.exitonclick()