import tkinter as tk
import random
user_score = 0
computer_score = 0
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    return result
def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score}\nComputer Score: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Your Score: {user_score}\nComputer Score: {computer_score}")
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
tk.Label(root, text="Choose rock, paper, or scissors:").pack()
button_frame = tk.Frame(root)
button_frame.pack()
tk.Button(button_frame, text="Rock", command=lambda: play("rock")).pack(side=tk.LEFT)
tk.Button(button_frame, text="Paper", command=lambda: play("paper")).pack(side=tk.LEFT)
tk.Button(button_frame, text="Scissors", command=lambda: play("scissors")).pack(side=tk.LEFT)
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()
score_label = tk.Label(root, text=f"Your Score: {user_score}\nComputer Score: {computer_score}", font=("Helvetica", 14))
score_label.pack()
tk.Button(root, text="Play Again", command=reset_game).pack()
root.mainloop()
