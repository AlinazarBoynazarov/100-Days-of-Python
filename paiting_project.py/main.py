import turtle as t
import random
import colorgram as cg


t.colormode(255)
tim = t.Turtle()


color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186,
                                                                                                                                                                                                                                                                             94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]

tim.penup()
tim.setheading(135)
tim.forward(250)
tim.setheading(0)


tim.hideturtle()
tim.pensize(20)
tim.speed(0)


for i in range(10):
    for j in range(10):
        # dot
        tim.dot(20, random.choice(color_list))
        # distance for another dot
        tim.forward(50)
    tim.backward(50*10)

    # direction
    tim.right(90)
    tim.forward(50)
    tim.left(90)


screen = t.Screen()

screen.exitonclick()
