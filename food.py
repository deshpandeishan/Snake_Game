from turtle import Turtle
from random import randint

grain = Turtle()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        grain.shape("circle")
        grain.penup()
        grain.color('green')
        grain.shapesize(stretch_len=0.5, stretch_wid=0.5)
        grain.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        self.goto(randint(-300, 300), randint(-300, 300))
