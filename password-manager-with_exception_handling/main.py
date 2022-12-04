from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters))
     for char in range(random.randint(8, 10))]
    [password_list.append(random.choice(numbers))
     for char in range(random.randint(2, 4))]
    [password_list.append(random.choice(symbols))
     for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please do not leave the fields empty")

    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading the old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                # json.dump(new_data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    try:
        with open("data.json", mode="r") as file:
            # Reading the old data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found.")

    else:
        if website in data:
            ret_email = data[website]["email"]
            ret_password = data[website]["password"]
            messagebox.showinfo(
                title=data[website], message=f"Email: {ret_email} \nPassword: {ret_password}")
        else:
            messagebox.showinfo(
                title="No", message=f"No details for {website} that exist in the file")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
# window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS
# website_label
website_label = Label(text="Website:", font=("Arial", 20, "bold"))
website_label.grid(column=0, row=1)


# email/Username labels
email_username = Label(text="Email/Username:", font=("Arial", 20, "bold"))
email_username.grid(column=0, row=2)

# passowrd label
password_label = Label(text="Password:", font=("Arial", 20, "bold"))
password_label.grid(column=0, row=3)


# ENTRIES
# website entry
website_entry = Entry(width=25)
website_entry.grid(column=1, row=1)
website_entry.focus()


# email Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "aboynaza@u.rochester.edu")


# password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# BUTTONS

# generate Password button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


# search button
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, columnspan=2)


window.mainloop()
