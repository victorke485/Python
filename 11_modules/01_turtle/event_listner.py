from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.width(5)

def move_forward():
    my_turtle.forward(20)

def turn_left():
    my_turtle.left(30)

def turn_right():
    my_turtle.right(30)

def move_backwad():
    my_turtle.forward(-20)

def clear():
    my_turtle.penup()
    my_turtle.clear()
    my_turtle.home()
    my_turtle.pendown()
    




screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_backwad, "Down")
screen.onkey(clear, "c")
screen.exitonclick()