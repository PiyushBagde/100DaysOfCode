import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_random_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Title', message='details missing')

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"There are the entered details: \nEmail : {email} \nPassword: {password}\nClick 'Ok' to save password.")
        if is_ok:
            try:
                with open("data.json", mode='r') as data_file:
                    # json.dump() used to write data in json file
                    # json.dump(new_data, data_file, indent=4)
                    data = json.load(data_file)  # load the data from json file # reading the data

            except FileNotFoundError:
                with open("data.json", mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)  # dumping new data
            else:
                data.update(new_data)  # updating the existing data
                with open("data.json", mode='w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(END, 'iamnotspare@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', command=generate_random_password, bg='#8E8FFA')
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=add_entry, bg='#1D24CA', fg='white')
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
