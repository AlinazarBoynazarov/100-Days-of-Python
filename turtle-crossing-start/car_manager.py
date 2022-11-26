import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
#  = 5
# MOVE_INCREMENT = 10
XCOR = 270


class CarManager():
    def __init__(self):
        self.start_move = 5
        self.all_cars = []

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            ycor = random.randint(-250, 250)
            new_car.goto(XCOR, ycor)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.start_move)

    def faster(self):
        self.start_move += 5
