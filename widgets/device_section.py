import customtkinter as ctk
from PIL import Image
from utils.events import handle_wifi_switch, handle_tv_switch, handle_thermostat_switch

def create_device_controls(root):
    # WiFi
    wifi_frame = ctk.CTkFrame(root, width=140, height=130)
    wifi_frame.place(x=490, y=210)

    wifi_switch_var = ctk.StringVar(value="On")
    wifi_switch = ctk.CTkSwitch(wifi_frame, text="", command=lambda: handle_wifi_switch(wifi_switch_var.get()),
                                variable=wifi_switch_var, onvalue="On", offvalue="Off")
    wifi_switch.place(x=95, y=6)

    ctk.CTkLabel(wifi_frame, textvariable=wifi_switch_var, font=("Arial", 17), text_color='#FDFEFE').place(x=10, y=6)
    ctk.CTkLabel(wifi_frame, image=ctk.CTkImage(light_image=Image.open("images/wifi.png"), size=(40, 40)), text="").place(x=52, y=40)
    ctk.CTkLabel(wifi_frame, text="Home Wifi", font=("Arial", 12), text_color='#FDFEFE').place(x=48, y=83)
    ctk.CTkLabel(wifi_frame, text="Connected", font=("Arial", 10), text_color='#FDFEFE').place(x=46, y=105)

    # TV
    tv_frame = ctk.CTkFrame(root, width=140, height=130)
    tv_frame.place(x=645, y=210)

    tv_switch_var = ctk.StringVar(value="On")
    tv_switch = ctk.CTkSwitch(tv_frame, text="", command=lambda: handle_tv_switch(tv_switch_var.get()),
                              variable=tv_switch_var, onvalue="On", offvalue="Off")
    tv_switch.place(x=95, y=6)

    ctk.CTkLabel(tv_frame, textvariable=tv_switch_var, font=("Arial", 17), text_color='#FDFEFE').place(x=10, y=6)
    ctk.CTkLabel(tv_frame, image=ctk.CTkImage(light_image=Image.open("images/tv.png"), size=(40, 40)), text="").place(x=52, y=40)
    ctk.CTkLabel(tv_frame, text="Benq Tv", font=("Arial", 12), text_color='#FDFEFE').place(x=48, y=83)
    ctk.CTkLabel(tv_frame, text="Connected", font=("Arial", 10), text_color='#FDFEFE').place(x=46, y=105)

    # Thermostat
    thermostat_frame = ctk.CTkFrame(root, width=140, height=130)
    thermostat_frame.place(x=800, y=210)

    thermostat_switch_var = ctk.StringVar(value="On")
    thermostat_switch = ctk.CTkSwitch(thermostat_frame, text="", command=lambda: handle_thermostat_switch(thermostat_switch_var.get()),
                                      variable=thermostat_switch_var, onvalue="On", offvalue="Off")
    thermostat_switch.place(x=95, y=6)

    ctk.CTkLabel(thermostat_frame, textvariable=thermostat_switch_var, font=("Arial", 17), text_color='#FDFEFE').place(x=10, y=6)
    ctk.CTkLabel(thermostat_frame, image=ctk.CTkImage(light_image=Image.open("images/thermostat.png"), size=(40, 40)), text="").place(x=52, y=40)
    ctk.CTkLabel(thermostat_frame, text="Thermostat", font=("Arial", 12), text_color='#FDFEFE').place(x=40, y=83)
    ctk.CTkLabel(thermostat_frame, text="Connected", font=("Arial", 10), text_color='#FDFEFE').place(x=42, y=105)
