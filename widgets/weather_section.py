import customtkinter as ctk
from PIL import Image
from datetime import datetime
from utils.helpers import get_user_location

def create_weather_section(root):
    weather_type = "Sunny"

    if weather_type == "Sunny":
        bg_color = "#FFD580"
    elif weather_type == "Rainy:
        bg_color = "#6C7A89"
    elif weather_type == "Cloudy":
        bg_color = "#B0BEC5"
    else:
        bg_color = "#2C3E50"

    frame = ctk.CTkFrame(root, width=450, height=130)
    frame.place(x=490, y=60)

    cloud_icon = ctk.CTkImage(light_image=Image.open("images/cloudy.png"), size=(200, 126))
    cloud_icon_label = ctk.CTkLabel(frame, image=cloud_icon, text="", compound='center')
    cloud_icon_label.place(x=20, y=10)

    location_icon = ctk.CTkImage(light_image=Image.open("images/location.png"), size=(25, 25))
    location_icon_label = ctk.CTkLabel(frame, image=location_icon, text="", compound='center')
    location_icon_label.place(x=320, y=10)

    city_label = ctk.CTkLabel(frame, text=get_user_location(), font=("Arial", 20), text_color='#FDFEFE')
    city_label.place(x=350, y=10)

    temperature_label = ctk.CTkLabel(frame, text="12°c", font=("Arial", 32), text_color='#FDFEFE')
    temperature_label.place(x=320, y=50)

    temp_desc_label = ctk.CTkLabel(frame, text="Outside temperature", font=("Arial", 17), text_color='#FDFEFE')
    temp_desc_label.place(x=260, y=90)

    weather_desc_label = ctk.CTkLabel(frame, text="Cloudy", font=("Arial",18), text_color='#FDFEFE')
    weather_desc_label.place(x=320, y=90)

    date_label = ctk.CTkLabel(frame, text=datetime.now().strftime("%A, %B %d"), font=("Arial", 15), text_color='#FDFEFE')
    date_label.place(x=20, y=100)

def refresh_weather():
    city_label.configure(text=get_user_location())
    
refresh_btn = ctk.CTkButton(frame, text="🔃", width=30, height=30, command=refresh_weather)
refresh_btn.place(x=410, y=10)    