import tkinter as tk
from tkinter import messagebox

# Theme colors
BG_COLOR = "#f7f7f7"
BTN_COLOR = "#4CAF50"
BTN_TEXT_COLOR = "white"
LISTBOX_BG = "#ffffff"
FONT = ("Helvetica", 12)

# Create the main window
root = tk.Tk()
root.title("🌟 My To-Do List")
root.geometry("400x500")
root.configure(bg=BG_COLOR)

# List to store tasks
tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task = tasks[index]
        confirm = messagebox.askyesno("Delete Task", f"Delete task: '{task['task']}'?")
        if confirm:
            tasks.pop(index)
            update_listbox()
    except IndexError:
        pass

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_listbox()
    except IndexError:
        pass

def edit_task():
    try:
        index = task_listbox.curselection()[0]
        old_task = tasks[index]["task"]
        new_task = simple_input_dialog("Edit Task", f"Update task:", old_task)
        if new_task:
            tasks[index]["task"] = new_task
            update_listbox()
    except IndexError:
        pass

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️ " if task["done"] else "🔲 "
        task_listbox.insert(tk.END, status + task["task"])

def simple_input_dialog(title, prompt, default_text=""):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry("300x150")
    dialog.configure(bg=BG_COLOR)

    tk.Label(dialog, text=prompt, bg=BG_COLOR, font=FONT).pack(pady=10)
    entry = tk.Entry(dialog, width=30, font=FONT)
    entry.insert(0, default_text)
    entry.pack(pady=5)
    entry.focus()

    def submit():
        dialog.result = entry.get()
        dialog.destroy()

    tk.Button(dialog, text="Save", bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=FONT, command=submit).pack(pady=10)

    dialog.result = None
    dialog.wait_window()
    return dialog.result

# === GUI Layout ===

# Title
tk.Label(root, text="📝 My To-Do List", bg=BG_COLOR, fg="#333", font=("Helvetica", 18, "bold")).pack(pady=10)

# Task entry
task_entry = tk.Entry(root, width=30, font=FONT)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add", width=10, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=FONT, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Delete", width=10, bg="#e74c3c", fg=BTN_TEXT_COLOR, font=FONT, command=delete_task).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Done", width=10, bg="#3498db", fg=BTN_TEXT_COLOR, font=FONT, command=mark_done).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Edit", width=10, bg="#f39c12", fg=BTN_TEXT_COLOR, font=FONT, command=edit_task).grid(row=1, column=1, padx=5, pady=5)

# Task list
task_listbox = tk.Listbox(root, width=40, height=15, font=FONT, bg=LISTBOX_BG, selectbackground="#dcdcdc")
task_listbox.pack(pady=10)

# Start the app
root.mainloop()
