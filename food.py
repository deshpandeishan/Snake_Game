from turtle import Turtle
from random import randint

grain = Turtle()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('green')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        self.goto(randint(-250, 250), randint(-250, 250))
