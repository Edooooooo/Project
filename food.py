from turtle import Turtle
from random import randint


class Food(Turtle):
    """ Creating Food for our Snake """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 circle
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)



