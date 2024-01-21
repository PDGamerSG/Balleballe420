from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake():
    
    def __init__(self):
        self.snake_segments = []
        self.create_initial_segements()
        self.head = self.snake_segments[0]

    def create_initial_segements(self):
        for position in POSITIONS:
            self.add_segements(position)

    def add_segements(self,pos):
        new_segement = Turtle()
        new_segement.penup()
        new_segement.color("powder blue")
        new_segement.shape("square")
        new_segement.goto(pos)
        self.snake_segments.append(new_segement)

    def move(self):

        for seg_num in range(len(self.snake_segments)-1,0,-1):
            new_position = self.snake_segments[seg_num-1].pos()
            self.snake_segments[seg_num].goto(new_position)
        self.head.forward(20)


    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000,1000)
        self.snake_segments.clear()
        self.create_initial_segements()
        self.head = self.snake_segments[0]

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def respawn_right(self):
        current_y = self.head.ycor()
        self.head.goto(x=300,y=current_y)
    def respawn_left(self):
        current_y = self.head.ycor()
        self.head.goto(x=-300,y=current_y)
    def respawn_down(self):
        current_x = self.head.xcor()
        self.head.goto(x=current_x,y=-260)