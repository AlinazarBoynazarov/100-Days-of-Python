import pandas
import turtle
from turtle import Turtle


image = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
screen.addshape(image)

turtle.shape(image)

guessed = []

data = pandas.read_csv("50_states.csv")

score = len(guessed) / len(data["state"])

while len(guessed) < 50:

    all_states = data["state"].tolist()

    answer_state = screen.textinput(
        title=f"{score}/{len(all_states)} Correct", prompt="What is another state's name?").title()

    if answer_state in all_states:
        score += 1
        # name of states on screen
        guessed.append(answer_state)
        row = data[data["state"] == answer_state]
        text = Turtle()
        text.color("black")
        text.penup()
        text.hideturtle()
        text.goto(int(row.x), int(row.y))
        text.write(f"{answer_state}", move=True, align='center',
                   font=('Arial', 16, 'normal'))

    elif answer_state == "Exit":
        to_learn = []
        for state in all_states:
            if state not in guessed:
                to_learn.append(state)

        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("to_lear.csv")

        break

print(f"You have {to_learn} to learn")
