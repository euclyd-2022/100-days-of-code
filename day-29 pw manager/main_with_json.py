from tkinter import *
from tkinter import messagebox
import random
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    pw_input.delete(0, END)

    #list comprehensions for random letter, number and symbol

    ascii_letters = range(97, 122) # ascii lowercase a-z
    new_letter = [chr(random.choice(ascii_letters)) for _ in range(random.randint(6, 8))]


     #convert to character from number

    numbers = range(0,9)
    new_number = [str(random.choice(numbers)) for _ in range(random.randint(2, 4))]


    symbols = range(33, 47)
    new_symbol =  [chr(random.choice(symbols)) for _ in range(random.randint(2, 4))]

    password_list = new_letter + new_number + new_symbol

    random.shuffle(password_list)
    password = "".join(password_list)
    pw_input.insert(0, password)
    copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = pw_input.get()
    website = website_input.get()
    email = email_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if password == "" or website == "":
        messagebox.showinfo(title="Error", message="There are empty fields")
        is_ok = False
    else:

        try:
            with open("pw_doc.json", "r") as data_file:
                print(f"{website} | {email} | {password} \n")
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("pw_doc.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4) #dump the new data
        else:
            # update with new data
            data.update(new_data)

            with open("pw_doc.json", "w") as data_file:
                # save updated data
                json.dump(data, data_file, indent=4)  # dump including the old data
                print(data)
        finally:
                pw_input.delete(0, END)
                website_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
#image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)



website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.insert(0, "p@c.com")
email_input.grid(column=1, row=2, columnspan=2)
email = email_input.get()

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)
pw_input = Entry(width=21)
pw_input.grid(column=1, row=3)
pw_button = Button(text="Generate Password", command=password_gen)
pw_button.grid(column=2, row=3)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

