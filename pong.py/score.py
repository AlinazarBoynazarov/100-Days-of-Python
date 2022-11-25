from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)

    def create(self):
        self.write(f"Left_player: {self.left_score}     Right_player: {self.right_score}", move=False, align='center',
                   font=('Arial', 16, 'normal'))

    def left_scored(self):
        self.clear()
        self.left_score += 1
        self.create()

    def right_scored(self):
        self.clear()
        self.right_score += 1
        self.create()
