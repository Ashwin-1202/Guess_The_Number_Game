import tkinter as tk
import random
number_to_guess = random.randint(1, 100)
attempts = 0
def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="Enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        result_label.config(text="Too Low! Try Again!")
    elif guess > number_to_guess:
        result_label.config(text="Too High! Try Again! ")
    else:
        result_label.config(text=f"Correct! 🎉 Attempts: {attempts}")

def restart_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    result_label.config(text="")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Guess The Number Game")
root.geometry("350x250")

title_label = tk.Label(root, text="Guess the Number (1-100)", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.pack(pady=5)

root.mainloop()