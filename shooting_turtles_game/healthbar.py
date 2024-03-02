from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Healthbar(Turtle):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.color("red")
        self.penup()
        self.goto(500, 270)
        self.hideturtle()
        self.show_health_bar()

    def show_health_bar(self):
        self.clear()
        self.write(f"Health: {self.health}%", align=ALIGNMENT, font=FONT)

    def update_health_bar(self):
        self.clear()
        self.health -= 10
        self.write(f"Health: {self.health}%", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)