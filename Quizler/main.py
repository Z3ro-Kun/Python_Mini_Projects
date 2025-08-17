from question_model import Question
from data import QuestionGenerator
from quiz_brain import QuizBrain
from ui import QuizInterface
import html


# new_question = Question(question_text, question_answer)
# question_bank.append(new_question)
# n = int(input("Enter number of questions: "))
quiz_ui = QuizInterface()



# question_number = 0
# quiz = QuizBrain(question_number)
# question_number = 1
# for i in range(1, n+1):
#     question_bank = QuestionGenerator()
#     question_text = question_bank.get_question()
#     question_answer = question_bank.get_answer()
#     user_answer = input(f"Q{question_number}: {question_text} (True/False): ")
#     quiz.check_answer(user_answer=user_answer, correct_answer=question_answer)
#     question_number+=1
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{question_number}")
