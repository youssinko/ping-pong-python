from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xbounce= 10
        self.ybounce= 10
        self.moving_speed = 0.1


    def moving_ball(self):
        new_x = self.xcor() + self.xbounce
        new_y = self.ycor() + self.ybounce

        self.goto(new_x, new_y)
    def change_direction(self):
        self.ybounce *= -1

    def hit_bounce(self):
        self.xbounce *= -1
        self.moving_speed *= 0.5
    def restart(self):
        self.goto(0, 0)
        self.moving_speed = 0.1
        self.hit_bounce()

    def game_over_msg(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f" Game Over", align='center', font=('Arial', 30, 'normal'))