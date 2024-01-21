from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("aquamarine")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.respawn_food()

    def respawn_food(self):
        ran_x = random.randint(-290,290)
        ran_y = random.randint(-260,290)
        self.goto(ran_x,ran_y)