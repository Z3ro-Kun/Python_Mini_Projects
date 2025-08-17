import random
from turtle import Turtle
from colors import COLORS


class Car(Turtle):

    def __init__(self, ycord, spd):

        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.move_speed=spd
        self.color(random.choice(COLORS))
        self.seth(180)
        self.teleport(random.randint(250, 300), ycord)

    def move(self):

        self.forward(5)