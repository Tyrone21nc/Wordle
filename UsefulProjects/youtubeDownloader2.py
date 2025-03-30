import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
	try:
		ytLink = my_link.get()
		print(f"Youtube link ---->{ytLink}")
		print("My link ------>   https://www.youtube.com/watch?v=dLixMzBw2j8")
		ytObject = YouTube(ytLink)
		video = ytObject.streams.get_highest_resolution()
		video.download()
		print("Download Complete")
	except:
		print("Youtube link is invalid")
		print("Download Incomplete")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
my_link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
my_link.pack()


# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()