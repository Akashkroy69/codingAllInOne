# import yt_dlp
# url = input()

# ydl_opts = {}


# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([url])
# print("video downloaded successful!!")

from pytube import YouTube

def download_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        message = stream.download(output_path=save_path)
        
        print("Download successful!",message)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
# Ask the user for the save path
save_path = r"C:\Users\akash\downloads" #input("Enter the path where you want to save the video: ")
# Download the video
download_video(video_url, save_path)
