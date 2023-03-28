from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score=Scoreboard()
r_paddle = Paddle((350, 0))

l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(ball.move, "p")

is_game_on = True
while is_game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # wall
    if ball.ycor() == -280 or ball.ycor() == 280:
        ball.bounce()

    # paddle
    if ball.distance(r_paddle) < 20 :
        score.r_score += 1
        print(score.r_score)
        ball.refresh()

    if ball.distance(l_paddle) < 20 :
        score.l_score += 1
        print(score.l_score)
        ball.refresh()




    #out of bound
    if ball.xcor()>380:
        ball.goto(0,0)
        score.l_increase()
        print(score.l_score)
        ball.refresh()

    if ball.xcor()==-380:
        ball.goto(0,0)
        score.r_increase()
        print(score.r_score)
        ball.refresh()


screen.exitonclick()
