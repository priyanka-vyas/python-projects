from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(self.pos)

    def up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.goto(x, new_y)
