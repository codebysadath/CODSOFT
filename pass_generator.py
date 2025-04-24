import tkinter as tk
import random
import string

# === Main Window ===
root = tk.Tk()
root.title("🔑 Password Generator")
root.geometry("450x400")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# === Password Display with Show/Hide ===
password_var = tk.StringVar()
show_password = False

display_frame = tk.Frame(root, bg="#f0f0f0")
display_frame.pack(pady=20)

display = tk.Entry(display_frame, textvariable=password_var,
                   font=("Arial", 14), width=25,
                   bg="#ffffff", fg="#000000",
                   bd=1, relief="solid", justify="center")
display.grid(row=0, column=0)

def toggle_show():
    global show_password
    show_password = not show_password
    display.config(show="" if show_password else "*")
    show_btn.config(text="Hide" if show_password else "Show")

show_btn = tk.Button(display_frame, text="Show", command=toggle_show,
                     font=("Arial", 10), bg="#888888", fg="#ffffff", bd=0)
show_btn.grid(row=0, column=1, padx=5)

# === Strength Meter ===
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12), bg="#f0f0f0")
strength_label.pack(pady=5)

strength_bar = tk.Frame(root, bg="#cccccc", height=10, width=300)
strength_bar.pack(pady=2)
strength_fill = tk.Frame(strength_bar, bg="#ff0000", height=10, width=0)
strength_fill.pack(side="left")

def assess_strength(pw: str):
    length = len(pw)
    categories = sum(bool(any(c in s for c in pw))
                     for s in [string.ascii_letters, string.digits, string.punctuation])
    if length >= 16 and categories == 3:
        return "Strong", "#00cc44", 300
    if length >= 12 and categories >= 2:
        return "Medium", "#ffa500", 200
    return "Weak", "#ff4444", 100

# === Generation Logic ===
def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    pw = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(pw)
    display.config(show="" if show_password else "*")
    # update strength
    strength, color, width = assess_strength(pw)
    strength_label.config(text=f"Strength: {strength}")
    strength_fill.config(bg=color, width=width)

# === Controls ===
# Length Slider
tk.Label(root, text="Length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_slider = tk.Scale(root, from_=8, to=24, orient="horizontal",
                         font=("Arial", 10), bg="#f0f0f0", length=300)
length_slider.set(12)
length_slider.pack()

# Checkboxes
opts_frame = tk.Frame(root, bg="#f0f0f0")
opts_frame.pack(pady=10)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(opts_frame, text="Include Digits", var=use_digits,
               bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=10)
tk.Checkbutton(opts_frame, text="Include Symbols", var=use_symbols,
               bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=1, padx=10)

# Generate & Copy Buttons
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Generate", font=("Arial", 12),
          bg="#4caf50", fg="#ffffff", bd=0,
          command=lambda: generate_password(
              length_slider.get(),
              use_digits.get(),
              use_symbols.get()
          )).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Copy", font=("Arial", 12),
          bg="#2196f3", fg="#ffffff", bd=0,
          command=copy_to_clipboard).grid(row=0, column=1, padx=10)

# === Start App ===
root.mainloop()