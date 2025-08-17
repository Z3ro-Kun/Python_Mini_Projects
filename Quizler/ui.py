THEME_COLOR = "#375362"
from tkinter import *
import time
from data import QuestionGenerator
class QuizInterface:

    def next_question_right(self):

        if self.question.get_answer() == "True":
            self.canvas.config(bg="green")
            time.sleep(1)
            self.canvas.config(bg="white")
            self.score += 1
        else:
            self.canvas.config(bg="red")
            time.sleep(1)
            self.canvas.config(bg="white")
        self.score_label.config(text=f"Score {self.score}")
        self.question = QuestionGenerator()
        self.canvas.itemconfig(self.canvas_text, text=self.question.get_question())

    def next_question_wrong(self):
        if self.question.get_answer() == "False":
            self.canvas.config(bg="green")
            time.sleep(1)
            self.canvas.config(bg="white")
            self.score += 1
        else:
            self.canvas.config(bg="red")
            time.sleep(1)
            self.canvas.config(bg="white")
        self.score_label.config(text=f"Score {self.score}")
        self.question = QuestionGenerator()
        self.canvas.itemconfig(self.canvas_text, text=self.question.get_question())


    def __init__(self):
        self.question = QuestionGenerator()
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.outer_canvas = Canvas(height=300, width=300, bg=THEME_COLOR, highlightthickness=0)
        self.canvas = Canvas(self.outer_canvas, height=250, width=300, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text=self.question.get_question(), width=280, font=("Arial", 20, "italic"))
        self.outer_canvas.create_window(150, 150, window=self.canvas)
        self.outer_canvas.grid(row=1, column=0, columnspan=2)

        self.tick = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick, command=self.next_question_right)
        self.tick_button.grid(row=2, column=0)

        self.cross = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross, command=self.next_question_wrong)
        self.cross_button.grid(row=2, column=1)


        self.window.mainloop()

