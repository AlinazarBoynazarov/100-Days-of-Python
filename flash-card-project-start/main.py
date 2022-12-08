from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
df = {}

try:
    data2 = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data1 = pandas.read_csv("data/spanish_words.csv")
    df = data1.to_dict(orient="records")
else:
    df = data2.to_dict(orient='records')


# ---------------------------- FUNCTIONALITY ------------------------------- #

def flip():
    canvas.itemconfig(image, image=new_image)

    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_card["english"])


def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df)
    canvas.itemconfig(image, image=old_image)
    spanish_word = current_card['spanish']

    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word, text=spanish_word, fill="black")

    window.after(5000, flip)


def known():
    df.remove(current_card)
    print(len(df))
    data = pandas.DataFrame(df)

    csv_data = data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

    # canvas.itemconfig(image, image=old_image)

    # canvas.itemconfig(language, text="Spanish", fill="black")
    # canvas.itemconfig(word, text=current_card["spanish"].values[0], fill="black")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Spanish")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(5000, flip)


# Card
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

old_image = PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 263, image=old_image)

new_image = PhotoImage(file="images/card_back.png")


# Text
language = canvas.create_text(400, 150, text="", font=(
    "Arial", 40, "italic"), fill="black")
canvas.grid(column=0, row=1, columnspan=2)


word = canvas.create_text(400, 263, text="", font=(
    "Arial", 40, "italic"), fill="black")
canvas.grid(column=0, row=1, columnspan=2)


# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0)
button_wrong.grid(column=0, row=2)

# Right Button
right_image = PhotoImage(file="images/right.png")
button_right = Button(
    image=right_image, command=known, highlightthickness=0)
button_right.grid(column=1, row=2)


next_card()


window.mainloop()
