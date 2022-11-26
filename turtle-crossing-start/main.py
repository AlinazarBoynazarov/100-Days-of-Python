import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.move()

    # detecting collision with the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.over()
            game_is_on = False

    # detecting collision with the upper frame
    if player.ycor() > 280:
        scoreboard.update()
        player.reset_position()
        car_manager.faster()


screen.exitonclick()
