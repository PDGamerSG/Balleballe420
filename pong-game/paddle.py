from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.goto(pos)
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 10
        if self.ycor() > 240:
            pass
        else: self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        if self.ycor() < -230:
            pass
        else: self.goto(self.xcor(),new_y)