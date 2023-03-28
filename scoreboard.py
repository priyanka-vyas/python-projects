from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score=0
        self.color("white")
        self.penup()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-40,260)
        self.write(f"{self.l_score}",align="center",font=("Arial", 20, "normal"))
        self.goto(40,260)
        self.write(f"{self.r_score}",align="center",font=("Arial", 20, "normal"))
        self.hideturtle()
    def r_increase(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_increase(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()