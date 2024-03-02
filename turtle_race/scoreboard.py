from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboards()

    def update_scoreboards(self):
        self.clear()
        self.goto(-200, 240)
        self.write(f"Level: {self.score}", align="Center", font=FONT)

    def increase_point(self):
        self.score += 1
        self.update_scoreboards()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)