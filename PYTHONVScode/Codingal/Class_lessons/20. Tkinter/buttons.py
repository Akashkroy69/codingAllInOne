from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Testing Buttons")

# function
def hello():
    print("hello Buddy!!")


frame = Frame(root, bg="purple", borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

button1 = Button(frame, fg="white", bg="black", text="Button 1",command=hello)
button1.pack(side=LEFT,padx=10,pady=10)

button2 = Button(frame, fg="white", bg="black", text="Button 2")
button2.pack(side=LEFT)

button3 = Button(frame, fg="white", bg="black", text="Button 2")
button3.pack(side=LEFT)

button4 = Button(frame, fg="white", bg="black", text="Button 4")
button4.pack(side=LEFT)

root.mainloop()

# grid layout