from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

label_1 = Label(text="is equal to", font=("Arial", 24, "bold"))
label_1.grid(column=0, row=1)

# Label 2
label_2 = Label(text="Miles", font=("Arial", 24, "bold"))
label_2.grid(column=2, row=0)


# Label 3
label_3 = Label(text="0", font=("Arial", 24, "bold"))
label_3.grid(column=1, row=1)


# Label 4
label_4 = Label(text="Km", font=("Arial", 24, "bold"))
label_4.grid(column=2, row=1)


def button_clicked():
    label_3.config(text=float(input.get())*1.609344)


button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)


# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)


input = Entry(width=7)
input.grid(column=1, row=0)

label = Label(text="Miles", font=("Arial", 24, "bold"))


window.mainloop()
