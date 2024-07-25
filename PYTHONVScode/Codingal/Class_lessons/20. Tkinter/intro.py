from tkinter import *
from PIL import Image,ImageTk

tkinterObject = Tk()

# gui logic
tkinterObject.geometry("500x500")
tkinterObject.minsize(100,100)
tkinterObject.maxsize(600,600)

tkinterObject.title("TKINTER Experimanet")
# 1 for text
# label text
text = Label(text="Hi Alsan",bg="pink",fg="blue",padx=10,
             pady=20,font=("comicsansms",40,"bold"),borderwidth=10,relief=RIDGE)
# SUNKEN, RAISED, GROOVE, RIDGE
# font="comicsansms 10 bold"


# pack attributes
# anchor: nw,ne,
# side: TOP, BOTTOM, right, left
# fill
# text.pack(side=BOTTOM, anchor="sw",fill=X)
text.pack(side=LEFT,fill=Y,pady=20,padx=20)


# 2 for png
# photo = PhotoImage(file=r"Codingal\Class_lessons\20. Tkinter\pipe.png")
# imageLabel = Label(image=photo)
# imageLabel.pack()

# 3 for jpg
# photo = ImageTk.PhotoImage(file=r"Codingal\Class_lessons\20. Tkinter\updown3.jpg")
# imageLabel = Label(image=photo)
# imageLabel.pack()


# text = Label(text="hi Alsan",bg="red",fg="white")
# text.pack()

tkinterObject.mainloop()    


# pip install pillow