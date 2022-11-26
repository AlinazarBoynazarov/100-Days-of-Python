from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)
        self.create()

    def create(self):
        self.write(f"LEVEL: {self.score}", move=False, align='center',
                   font=('Arial', 16, 'normal'))

    def over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center',
                   font=('Arial', 16, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.create()
