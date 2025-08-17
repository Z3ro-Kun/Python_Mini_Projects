from scoreboard import Scoreboard
from snaky_boi import Snake
from turtle import Screen
import time
from food import Food



screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orchid1")
screen.title("Snaky Boi")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

HEAD=snake.snake_body[0]


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on=True


while game_is_on:

    screen.update()
    time.sleep(0.2)
    snake.move()


    # Detect collision with food
    if HEAD.distance(food) < 15:
        scoreboard.score_display()
        food.refresh()
        snake.grow_long()



    #detect collision with wall
    if HEAD.xcor()>280.00 or HEAD.ycor()>280.00 or HEAD.xcor()<-280.00 or HEAD.ycor()<-280.00:
        # print("Game Over")
        scoreboard.reset()
        snake.reset()
        # game_is_on=False


    # detect collision with itself
    for segment in snake.snake_body[1:]:
        if HEAD.distance(segment)< 10:
            # game_is_on= False
            scoreboard.reset()
            snake.reset()
screen.exitonclick()