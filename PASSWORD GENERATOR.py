import random
import pyperclip
from tkinter import *
from tkinter.ttk import *


def generate_password():
    length = var1.get()
    password = ""

    if var.get() == 1:  # Low Strength
        characters = "abcdefghijklmnopqrstuvwxyz"
    elif var.get() == 0:  # Medium Strength
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif var.get() == 3:  # Strong Strength
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

    if length > 0:
        password = "".join(random.choice(characters) for _ in range(length))
        password_label.config(text="" + password)
        pyperclip.copy(password)


root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
root.geometry("450x250")
root.config(bg="#3498db")

style = Style()
style.configure("TRadiobutton", background="#3498db", foreground="white")

label = Label(root, text="Password Generator", font=("Arial Bold", 20), background="#3498db", foreground="white")
label.grid(row=0, column=0, columnspan=4, pady=10)

password_label = Label(root, text="Password:", background="#3498db", foreground="white")
password_label.grid(row=1, column=0, pady=5)

# Use a Label to display the password
password_label = Label(root, text="", background="#3498db", foreground="black", font=("Arial", 18))
password_label.grid(row=1, column=1, columnspan=2, pady=5)

length_label = Label(root, text="Length:", background="#3498db", foreground="white")
length_label.grid(row=2, column=0, pady=5)

combo = Combobox(root, textvariable=var1, state="readonly", font=("Arial", 14), values=list(range(8, 33)))
combo.grid(row=2, column=1, pady=5)
combo.current(0)

strength_label = Label(root, text="Strength:", background="#3498db", foreground="white")
strength_label.grid(row=3, column=0, pady=5)

low_strength = Radiobutton(root, text="Low", variable=var, value=1, style="TRadiobutton")
low_strength.grid(row=3, column=1, pady=5)

medium_strength = Radiobutton(root, text="Medium", variable=var, value=0, style="TRadiobutton")
medium_strength.grid(row=3, column=2, pady=5)

strong_strength = Radiobutton(root, text="Strong", variable=var, value=3, style="TRadiobutton")
strong_strength.grid(row=3, column=3, pady=5)

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
