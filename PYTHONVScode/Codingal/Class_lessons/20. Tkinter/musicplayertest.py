import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")

        # buttons
        self.playButton = tk.Button(root, text= "play",command=self.play)
        self.playButton.pack(pady=20)
        self.playButton = tk.Button(root, text= "pause",command=self.pause)
        self.playButton.pack(pady=20)
        self.playButton = tk.Button(root, text= "stop",command=self.stop)
        self.playButton.pack(pady=20)
        self.playButton = tk.Button(root, text= "add music",command=self.addMusic)
        self.playButton.pack(pady=20)

        # functions to control
        def play(self):
            pass
        def pause(self):
            pass
        def stop(self):
            pass
        def addMusic(self):
            pass

# gui
root = tk.Tk()
root.geometry("200x300")
musicPlayer = MusicPlayer(root=root)
root.mainloop()