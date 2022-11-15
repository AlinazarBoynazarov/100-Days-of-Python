from turtle import Turtle, Screen
import random

race_on = True
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race (red, orange, yellow, green, blue, purple)? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ['tim', 'jony', 'mugambo', 'alex', 'tony', 'ali']
all_turtles = []
y_positions = [150, 100, 50, 0, -50, -100]


for i in range(0, 6):
    names[i] = Turtle(shape="turtle")
    names[i].color(colors[i])
    names[i].penup()
    names[i].goto(x=-230, y=y_positions[i])
    all_turtles.append(names[i])


if user_bet:
    race_on == True

while race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)

screen.exitonclick()
