import tkinter as tk
from tkinter import messagebox
import json

# Initialize window
root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x300")

# Labels and Entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Feedback:").grid(row=2, column=0, padx=10, pady=5)
entry_feedback = tk.Text(root, width=25, height=5)
entry_feedback.grid(row=2, column=1, padx=10, pady=5)

# Function to save feedback
def save_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END).strip()

    if not name or not email or not feedback:
        messagebox.showwarning("Incomplete", "Please fill in all fields!")
        return

    # Create feedback dictionary
    feedback_data = {
        "Name": name,
        "Email": email,
        "Feedback": feedback
    }

    # Save to file
    with open("feedback.json", "a") as file:
        file.write(json.dumps(feedback_data) + "\n")

    messagebox.showinfo("Saved", "Thank you for your feedback!")

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_feedback.delete("1.0", tk.END)

# Submit Button
btn_submit = tk.Button(root, text="Submit Feedback", command=save_feedback)
btn_submit.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
