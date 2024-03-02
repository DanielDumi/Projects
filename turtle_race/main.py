import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# from tkinter import *

screen = Screen()
screen.bgcolor("cyan")
screen.title("Turtle Race!")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_left()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_point()
        car_manager.increase_speed()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()