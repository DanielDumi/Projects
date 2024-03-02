from turtle import Turtle
import random
START_POS = (0, 270)
RANDOM_X_INCREMENT = [-20, +20]


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.setheading(270)
        self.color("green")
        self.goto(START_POS)

    def movement(self):
        new_x = self.xcor() + random.choice(RANDOM_X_INCREMENT)
        self.goto(new_x, self.ycor())
        if new_x > 500:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
        elif new_x < -500:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())



