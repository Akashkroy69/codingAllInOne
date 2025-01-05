import tkinter as tk

root = tk.Tk()
root.title("Simple Form")
root.geometry("300x200")

# Using grid layout
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

def submit():
    print(f"Name: {entry_name.get()}")
    print(f"Age: {entry_age.get()}")
    btn_submit.place(50,50)

btn_submit = tk.Button(root, text="Submit", command=submit)
btn_submit.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
