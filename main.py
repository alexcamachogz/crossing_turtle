import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if randint(1, 4) == 1:
        cars_manager.create_car()

    cars_manager.move()

    for car in cars_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() == player.get_finish_line():
        player.go_home()
        score.increase_score()
        cars_manager.increase_speed()

screen.exitonclick()
