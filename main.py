import tkinter as tk
from tkinter import messagebox
import hashlib
import re

def check_password_strength(password):
    criteria = [
        (len(password) >= 8, "At least 8 characters"),
        (re.search(r"[a-z]", password), "Lowercase letter"),
        (re.search(r"[A-Z]", password), "Uppercase letter"),
        (re.search(r"\d", password), "Digit"),
        (re.search(r"[@$!%*?&]", password), "Special character"),
    ]
    
    passed_criteria = sum(1 for condition, _ in criteria if condition)
    messages = [msg for condition, msg in criteria if not condition]
    
    strength_levels = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
    
    return strength_levels.get(passed_criteria, "Very Weak"), messages

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    
    strength, missing_criteria = check_password_strength(password)
    hashed_password = hash_password(password)
    
    feedback = f"Password Strength: {strength}\nSHA-256 Hash: {hashed_password}"
    if missing_criteria:
        feedback += "\nMissing: " + ", ".join(missing_criteria)
    
    result_label.config(text=feedback)

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("420x320")
root.resizable(False, False)

tk.Label(root, text="Enter Password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_password).pack(pady=10)

result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

root.mainloop()
