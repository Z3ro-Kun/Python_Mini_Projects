from turtle import Turtle

MOVE_FORWARD=20

class Snake:
    def __init__(self):
        self.snake_body = []
        self.make_snake()
        self.c=0


    def make_snake(self):

        for i in range(3):
            self.new_turtle=Turtle()
            self.new_turtle.shape("square")
            self.new_turtle.penup()
            self.new_turtle.color("white")
            self.snake_body.append(self.new_turtle)
        self.snake_body[1].teleport(self.snake_body[0].xcor()-20, 0)
        self.snake_body[2].teleport(self.snake_body[1].xcor()-20, 0)

    def grow_long(self):
        self.new_turtle = Turtle()
        self.new_turtle.shape("square")
        self.new_turtle.penup()
        self.new_turtle.color("white")
        self.new_turtle.hideturtle()
        self.snake_body.append(self.new_turtle)
        self.c=0

    def up(self):
        if self.snake_body[0].heading()==180.0:
          self.snake_body[0].right(90)
        if self.snake_body[0].heading()==0.0:
          self.snake_body[0].left(90)

    def down(self):
        if self.snake_body[0].heading()==180.0:
          self.snake_body[0].left(90)
        if self.snake_body[0].heading()==0.0:
          self.snake_body[0].right(90)

    def left(self):
        if self.snake_body[0].heading()==270.0:
          self.snake_body[0].right(90)
        else:
            self.snake_body[0].left(90)



    def right(self):
        if self.snake_body[0].heading() == 270.0:
            self.snake_body[0].left(90)
        else:
            self.snake_body[0].right(90)



    def move(self):

        if self.c==0:
            self.new_turtle.showturtle()
        for i in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[i].teleport(self.snake_body[i-1].xcor(), self.snake_body[i-1].ycor())
            self.snake_body[i-1].forward(MOVE_FORWARD)

        # snake_body[0].forward(20)
        # turn_left()

    def reset(self):
        self.c=1
        a= len(self.snake_body)
        for i in range(3, a):
            self.snake_body[len(self.snake_body)-1].hideturtle()
            self.snake_body[len(self.snake_body)-1].goto(1000, 1000)
            self.snake_body.pop(len(self.snake_body)-1)
        print(len(self.snake_body))

        self.snake_body[0].home()
        self.snake_body[1].teleport(self.snake_body[0].xcor() - 20, 0)
        self.snake_body[2].teleport(self.snake_body[1].xcor() - 20, 0)