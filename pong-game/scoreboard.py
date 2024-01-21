from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",60,"bold")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(x=-50,y=200)
        self.write(arg=self.l_score,align=ALIGNMENT,font=FONT)
        self.goto(x=50,y=200)
        self.write(arg=self.r_score,align=ALIGNMENT,font=FONT)


    def update_l_score(self):
        self.l_score +=1
        self.update_scoreboard()


    def update_r_score(self):
        self.r_score +=1
        self.update_scoreboard()
