import json
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = " ".join(password_list)

    print(f"Your password is: {password}")

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error",
                                   message="Data Not Found")


def add_button():
    print("I got clicked")
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please dont leave some fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Website",
                                       message=f"These are details entered:\nEmail: {username}\nPassword: {password}\nIs it ok to save?")
        # if is_ok:
        #     with open("data.txt", "a") as file:
        #         file.write(f"{website}|{username}|{password}\n")
        #         website_input.delete(0, END)
        #         password_input.delete(0, END)
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Airal", 10))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Airal", 10))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Airal", 10))
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=51)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "angela@abc.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

# button


search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=add_button)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
