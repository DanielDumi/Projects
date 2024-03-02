from turtle import Turtle

MOVING_DISTANCE = 20


class Projectile(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed(1)
        self.goto(x, y)
        self.state = "ready"

    def move(self):
        if self.state == "fire":
            self.shape("triangle")
            self.color("red")
            self.setheading(90)
            new_y = self.ycor() + MOVING_DISTANCE
            self.goto(self.xcor(), new_y)
        elif self.state == "enemy":
            self.shape("triangle")
            self.color("green")
            self.setheading(270)
            self.showturtle()
            new_y = self.ycor() - MOVING_DISTANCE
            self.goto(self.xcor(), new_y)

    def shoot(self):
        self.state = "fire"

    def enemy_shoot(self):
        self.state = "enemy"