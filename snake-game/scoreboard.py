from turtle import Turtle

FONT=("Courier",20,"bold")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open("high_score.txt") as file:
            hscore = file.read()
        self.highscore = int(hscore)
        self.score = 0
        self.goto(x=-295,y=-295)
        self.draw_line()
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.highscore}",align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score +=1
        self.write_score()

    def reset_score(self):
        if self.score > self.highscore:
            with open(file="high_score.txt",mode="w") as file:
                self.highscore = self.score
                file.write(str(self.score))
        self.score = 0
        self.write_score()


    def draw_line(self):
        line = Turtle()
        line.penup()
        line.hideturtle()
        line.goto(x=-300,y=-265)
        line.pensize(2)
        line.pencolor("white")
        line.pendown()
        line.goto(x=300,y=-265)
