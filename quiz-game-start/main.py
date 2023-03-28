from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import data

question_bank = []

for i in data.question_data:
    que = Question(i["text"], i["answer"])
    question_bank.append(que)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
