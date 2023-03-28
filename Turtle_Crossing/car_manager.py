COLORS = ["red", "yellow", "green", "blue", "purple", "orange", "pink"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self, level):
        self.level = level
        self.all_cars = []
        # new_carcreate_turtle()

    def create_turtle(self):
        random_chance=random.randint(1,100)
        if random_chance==1:
            rand_color = random.choice(COLORS)
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(rand_color)
            new_car.shapesize(1, 2)
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if self.level == 1:
                car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())
            else:
                car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())
