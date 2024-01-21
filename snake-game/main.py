from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("dim gray")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
scoreboard = Scoreboard()
print(snake.snake_segments)

screen.onkeypress(fun=snake.move_up,key="Up")
screen.onkeypress(fun=snake.move_down,key="Down")
screen.onkeypress(fun=snake.move_left,key="Left")
screen.onkeypress(fun=snake.move_right,key="Right")


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.09)

    snake.move()

    # Detect collision with food.

    if snake.head.distance(food) < 15:
        food.respawn_food()
        scoreboard.update_score()
        snake.add_segements(snake.snake_segments[len(snake.snake_segments)-1].pos())

    # Detect collision with wall

    if snake.head.ycor() < -260:
        scoreboard.reset_score()
        snake.reset_snake()
        time.sleep(1)

    # Repalce snake if it pass wall
    if snake.head.ycor() > 300:
        snake.respawn_down()
    elif snake.head.xcor() > 300:
        snake.respawn_left()
    elif snake.head.xcor() < -300:
        snake.respawn_right()

    # Detect Tail Collision
    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments)<15:
            scoreboard.reset_score()
            snake.reset_snake()
            time.sleep(1)
        





screen.exitonclick()