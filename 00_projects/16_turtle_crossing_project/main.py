import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars[:]:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if car.xcor() < -300:
            car.hideturtle()
            car_manager.cars.remove(car)

    if player.ycor() > 250:
        scoreboard.update_level()
        player.reset()
        car_manager.level_up()

        




screen.exitonclick()
