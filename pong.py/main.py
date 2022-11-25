import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard


# creating a screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


l_pad = Paddle((-350, 0))
r_pad = Paddle((350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(key="w", fun=l_pad.go_up)
screen.onkey(key="s", fun=l_pad.go_down)

screen.onkey(key="Up", fun=r_pad.go_up)
screen.onkey(key="Down", fun=r_pad.go_down)


game_on = True
round_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    score.create()
    ball.move()

    # detect collision with upper and lower frames
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # detect collision with pads
    if ball.distance(r_pad) < 50 and ball.xcor() > 330 or ball.distance(l_pad) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect collision with left and right frames
    if ball.xcor() > 500:
        score.left_scored()
        ball.reset_position()
        ball.bounce_x()

    if ball.xcor() < -500:
        score.right_scored()
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()
