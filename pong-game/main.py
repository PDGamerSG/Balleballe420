from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


r_paddle = Paddle(pos=(370,0))
l_paddle = Paddle(pos=(-370,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(key="Up",fun=r_paddle.go_up)
screen.onkeypress(key="Down",fun=r_paddle.go_down)
screen.onkeypress(key="w",fun=l_paddle.go_up)
screen.onkeypress(key="s",fun=l_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.interval)
    screen.update()
    ball.ball_movement()
    # Collision with walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    
    # Colision with paddle
    if ball.xcor() > 340 or ball.xcor() < -340:
        if ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50 :
            ball.paddle_bounce()
    
    # Missed Paddle

    if ball.xcor() > 390:
        time.sleep(0.5)
        ball.reset_ball()
        scoreboard.update_l_score()
    if ball.xcor() < -390:
        time.sleep(0.5)
        ball.reset_ball()
        scoreboard.update_r_score()












screen.exitonclick()