STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200
from turtle import Turtle
from scoreboard import Scoreboard


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        self.score = Scoreboard()

    def reached_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            self.create_turtle()
            self.score.increase()
            return True
        else:
            return False

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        if self.ycor() == FINISH_LINE_Y:
            self.reached_finish_line()
