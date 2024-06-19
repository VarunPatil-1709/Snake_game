
from turtle import Turtle
import time

class start(Turtle):
    def __init__(self):
        ascii_art = """
           _____                   _             
          / ____|                 | |            
         | (___    _ __     __ _  | | __   ___   
          \___ \  | '_ \   / _` | | |/ /  / _ \  
          ____) | | | | | | (_| | |   <  |  __/  
         |_____/  |_| |_|  \__,_| |_|\_\  \___|  


           _____                                 
          / ____|                                
         | |  __    __ _   _ __ ___     ___      
         | | |_ |  / _` | | '_ ` _ \   / _ \     
         | |__| | | (_| | | | | | | | |  __/     
          \_____|  \__,_| |_| |_| |_|  \___|     

        """
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-50, -150)
        self.write(ascii_art, align="center", font=("Courier", 14, "bold"))
        time.sleep(2)
        self.clear()
        self.box()


    def box(self):
        self.penup()
        self.color("white")
        self.goto(-275, -275)
        self.hideturtle()
        self.pensize(5)
        self.pendown()
        for i in range(0, 4):
            self.forward(550)
            self.left(90)
