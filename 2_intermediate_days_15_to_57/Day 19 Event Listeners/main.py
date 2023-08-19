# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
# screen.listen()
# screen.onkey(key='space', fun=move_forwards)
# screen.exitonclick()
"""This effectively uses a function as an Input, this is known as Higher Order function.
It's better to use keyword arguments rather than positional arguments when using these.
"""
### Etch a Sketch ###
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.home()
#     tim.penup()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='d', fun=turn_right)
# screen.onkey(key='c', fun=clear)
# screen.exitonclick()

### Object State
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color =  turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've wone! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost :( The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()