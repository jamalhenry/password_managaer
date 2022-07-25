from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Function created to save the passwords once the "add" button is clicked
def save():
   web = website_entry.get()
   user = username_entry.get()
   password = password_entry.get()
   if len(web) == 0 or len(password) == 0:
       messagebox.showerror(message="Please do not leave any fields empty!")
   else:
       #Message box that ask the user if they would like to save the password
       is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail/Username: {user} " 
                              f"\nPassword: {password} \n Is it ok to save?")
       if is_ok:
           #Writing the information to a file named data.txt
           with open("data.txt", mode="a") as file:
               file.write(f"{web} | {user} | {password}\n")
               website_entry.delete(0, END)
               password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#Create window with Tkinter

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Use Canvas to import picture
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
#Email/Username Label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
#Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Website input
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
#Username input
username_entry= Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "jamalhenry.com")
#Password input
password_entry= Entry(width=18)
password_entry.grid(column=1, row=3)


#Password Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
#Add Button
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)










window.mainloop()
