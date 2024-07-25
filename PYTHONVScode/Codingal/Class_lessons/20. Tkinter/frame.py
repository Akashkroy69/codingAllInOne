from tkinter import *

root = Tk()

# gui logic
root.geometry("500x500")
frame_1 = Frame(root, bg="black",borderwidth=6,relief=SUNKEN,padx=50)
frame_1.pack(side=LEFT,fill=Y)

label = Label(frame_1,text="Welcome to my VS Code",bg="purple",fg="white",padx=10,pady=10)
label.pack(pady=40)

frame_2 = Frame(root, bg="black",borderwidth=6,relief=SUNKEN)
frame_2.pack(side=TOP,fill=X)

label1 = Label(frame_2,text="test",bg="purple",fg="white",padx=10,pady=10)
label1.pack(padx=40)






# main loop
root.mainloop()