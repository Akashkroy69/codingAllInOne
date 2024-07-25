from tkinter import *
from PIL import Image,ImageTk
from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import time

root = Tk()

def downloadVid():
    src = sourceLink.get()

    yt = YouTube(src)
    stream = yt.streams.get_highest_resolution()
    savePath = r"C:\Users\akash\downloads"
    message = stream.download(output_path=savePath)
    for i in range(101):
        time.sleep(0.05)  # Simulate processing time
        progress_var.set(i)  # Update progress bar
        root.update_idletasks()  # Update GUI
    progress_var.set(0)

    print("Download successful!",message)
    

root.geometry("833x533")
root.minsize(833,533)
root.maxsize(833,533)
root.title("Youtube Downloader")
# setting the background as red
root.configure(bg="red")
# setting the icon
root.iconbitmap(r"Codingal\Additional Projects\youtubeDownloader\yticon.ico")

# method 1
# photo = PhotoImage(file=r"Codingal\Class_lessons\20. Tkinter\Tkinter_Repractice\ytD.png")
# imgLabel = Label(image=photo)
# imgLabel.pack()

# frame for image
frameForLogo = Frame(root,bg="white",borderwidth=10,relief="raised")
frameForLogo.pack(side=LEFT,fill="both")

# method 2
image = Image.open(r"Codingal\Additional Projects\youtubeDownloader\ytD.png")
photo = ImageTk.PhotoImage(image=image)
imgLabel = Label(frameForLogo,image=photo,border=10, relief="sunken",padx=10,pady=10)
imgLabel.pack(pady=(frameForLogo.winfo_height()//2)  ,padx=1)


# side= top, bottom,left,right

enterLinkFrame = Frame(root,borderwidth=3,relief="sunken",bg="white")
enterLinkFrame.pack(padx=10,pady=10)
enterLinkFrame.place(x=366,y=100)
enterLabel = Label(enterLinkFrame,text="Enter Your Link Here",font=("comicsansms",20,"bold"),fg="red",bg="white")
enterLabel.pack(padx=5,pady=5)

# input-------------------1
sourceLink = StringVar()
sourceLinkInput = Entry(enterLinkFrame,textvariable=sourceLink,borderwidth=10,relief="ridge",font=("comicsansms",20,"bold"))
sourceLinkInput.pack(fill=X,padx=5,pady=5)

# button code
frameForText = Frame(root,bg="white")
frameForText.pack()
frameForText.place(x=410,y=200)
# ---------------------- onclick
button = Button(enterLinkFrame,text="Download From YOUTUBE",bg="white",fg="red", 
             padx=3,pady=3,font=("comicsansms",10,"bold"),borderwidth=3,relief="raised",command=downloadVid)
button.pack(side=TOP,padx=5,pady=15)

# progress bar
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(enterLinkFrame, mode='determinate', variable=progress_var)
progress_bar.pack(pady=10)


root.mainloop()