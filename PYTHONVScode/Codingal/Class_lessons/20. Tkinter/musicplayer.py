import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")

        self.playlist = []

        # Create and configure the buttons
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=10)

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.playlist[0])
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def add_song(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            print(f"Added: {file_path}")

if __name__ == "__main__":
  root = tk.Tk()
  music_player = MusicPlayer(root)
#   music_player1 = MusicPlayer(root)
#   music_player2 = MusicPlayer(root)
  root.mainloop()


# The line if __name__ == "__main__": is a common Python idiom used to determine if the Python script 
# is being run as the main program or if it is being imported as a module into another script.