from turtle import Turtle, Screen, colormode
import random
# import colorgram

# # rgb_colors = []
# # colors = colorgram.extract("image.jpg", 30)
# # for color in colors:
# #     rgb_c = color.rgb # Rgb(r=168, g=99, b=102) 
# #     rgb_colors.append((rgb_c.r, rgb_c.g, rgb_c.b))

# # print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

my_turtle = Turtle()
colormode(255)

my_turtle.hideturtle()
my_turtle.penup()
my_turtle.speed("fastest")
y = -250
x = -250
for _ in range(10):
    my_turtle.goto(x, y)
    y += 50
    for _ in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)


screen = Screen()
screen.exitonclick()