import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkVideoPlayer import TkinterVideo

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        # Create and configure the video player
        self.video_player = TkinterVideo(master=root, scaled=True)
        self.video_player.pack(expand=True, fill="both")

        # Create and configure the file selection button
        self.select_button = tk.Button(root, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=10)

    def select_video(self):
        file_path = tk.filedialog.askopenfilename(defaultextension=".mp4", filetypes=[("Video files", "*.mp4")])
        if file_path:
            self.video_player.load(file_path)
            self.video_player.play()

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
