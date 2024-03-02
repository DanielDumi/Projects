import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.start_distance = STARTING_MOVE_DISTANCE

    def move_left(self):
        for car in self.all_cars:
            car.forward(self.start_distance)

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(300, 320), random.randint(-200, 240))
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.start_distance += MOVE_INCREMENT







