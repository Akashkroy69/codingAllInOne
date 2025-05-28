# Create an app where:

#     A Label shows “Move the mouse!”

#     As you move the mouse, update the label to show the position.

#     If you press the Escape key, exit the program.

import tkinter as tk

def on_mouse_move(event):
    # Update label with mouse position
    label.config(text=f"Mouse at ({event.x}, {event.y})")

def on_escape(event):
    # Exit the program when Escape key is pressed
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Mouse Tracker")
root.geometry("400x300")

# Create the label
label = tk.Label(root, text="Move the mouse!", font=("Arial", 16))
label.pack(pady=50)

# Bind mouse motion to the on_mouse_move function
root.bind("<Motion>", on_mouse_move)

# Bind Escape key to exit
root.bind("<Escape>", on_escape)

# Run the app
root.mainloop()
