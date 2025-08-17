from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 15, "bold")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.teleport(0, 270)
        self.score=0
        with open("data.txt") as highscore:
            self.highscore= int(highscore.read())
        self.hideturtle()
        self.score_display()


    def score_display(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", move=False, font=FONT, align=ALIGNMENT)
        self.score+=1


    def reset(self):

        if self.highscore < self.score:
            self.highscore=self.score
        with open("data.txt", mode="w") as highscore:
            highscore.write(f"{self.highscore}")
        self.score=0
        self.score_display()
        # self.home()
        # self.write("GAME OVER", font=("Comic Sans MS", 40, "bold"), align=ALIGNMENT)