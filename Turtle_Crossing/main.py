import random
from turtle import Turtle, Screen
from car import Car
import time
MOVE_SPEED=0.1
from scoreboard import ScoreBoard

N=6


screen=Screen()
screen.setup(width=600, height=500)
screen.bgcolor("white")
screen.title("Turtle Crossing")


score=ScoreBoard(-230)


car=[]


def make_cars():
    for i in range(10):
        car.append(Car(random.randint(-180, 170), MOVE_SPEED))


# Finish Line

finish_line=Turtle()
finish_line.hideturtle()
finish_line.teleport(-180, 180)
finish_line.forward(360)


screen.tracer(0)
turtle_1=Turtle()
turtle_1.penup()
turtle_1.shape("turtle")
turtle_1.seth(90)
turtle_1.teleport(0, -230)
screen.update()


def move_turtle():
    turtle_1.forward(20)


screen.listen()
screen.onkey(move_turtle, "Up")



game_is_on = True

c=1

make_cars()

while game_is_on:



    if c%20==0:
        make_cars()
        N+=6


    for i in range(N):
       car[i].move()


    if turtle_1.ycor()>= 175:
        turtle_1.teleport(0, -230)
        score.score_display()
        MOVE_SPEED*=0.9

    for i in car:
        if turtle_1.distance(i)<=15:
            score.game_over()
            game_is_on = False
    c+=1
    screen.update()
    time.sleep(MOVE_SPEED)

screen.exitonclick()