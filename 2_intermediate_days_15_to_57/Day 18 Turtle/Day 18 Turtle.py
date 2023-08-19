from turtle import Turtle, Screen

tim = Turtle()
# tom = Turtle()
# terry = Terry()

tim.shape('turtle')
tim.color('#ADFF2F')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for  _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# can import everything by using an asterisk eg from turtle import *, not particularly good practice
# how to alias modules import turtle as t
# tim = t.Turtle()
# some modules need installing
# import heroes
# print(heroes.gen())

# for _ in range (10):
#     tim.speed(1)
#     tim.pd()
#     tim.forward(20)
#     tim.pu()
#     tim.forward(10)

# for _ in range(4):
#     tim.forward(20)
#     tim.right(90)
# for _ in range(5):
#     tim.forward(20)
#     tim.right(72)
# for _ in range(6):
#     tim.forward(20)
#     tim.right(60)
# for _ in range(7):
#     tim.forward(20)
#     tim.right(51.8)
# for _ in range(8):
#     tim.forward(20)
#     tim.right(45)

import turtle as t
# import random
#
# tim = t.Turtle()
#
# ########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

#
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
# ########### Challenge 5 - Random Walk Random Color ########
#
# def random_color():
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#         random_color = (r,g,b)
#         return random_color
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
#
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
# ########### Challenge 6 - Random Circle ########
#
# def random_color():
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#         random_color = (r,g,b)
#         return random_color
#
#
# tim.pensize(2)
# tim.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + 10)
#
# draw_spirograph(5)

"""Final Challenge - DIY Damian Hurst"""

screen = Screen()
screen.exitonclick()