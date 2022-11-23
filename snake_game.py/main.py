import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    scoreboard.create()
    snake.move()


# detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

        scoreboard.update()


# detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.over()
        game_on = False

# detect collision with tail

    for segment in snake.whole_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.over()


screen.exitonclick()
