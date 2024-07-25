from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Akash Travel Agancy")

welcomeText = Label(root, text="Welcome To Akash Travel Agancy", font=("comicsansms 13 bold"))
welcomeText.grid(row=0, column=2)

# function
def submit():
    pass

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentMode = Label(root, text="Payment Mode")
# foodService = Label(root, text="Food Service")

name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
emergency.grid(row=4, column=1)
paymentMode.grid(row=5, column=1)
# foodService.grid(row=6, column=1)

# variable classes
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()
# entry widget
nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
emergencyEntry = Entry(root, textvariable=emergencyValue)
paymentModeEntry = Entry(root, textvariable=paymentModeValue)
# foodServiceEntry = Entry(root, textvariable=foodServiceValue)

nameEntry.grid(row=1, column=2)
phoneEntry.grid(row=2, column=2)
genderEntry.grid(row=3, column=2)
emergencyEntry.grid(row=4, column=2)
paymentModeEntry.grid(row=5, column=2)
# foodServiceEntry.grid(row=6, column=2)

# checkbox
foodService = Checkbutton(text="Do you want us to include meal? ", variable=foodServiceValue)
foodService.grid(row=6, column=2)

submitButton = Button(root, text="Submit to Akash Travel Agency", command=submit)
submitButton.grid(row=7, column=2)

root.mainloop()