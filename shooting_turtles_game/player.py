from turtle import Turtle

START_POS = (0, -270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("cyan")
        self.goto(START_POS)

    def left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


