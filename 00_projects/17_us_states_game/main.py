from turtle import Turtle, Screen
from pathlib import Path
import pandas as pd
import time

image = str(Path("00_projects/17_us_states_game/blank_states_img.gif"))
states_csv = Path("00_projects/17_us_states_game/50_states.csv")

data = pd.read_csv(states_csv)
state_list = data.state.to_list()
x_list = data.x.to_list()
y_list = data.y.to_list()

screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)


turtle = Turtle()
turtle.shape(image)
turtle.penup()

new_turtle = Turtle()
new_turtle.penup()
new_turtle.color("black")
new_turtle.hideturtle()

game_on = True
answered_states = []
while game_on:
    answer_state = screen.textinput(title=f"{len(answered_states)}/ {len(state_list)} States Correct. Guess the State", prompt="What's another state's name?").title()
    if answer_state in state_list and answer_state not in answered_states:
        answered_states.append(answer_state)
        index = state_list.index(answer_state)
        x = x_list[index]
        y = y_list[index]
        new_turtle.goto(x, y)
        new_turtle.write(answer_state)
    if len(answered_states) == len(state_list) or answer_state == "Exit":
        game_on = False


for state in answered_states:
    state_list.remove(state)

state_to_learn_list = []

for state in state_list:
    x = x_list[state_list.index(state)]
    y = y_list[state_list.index(state)]
    state_to_learn_list.append(
        {"state": state,
         "x": x,
         "y": y}
    )

df = pd.DataFrame(state_to_learn_list)
df.to_csv("00_projects/17_us_states_game/states_to_learn.csv")
