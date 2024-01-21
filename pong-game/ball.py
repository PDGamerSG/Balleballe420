from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.home()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.xcore = 10
        self.ycore = 10
        self.interval = 0.1
    
    def ball_movement(self):
        new_x = self.xcor() + self.xcore
        new_y = self.ycor() + self.ycore
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.ycore *= -1
    
    def paddle_bounce(self):
        self.xcore *= -1
        self.interval *=0.9
    
    def reset_ball(self):
        self.interval = 0.1
        self.paddle_bounce()
        self.home()