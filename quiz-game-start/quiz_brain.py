class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}:{question.text}(True/False):")
        self.check_answer(ans, question.answer)

    def check_answer(self, user_ans, answer):
        if user_ans.lower() == answer.lower():
            self.score += 1
            print(self.score)
