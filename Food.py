from turtle import Turtle
import random
class Food():
    def __init__(self):
        self.food =Turtle("circle")
        self.food.color("yellow")
        self.food.penup()
        self.food.shapesize(0.5,0.5)
        self.refresh()

    def refresh(self):
        f_x= random.randint(-260,260)
        f_y = random.randint(-260, 260)
        self.food.goto(f_x,f_y)

