import turtle
from turtle import Turtle
import time

class Startname(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 0)
        self.pendown()
        self.write("Start...", align="center", font=("Courier", 14, "bold"))
        time.sleep(1.5)
        turtle.update()
        turtle.ontimer(lambda: self.clear(),  500)