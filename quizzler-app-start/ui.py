THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # start_label
        self.start_label = Label(text="Score:", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.start_label.grid(column=1, row=0)

        # question canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="queston", width=200, fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_img, command=self.true_pressed, highlightthickness=0)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = Button(image=wrong_img, command=self.false_pressed, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.start_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="ENd of QUiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

