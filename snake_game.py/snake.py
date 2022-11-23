from turtle import Turtle
COORDINATES = [[0, 0], [-20, 0], [-40, 0]]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.width = 20
        segment.height = 20
        segment.penup()
        segment.goto(position)
        self.whole_snake.append(segment)

    def extend(self):
        # add a new segment to snake
        self.add_segment(self.whole_snake[-1].position())

    def move(self):
        for segment in range(len(self.whole_snake)-1, 0, -1):
            new_x = self.whole_snake[segment - 1].xcor()
            new_y = self.whole_snake[segment - 1].ycor()
            self.whole_snake[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
