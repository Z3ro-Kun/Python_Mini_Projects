from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self, xcord):

        super().__init__()
        self.penup()
        self.teleport(xcord, 200)
        self.score = 0
        self.color("Black")
        self.hideturtle()
        self.score_display()

    def score_display(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, font=FONT, align=ALIGNMENT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", font=("Comic Sans MS", 40, "bold"), align=ALIGNMENT)