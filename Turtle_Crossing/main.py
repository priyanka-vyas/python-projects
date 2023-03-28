from turtle import Turtle,Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen=Screen()
screen.setup(600,600)
screen.tracer(0)
scoreboard=Scoreboard()
player=Player()
car_manager=CarManager(0)
screen.listen()
screen.onkey(player.up, "Up")
is_game_on=True


while is_game_on:
    time.sleep(0.01)
    screen.update()
    car_manager.create_turtle()
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            is_game_on=False
    if player.reached_finish_line():
        scoreboard.increase()
screen.exitonclick()
