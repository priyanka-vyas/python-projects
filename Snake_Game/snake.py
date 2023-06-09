MOVE_POSITION = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_POSITION)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(0)

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
