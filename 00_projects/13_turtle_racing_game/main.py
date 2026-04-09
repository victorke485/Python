from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)

colors = ["red", "green", "blue", "orange", "purple", "yellow"]

input_prompt = f"Which turtle will win the race? Enter a color {colors}: "
user_bet = screen.textinput(title = "Make your bet", prompt=input_prompt)
while user_bet not in colors:
    user_bet = screen.textinput(title = "Make your bet", prompt=f"Please choose a valid option. {input_prompt}")

all_turtles = []

y_step = 360 / len(colors)
y_position = -160

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_position)
    y_position += y_step
    all_turtles.append(new_turtle)



is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        else:
            turtle.forward(randint(0, 10))
    




screen.exitonclick()