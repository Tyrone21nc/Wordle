"""
Author: Romain Dzeinse
Date: 4/13/24
Objective: Building a weather app using information, and API, from the AirNow.gov website
- Following along from YouTube video tittled: Tkinter Course - Create Graphic User Interfaces in Python Tutorial
from FreeCodeCamp recorded by John Elder, creator of Codemy
- link: https://www.youtube.com/watch?v=YXPyB4XeYLA
"""
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Romain's Weather App")
root.iconbitmap("C:\\Users\\thier\\PycharmProjects\\pythonYourProject\\UMBC_profpic.jpg")
root.geometry("600x75")
bg_color = ""


# Create Zip code Lookup
def zip_look_up():
    zip.get()
    # zip_Label = Label(root, text=zip.get())
    # zip_Label.pack()


# Weather API query link
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=21113&distance=15&API_KEY=BC0A9066-17E8-4F80-9437-F9B7B701A27B
#
try:
    # To request API
    zip_code = "20902"
    api_request = requests.get(
        f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=15&API_KEY=BC0A9066-17E8-4F80-9437-F9B7B701A27B")
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    quality = str(api[0]["AQI"])
    category = api[0]["Category"]["Name"]

    if category == "Good":
        bg_color = "green"
    elif category == "Moderate":
        bg_color = "yellow"
    elif category == "Unhealthy for Sensitive Groups":
        bg_color = "orange"
    elif category == "Unhealthy":
        bg_color = "red"
    elif category == "Very Unhealthy":
        bg_color = "violet"
    elif category == "Hazardous":
        bg_color = "maroon"

    root.configure(background=bg_color)
    my_label = Label(root, text=f"{city} Air Quality: {quality} {category}", font=("Helvetica", 20), background=bg_color)
    my_label.pack()
except Exception as e:
    api = "Error..."

# zip = Entry(root)
# zip.pack()
# zip_button = Button(root, text="Lookup Zipcode", command=zip_look_up(), background="red")

root.mainloop()


