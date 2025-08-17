from data import QuestionGenerator
from ui import QuizInterface
class QuizBrain:

    def __init__(self, question_number):
        self.question_number = question_number
        self.score = 0

        self.current_question = None

    def check_answer(self, user_answer, correct_answer):
        correct_answer = correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        self.question_number+=1
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question_right():
        question = QuestionGenerator()
        quiz_ui.canvas.itemconfig(quiz_ui.canvas_text, text=question.get_question())
        if question.get_answer() == "true":
            quiz_ui.score += 1

    def next_question_wrong():
        question = QuestionGenerator()
        quiz_ui.canvas.itemconfig(quiz_ui.canvas_text, text=question.get_question())
        if question.get_answer() == "false":
            quiz_ui.score += 1
