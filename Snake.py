from turtle import Turtle
Position = [(0, 0), (-20, 0), [-40, 0]]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]

    def create_snake(self):
        for seg in Position:
            self.add_seg(seg)

    def add_seg(self, seg):
        new_index: Turtle = Turtle("square")
        new_index.penup()
        new_index.color("white")
        new_index.goto(seg)
        self.segements.append(new_index)

    def exted_snake(self):
        self.add_seg(self.segements[-1].position())


    def move(self):
        for seg in range(len(self.segements) - 1, 0, -1):
            new_x = self.segements[seg - 1].xcor()
            new_y =self. segements[seg - 1].ycor()
            self.segements[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)