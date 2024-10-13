from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle('left')
r_paddle = Paddle('right')

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up,'Up')
screen.onkeypress(r_paddle.go_down,'Down')
screen.onkeypress(l_paddle.go_up,'w')
screen.onkeypress(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    ball.move()

    #se la pallina arriva nei bordi superiori
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.respawn()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.respawn()

    if(scoreboard.l_score > 9 or scoreboard.r_score > 9):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()


