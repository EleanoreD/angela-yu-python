# import colorgram
# rgb_colors = []
# colors = colorgram.extract('pic.jpg', 25)
# for color in colors:
#     #rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


import turtle as t
import random
t.colormode(255)
color_list = [(113, 105, 67), (184, 160, 127), (77, 113, 77), (33, 126, 164), (55, 52, 35), (228, 219, 202), (156, 137, 72), (76, 73, 38), (219, 195, 151), (149, 159, 152), (234, 224, 228), (218, 226, 220), (217, 223, 229), (149, 160, 168), (47, 57, 44), (169, 156, 161), (165, 112, 98), (57, 70, 53), (115, 136, 112), (117, 102, 106), (212, 183, 176), (45, 57, 63), (205, 183, 189), (180, 198, 191), (151, 113, 118)]

t.pensize(20)
t.speed("fastest")

for _ in range(5):
    for _ in range(10):
        t.color(random.choice(color_list))
        t.forward(0)
        t.penup()
        t.forward(50)
        t.pendown()

    t.left(90)
    t.penup()
    t.forward(50)
    t.left(90)
    t.pendown()

    for _ in range(10):
        t.color(random.choice(color_list))
        t.forward(0)
        t.penup()
        t.forward(50)
        t.pendown()

    t.color(random.choice(color_list))
    t.forward(0)
    t.right(90)
    t.penup()
    t.forward(50)
    t.pendown()
    t.right(90)




t.exitonclick()
