from turtle import Turtle, Screen
import random

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("red")

def draw_square(length):
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)

def draw_dashed_line(length):
    while length > 0:
        my_turtle.pendown()
        my_turtle.forward(5)
        my_turtle.penup()
        my_turtle.forward(5)        
        length -= 10

def draw_pentagon(sides):
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.left(360 / sides)
    change_color()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    my_turtle.color(R, G, B)

def change_width(width):
    my_turtle.width(width)

def change_speed(speed):
    my_turtle.speed(speed)


# for i in range(3, 10):
#     draw_pentagon(i)
def draw_random_walk(steps):
    change_speed("fastest")
    change_width(20)
    for i in range(steps):
        change_color()
        my_turtle.forward(50)
        my_turtle.setheading(random.choice([0, 90, 180, 270]))
      

def draw_spirograph(size_of_gap):
    change_speed("fastest")
    change_width(2)
    
    for _ in range(int(360 / size_of_gap)):
        change_color()
        my_turtle.pendown()
        my_turtle.circle(100)
        my_turtle.setheading( my_turtle.heading() + size_of_gap )

draw_spirograph(8)


screen = Screen()
screen.exitonclick()