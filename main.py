from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(600, 400)
screen.tracer(0)
score = Score()
ball = Ball()
turtle = Turtle()
turtle.pen(pencolor="green")
turtle.pendown()
turtle.setposition(0,300)
turtle.setposition(0,-300)

l_paddle= Paddle((-280,0))
r_paddle= Paddle((280,0))

screen.listen()
screen.onkey(l_paddle.rightup_move, "Up")
screen.onkey(l_paddle.rightdown_move, "Down")
screen.onkey(r_paddle.leftup_move, "w")
screen.onkey(r_paddle.leftdown_move, "s")

game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.moving_ball()
    if ball.ycor() > 180 or ball.ycor() < -180:
        ball.change_direction()
    if ball.distance(r_paddle) < 20 and ball.xcor()>260 or ball.distance(l_paddle) < 20 and ball.xcor() < -260:
        ball.hit_bounce()
    if ball.xcor() == 280:
        score.right_player()
        ball.restart()

    elif ball.xcor() == -280:
        score.left_player()
        ball.restart()
    if score.second_score == 5 or score.score == 5:
        ball.game_over_msg()
        game_on: False



screen.exitonclick()