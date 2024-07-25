import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to display input/output
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers and operations
        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons
        for (text, row, col) in self.buttons:
            btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col)

        # Bind Enter key to the equals button
        root.bind('<Return>', lambda event: self.on_button_click('='))

    def on_button_click(self, symbol):
        current = self.entry.get()

        # Perform calculation
        if symbol == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        # Clear the entry field
        elif symbol == 'C':
            self.entry.delete(0, tk.END)
        # Append the symbol to the entry field
        else:
            self.entry.insert(tk.END, symbol)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
