from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    password += "".join([random.choice(string.ascii_uppercase) for _ in range(4)])
    password += "".join([random.choice(string.ascii_lowercase) for _ in range(4)])
    password += "".join([random.choice(string.digits) for _ in range(4)])
    password += "".join([random.choice(string.punctuation) for _ in range(4)])
    password = "".join(random.sample(password, len(password)))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------- Search Websites ------------------------------ #
def search():
    website = website_entry.get()
    try:
        with open("00_projects/21_password_manager/data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data.keys():
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showwarning(title="Error", message=f"No details for {website} found.")
    
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        )

        if is_ok:
            new_data = {website: {"email": email, "password": password}}
            try:
                with open("00_projects/21_password_manager/data.json", "r") as data_file:
                    pass
            except FileNotFoundError:
                with open("00_projects/21_password_manager/data.json", "w") as data_file:
                    pass

            with open("00_projects/21_password_manager/data.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                    data.update(new_data)
                except json.JSONDecodeError:
                    data = new_data

            with open("00_projects/21_password_manager/data.json", "w") as data_file:                
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="00_projects/21_password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(width=15, text="Search", bg="white", highlightthickness=0, command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(
    text="Generate Password",
    bg="white",
    highlightthickness=0,
    command=generate_password,
)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, bg="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
