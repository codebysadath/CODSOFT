import tkinter as tk
import random

# === Setup ===
root = tk.Tk()
root.title("Rock Paper Scissors - Emoji Battle")
root.geometry("500x600")
root.config(bg="#1e1e1e")

options = ["Rock", "Paper", "Scissors"]
emojis = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

user_score = 0
cpu_score = 0

# === Fonts & Styles ===
font_title = ("Arial", 24, "bold")
font_score = ("Arial", 18)
font_move = ("Arial", 60)
font_result = ("Arial", 16)
fg_color = "#00ffee"

# === Title ===
tk.Label(root, text="Rock ✊ Paper ✋ Scissors ✌️",
         font=font_title, fg=fg_color, bg="#1e1e1e").pack(pady=20)

# === Move Display ===
move_frame = tk.Frame(root, bg="#1e1e1e")
move_frame.pack(pady=10)

user_hand = tk.Label(move_frame, text="❔", font=font_move, bg="#1e1e1e", fg="white")
vs_label = tk.Label(move_frame, text="VS", font=("Arial", 20, "bold"), fg="gray", bg="#1e1e1e")
cpu_hand = tk.Label(move_frame, text="❔", font=font_move, bg="#1e1e1e", fg="white")

user_hand.grid(row=0, column=0, padx=30)
vs_label.grid(row=0, column=1, padx=10)
cpu_hand.grid(row=0, column=2, padx=30)

# === Result Label ===
result_label = tk.Label(root, text="Make your move!", font=font_result, fg="white", bg="#1e1e1e")
result_label.pack(pady=10)

# === Score ===
score_var = tk.StringVar()
score_var.set("You: 0   |   CPU: 0")
score_label = tk.Label(root, textvariable=score_var, font=font_score, fg="white", bg="#1e1e1e")
score_label.pack(pady=10)

# === Game Logic ===
def play(user_choice):
    global user_score, cpu_score

    cpu_choice = random.choice(options)

    user_hand.config(text=emojis[user_choice])
    cpu_hand.config(text=emojis[cpu_choice])

    if user_choice == cpu_choice:
        outcome = "It's a Tie!"
    elif (user_choice == "Rock" and cpu_choice == "Scissors") or \
         (user_choice == "Paper" and cpu_choice == "Rock") or \
         (user_choice == "Scissors" and cpu_choice == "Paper"):
        user_score += 1
        outcome = "You Win!"
    else:
        cpu_score += 1
        outcome = "CPU Wins!"

    result_label.config(text=f"You chose {user_choice}, CPU chose {cpu_choice}.\n{outcome}")
    score_var.set(f"You: {user_score}   |   CPU: {cpu_score}")

# === Buttons ===
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

def create_choice_btn(label):
    return tk.Button(btn_frame, text=label, font=("Arial", 14),
                     bg="#333333", fg="white", width=10,
                     activebackground="#555555", command=lambda: play(label))

create_choice_btn("Rock").grid(row=0, column=0, padx=10)
create_choice_btn("Paper").grid(row=0, column=1, padx=10)
create_choice_btn("Scissors").grid(row=0, column=2, padx=10)

# === Reset Button ===
def reset_game():
    global user_score, cpu_score
    user_score = 0
    cpu_score = 0
    user_hand.config(text="❔")
    cpu_hand.config(text="❔")
    score_var.set("You: 0   |   CPU: 0")
    result_label.config(text="Make your move!")

tk.Button(root, text="Reset", font=("Arial", 12), bg="#ff4444", fg="white",
          activebackground="#cc3333", command=reset_game).pack(pady=15)

# === Start the App ===
root.mainloop()
