from tkinter import *

win = Tk()
win.title("Simple Form")
win.geometry("300x200")

def keyPress_(event):
    print(f"Key pressed: {event.char}")
    if event.char == 'q':
        win.destroy()


win.bind("<Key>", keyPress_)


def on_left_click(event):
    print(f"Left click at ({event.x}, {event.y})")

def on_motion(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

win.bind("<Motion>", on_motion)


win.bind("<Button-1>", on_left_click)



win.mainloop()

