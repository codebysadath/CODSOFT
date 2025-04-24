import tkinter as tk

# === Colors & Fonts ===
BG_COLOR = "#2e2e2e"
DISPLAY_BG = "#1e1e1e"
DISPLAY_FG = "#00ff88"
# Material-inspired color palette
DIGIT_BG = "#03A9F4"        # Light Blue for digits
DIGIT_HOVER = "#29B6F6"
OP_BG = "#4CAF50"           # Green for operators
OP_HOVER = "#66BB6A"
SPECIAL_BG = "#9C27B0"      # Purple for '='
SPECIAL_HOVER = "#AB47BC"
CLEAR_BG = "#F44336"        # Red for 'C'
CLEAR_HOVER = "#E57373"
BTN_FG = "#ffffff"
FONT_BTN = ("Arial Rounded MT Bold", 18)
FONT_DISPLAY = ("Arial Rounded MT Bold", 32)

# === Main Window ===
root = tk.Tk()
root.title("🧮 Calculator")
root.geometry("400x550")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# === Expression Storage ===
expression = ""
equation = tk.StringVar()

# === Functions ===
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")


def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except Exception:
        equation.set("Error")
        expression = ""

# === Hover Effects ===
def on_enter(e, widget, hover_color):
    widget['bg'] = hover_color

def on_leave(e, widget, original_color):
    widget['bg'] = original_color

# === Display ===
display = tk.Entry(root, textvariable=equation,
                   font=FONT_DISPLAY,
                   bg=DISPLAY_BG, fg=DISPLAY_FG,
                   bd=0, justify="right", insertbackground=DISPLAY_FG)
display.pack(expand=True, fill="both", padx=10, pady=10)

# === Button Grid ===
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(expand=True, fill="both")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(btn_frame, bg=BG_COLOR)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        # Determine colors and command
        if char == 'C':
            bg, hover, cmd = CLEAR_BG, CLEAR_HOVER, clear
        elif char == '=':
            bg, hover, cmd = SPECIAL_BG, SPECIAL_HOVER, equal
        elif char in ['+', '-', '*', '/']:
            bg, hover, cmd = OP_BG, OP_HOVER, lambda x=char: press(x)
        else:
            bg, hover, cmd = DIGIT_BG, DIGIT_HOVER, lambda x=char: press(x)

        btn = tk.Button(row_frame, text=char,
                        font=FONT_BTN,
                        bg=bg, fg=BTN_FG,
                        bd=0, relief='flat',
                        activebackground=hover,
                        command=cmd)
        btn.pack(side="left", expand=True, fill="both", padx=6, pady=6)
        # Bind hover effects
        btn.bind("<Enter>", lambda e, w=btn, h=hover: on_enter(e, w, h))
        btn.bind("<Leave>", lambda e, w=btn, o=bg: on_leave(e, w, o))

# === Run App ===
root.mainloop()
