import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a color:")

# def move_forward():
#     tim.forward(10)
colors = ["red", "yellow", "green", "pink", "blue", "purple"]
is_race_on = False
y = [-150, -100, -50, 0, 50, 100]
all_turtles = []
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-200, y[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            if turtle.pencolor()==user_bet:
                print(f"You won! The {turtle.pencolor()} won the race. ")
            else:
                print(f"You lose! The {turtle.pencolor()} won the race. ")
            is_race_on=False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
