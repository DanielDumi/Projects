from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("cyan")
        self.penup()
        self.goto(500, -270)
        self.hideturtle()
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 10
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def you_won(self):
        self.goto(0, 0)
        self.write("YOU WON!", align="Center", font=FONT)

