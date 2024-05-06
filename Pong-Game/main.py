from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(height=600, width=800)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect ball collision with upper and down wall
    if ball.ycor() > 288 or ball.ycor() < -280:
        ball.bounce_y()

    # detection of ball with paddle
    if ball.xcor() > 330 or ball.xcor() < -330:
        if (ball.distance(r_paddle) < 50) or (ball.distance(l_paddle) < 50):
            ball.bounce_x()
        elif ball.xcor() > 400:  # if r_corner missed
            ball.reset_position()
            score.update_l_score()

            ball.bounce_x()
        elif ball.xcor() < -400:  # if l_corner missed
            ball.reset_position()
            score.update_r_score()
            ball.bounce_x()

screen.exitonclick()
