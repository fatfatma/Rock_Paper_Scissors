import random
import tkinter as tk
from tkinter import messagebox

options = ["rock", "paper", "scissors"]
rock = options[0]
paper = options[1]
scissors = options[2]

def play(user_choice):
    computer_choice = random.choice(options)
    result = ""

    if user_choice == rock:
        if computer_choice == rock:
            result = "Computer chose: Rock\nResult: Draw"
        elif computer_choice == paper:
            result = "Computer chose: Paper\nYou lost"
        else:
            result = "Computer chose: Scissors\nYou won"
    if user_choice == paper:
        if computer_choice == rock:
            result = "Computer chose: Rock\nYou won"
        elif computer_choice == paper:
            result = "Computer chose: Paper\nResult: Draw"
        else:
            result = "Computer chose: Scissors\nYou lost"
    if user_choice == scissors:
        if computer_choice == rock:
            result = "Computer chose: Rock\nYou lost"
        elif computer_choice == paper:
            result = "Computer chose: Paper\nYou won"
        else:
            result = "Computer chose: Scissors\nResult: Draw"

    messagebox.showinfo("Game Result", result)

# GUI design
window = tk.Tk()
window.title("Rock Paper Scissors Game")

label = tk.Label(window, text="Welcome to the Game!", font=("Arial", 16))
label.pack(pady=10)

btn_rock = tk.Button(window, text="Rock", width=20, command=lambda: play("rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(window, text="Paper", width=20, command=lambda: play("paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(window, text="Scissors", width=20, command=lambda: play("scissors"))
btn_scissors.pack(pady=5)

window.mainloop()
