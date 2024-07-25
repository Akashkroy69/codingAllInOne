from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Grid Layout")

# functions
def getVals():
    print(f"value of username is : {userValue.get()}")
    print(f"value of username is : {passwordValue.get()}")

userName = Label(root, text="UserName")
password = Label(root, text="password")
# userName.pack()
# password.pack()
userName.grid(row=0)
password.grid(row=1)

# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
# about Entry Widget
userValue = StringVar()
passwordValue = StringVar()
userEntry = Entry(root, textvariable=userValue)
passwordEntry = Entry(root, textvariable=passwordValue)


userEntry.grid(row=0,column=1)
passwordEntry.grid(row=1,column=1)

# button in another way
Button(text="submit", command=getVals).grid()

# resultValue = userValue + passwordValue
# resultEntry = Entry(root, textvariable="resultValue")
# result = Label(root, text="Result")
# result.grid(row=4,column=0)
# resultEntry.grid(row=4,column=1)



root.mainloop()