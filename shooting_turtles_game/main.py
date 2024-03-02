import time
import random
from turtle import Screen
from player import Player
from enemy import Enemy
from projectile import Projectile
from scoreboard import Scoreboard
from healthbar import Healthbar

START_POS_PROJECTILE = (0, 0)

screen = Screen()
screen.title("Shooting turtles")
screen.setup(1200, 600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
enemy_1 = Enemy()
enemy_2 = Enemy()
enemy_3 = Enemy()
enemy_2.goto(200, 270)
enemy_3.goto(-200, 270)

scoreboard = Scoreboard()
healthbar = Healthbar()
projectiles = []
enemy_projectiles = []

screen.listen()
screen.onkeypress(player.left, "a")
screen.onkeypress(player.right, "d")
screen.onkey(lambda: shoot_projectile(player.xcor(), player.ycor()), "space")


def shoot_projectile(x_pos, y_pos):
    for projectile in projectiles:
        if projectile.state == "ready":
            projectile.goto(x_pos, y_pos)
            projectile.shoot()
            return

    new_projectile = Projectile(x_pos, y_pos)
    new_projectile.shoot()
    projectiles.append(new_projectile)


def enemy_shoot_projectile(x_pos, y_pos):
    for projectile in enemy_projectiles:
        if projectile.state == "ready":
            projectile.goto(x_pos, y_pos)
            projectile.enemy_shoot()
            return

    new_projectile = Projectile(x_pos, y_pos)
    new_projectile.enemy_shoot()
    enemy_projectiles.append(new_projectile)


def choose_enemy_to_shoot(random_number):
    if random_number == 1:
        enemy_shoot_projectile(enemy_1.xcor(), enemy_1.ycor())
    elif random_number == 2:
        enemy_shoot_projectile(enemy_2.xcor(), enemy_2.ycor())
    elif random_number == 3:
        enemy_shoot_projectile(enemy_3.xcor(), enemy_3.ycor())


game_is_on = True
while game_is_on:
    screen.update()
    enemy_1.movement()
    enemy_2.movement()
    enemy_3.movement()
    random_number = random.randint(1, 10)
    for projectile in projectiles:
        projectile.move()
        if projectile.distance(enemy_1) < 10:
            enemy_1.goto(-1000, -1000)
            scoreboard.update_scoreboard()
        elif projectile.distance(enemy_2) < 10:
            scoreboard.update_scoreboard()
            enemy_2.goto(-1000, -1000)
        elif projectile.distance(enemy_3) < 10:
            scoreboard.update_scoreboard()
            enemy_3.goto(-1000, -1000)
        if scoreboard.score == 30:
            scoreboard.you_won()
            game_is_on = False

    for projectile in enemy_projectiles:
        projectile.move()
        if projectile.distance(player) < 20:
            healthbar.update_health_bar()
            if healthbar.health == 0:
                healthbar.game_over()
                game_is_on = False
    choose_enemy_to_shoot(random_number)
    time.sleep(0.1)
screen.exitonclick()