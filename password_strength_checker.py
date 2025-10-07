import tkinter as tk
import re

# Function to check password strength
def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    if strength == 5:
        return "🟢 Strong Password", "lime"
    elif strength >= 3:
        return "🟡 Moderate Password", "orange"
    else:
        return "🔴 Weak Password", "red"

def check_strength_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("❌ Password must be at least 8 characters long")
    if not re.search(r'[a-z]', password):
        feedback.append("❌ Add lowercase letters (a-z)")
    if not re.search(r'[A-Z]', password):
        feedback.append("❌ Add uppercase letters (A-Z)")
    if not re.search(r'\d', password):
        feedback.append("❌ Add digits (0-9)")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        feedback.append("❌ Add special characters (!@#$...)")
    return feedback

def evaluate_password():
    password = entry.get()
    result, color = check_strength(password)
    strength_label.config(text=result, fg=color)
    feedback_list.delete(0, tk.END)
    for message in check_strength_feedback(password):
        feedback_list.insert(tk.END, message)

# UI Setup
root = tk.Tk()
root.title("💡 Password Strength Checker")
root.geometry("500x400")
root.configure(bg="#121212")
root.resizable(False, False)

# Styling
style_font = ("Segoe UI", 12)
title_font = ("Segoe UI", 18, "bold")

# Title
tk.Label(root, text="🔐 Password Strength Checker", font=title_font, bg="#121212", fg="#00ffe1").pack(pady=20)

# Entry Frame for rounded effect
entry_frame = tk.Frame(root, bg="#1f1f1f", bd=2)
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, show="*", font=style_font, bg="#1f1f1f", fg="white", insertbackground="white", width=30, relief=tk.FLAT)
entry.pack(padx=10, pady=8)

# Button with hover effect
def on_enter(e):
    check_button['background'] = '#00ffe1'
    check_button['foreground'] = '#000'

def on_leave(e):
    check_button['background'] = '#333'
    check_button['foreground'] = '#fff'

check_button = tk.Button(root, text="Check Strength", command=evaluate_password, bg="#333", fg="white",
                         font=("Segoe UI", 12, "bold"), bd=0, padx=20, pady=8, cursor="hand2", activebackground="#555")
check_button.pack(pady=5)
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

# Strength Label
strength_label = tk.Label(root, text="", font=("Segoe UI", 14, "bold"), bg="#121212")
strength_label.pack(pady=10)

# Feedback ListBox
feedback_list = tk.Listbox(root, width=60, height=6, font=("Consolas", 10), bg="#1f1f1f", fg="#eeeeee", bd=0, highlightthickness=0)
feedback_list.pack(pady=10)

# Start GUI
root.mainloop()
