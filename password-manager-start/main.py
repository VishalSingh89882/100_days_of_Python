from tkinter import *
from tkinter import messagebox
from turtle import save
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for i in range(nr_letters)]
    password_symbol = [random.choice(symbols) for i in range(nr_symbols)]
    password_number = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)

    password_name.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

def save():
    website = website_name.get()
    email = email_name.get()
    password = password_name.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("password-manager-start/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_name.delete(0, END)
                password_name.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)


website_label  = Label(text="Website")
website_label.grid(column=0,row=1)
email_label  = Label(text="Email/Username")
email_label.grid(column=0,row=2)
password_label  = Label(text="Password")
password_label.grid(column=0,row=3)

website_name = Entry(width=35)
website_name.grid(column=1,row=1,columnspan=2)
website_name.focus()
email_name = Entry(width=35)
email_name.grid(column=1,row=2,columnspan=2)
email_name.insert(0,"vishal@gmail.com")
password_name = Entry(width=35)
password_name.grid(column=1, row=3, columnspan=2)

generate_password_button = Button(
    text="Generate Password",
    command=password_generator)
generate_password_button.grid(column=2, row=3, sticky="ew")

Add_button = Button(text="Add", command=save)
Add_button.grid(column=1, row=4, columnspan=2, sticky="ew")









window.mainloop()