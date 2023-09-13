from tkinter import *
import random


def reset_game():
    result_label.config(text="")
    player_choice.set("Your Choice")
    computer_choice.set("Computer's Choice")


def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice.set(random.choice(choices))

    if player_choice == computer_choice.get():
        result_label.config(text="It's a tie!")
    elif (
            (player_choice == "Rock" and computer_choice.get() == "Scissors")
            or (player_choice == "Paper" and computer_choice.get() == "Rock")
            or (player_choice == "Scissors" and computer_choice.get() == "Paper")
    ):
        result_label.config(text="You Win!", fg="green")
    else:
        result_label.config(text="Computer Wins!", fg="red")


root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x300")
root.configure(bg="#3498db")

player_choice = StringVar()
computer_choice = StringVar()

frame = Frame(root, bg="#3498db")
frame.pack(pady=20)

Label(frame, text="Rock Paper Scissors", font=("Arial Bold", 20), fg="white", bg="#3498db").grid(row=0, column=0, columnspan=3, pady=10)

Label(frame, textvariable=player_choice, font=("Arial", 16), fg="white", bg="#3498db").grid(row=1, column=0, pady=10, padx=20)

Label(frame, text="VS", font=("Arial", 16), fg="white", bg="#3498db").grid(row=1, column=1, pady=10)

Label(frame, textvariable=computer_choice, font=("Arial", 16), fg="white", bg="#3498db").grid(row=1, column=2, pady=10, padx=20)

result_label = Label(frame, text="", font=("Arial Bold", 16), fg="black", bg="white")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

Button(frame, text="Rock", font=("Arial", 14), width=8, command=lambda: play_game("Rock")).grid(row=3, column=0, padx=10)

Button(frame, text="Paper", font=("Arial", 14), width=8, command=lambda: play_game("Paper")).grid(row=3, column=1, padx=10)

Button(frame, text="Scissors", font=("Arial", 14), width=8, command=lambda: play_game("Scissors")).grid(row=3, column=2, padx=10)

Button(root, text="Reset Game", font=("Arial", 14), fg="white", bg="red", command=reset_game).pack(pady=20)

root.mainloop()
