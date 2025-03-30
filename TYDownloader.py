"""
Download some YouTube videos
"""
from pytube import YouTube
import os

# Input URL of the YouTube video
video_url = input("Enter the YouTube video URL: ")

# Specify the destination folder where you want to download the video
download_folder = input("Enter the destination folder (e.g., C:/Downloads or /home/user/Videos): ")

# Check if the folder exists, if not, create it
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Create a YouTube object
yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)


# Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Download the video to the specified directory
print("Downloading...")
stream.download(output_path=download_folder)
print(f"Download complete! Video saved to {download_folder}")


