from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level ={self.score} ", align="left", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER! ", align="center", font=("Arial", 20, "normal"))

    def increase(self):
        self.score += 1
        self.update_board()
