from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup() # TRACERS
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.refresh()
        self.pendown() # TRACERS


    def refresh(self):
        self.randx = random.randint(-300, 300)
        self.randy = random.randint(-300, 300)
        self.goto(self.randx, self.randy)