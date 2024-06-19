from turtle import Turtle

class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.updatescore()



    def updatescore(self):
        self.write(f"Score {self.score}", align="center", font=("Courier", 18, "bold"))
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over...", align="center", font=("Courier", 18, "bold"))


    def increse_score(self):
        self.score+=1
        self.clear()
        self.updatescore()