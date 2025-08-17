import random
from turtle import Turtle



class Ball(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.screen=screen
        self.move_speed=0.1
        self.x=0
        self.y=0
        self.new_y= 10
        self.new_x= 10


    def move(self):

        self.x+=self.new_x
        self.y+=self.new_y
        self.goto(self.x, self.y)
        self.screen.update()


    def refresh(self):
        self.x=0
        self.y=0
        self.new_x*=-1
        self.move_speed=0.1
        self.home()


    def bounce(self):

        if self.ycor() >= 280:
            self.new_y*=-1

        if self.ycor() <= -280:
            self.new_y*=-1

    def collide_paddle(self):

        # self.new_y*=-1
        self.new_x*=-1
        self.move_speed*=0.9
