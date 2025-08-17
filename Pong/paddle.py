from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, xcord, screen):
        super().__init__()
        self.paddle1=Turtle()
        self.xcord=xcord
        self.screen=screen
        self.screen.tracer(0)
        self.paddle1.penup()
        self.paddle1.shape("square")
        self.paddle1.speed(7)
        self.paddle1.color("white")
        self.paddle1.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle1.seth(90)
        self.paddle1.teleport(self.xcord, 0)
        self.screen.update()




    def move_forward(self):

        self.paddle1.goto(self.xcord, self.paddle1.ycor() + 20)
        self.screen.update()


    def move_backward(self):

        self.paddle1.goto(self.xcord, self.paddle1.ycor() - 20)
        self.screen.update()