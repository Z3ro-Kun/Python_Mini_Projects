from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
import random

from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Pong")


game_is_on=True


screen.tracer(0)
paddle1=Paddle(350, screen)
paddle2=Paddle(-350, screen)
screen.update()
# screen.tracer(1)


screen.listen()
screen.onkeypress(paddle2.move_forward, "Up")
screen.onkeypress(paddle2.move_backward, "Down")

screen.onkeypress(paddle1.move_forward, "w")
screen.onkeypress(paddle1.move_backward, "s")


score1 = ScoreBoard(100)
score2 = ScoreBoard(-100)


# center dotted line
dot_line=Turtle()
dot_line.hideturtle()
dot_line.color("white")
dot_line.teleport(0, 290)
dot_line.seth(270)
dot_line.width(10)
for i in range(10):
   dot_line.pendown()
   dot_line.forward(30)
   dot_line.penup()
   dot_line.forward(30)
   screen.update()


ball1=Ball(screen)


while game_is_on:

   ball1.bounce()



   if ball1.xcor()>380:
       score2.score_display()
       ball1.refresh()

   if ball1.xcor()<-380:
       score1.score_display()
       ball1.refresh()

   if (ball1.distance(paddle1.paddle1)<=50 and ball1.xcor() >= 320) or (ball1.distance(paddle2.paddle1)<=50 and ball1.xcor() <= -320):
         ball1.collide_paddle()

   if score1.score == 10 or score2.score == 10:
       score1.game_over()

   ball1.move()
   time.sleep(ball1.move_speed)












screen.update()

screen.exitonclick()