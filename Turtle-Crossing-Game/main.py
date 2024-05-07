import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

timmy = Player()
car_manager = CarManager()
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()

    # generate random cars  and make them move
    car_manager.generate_car()
    car_manager.motion()

    # detect collision with cars
    for car in car_manager.cars:
        if car.distance(timmy) < 20:
            score.game_over()
            game_is_on = False

    # check if turtle crossed the finish line
    if timmy.ycor() > 280:
        score.update_score()
        timmy.starting_position()
        car_manager.increase_speed()

    screen.onkey(fun=timmy.move, key='Up')

screen.exitonclick()
