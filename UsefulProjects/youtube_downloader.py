from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)


my_url = "https://www.youtube.com/watch?v=rPVlKOc0-rs"
my_save_path = "C:\\Users\\thier\\DownloadedYoutubeVideos"
download_video(my_url, my_save_path)
