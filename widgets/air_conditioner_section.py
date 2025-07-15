import customtkinter as ctk
from PIL import Image
from utils.events import handle_air_conditioner_switch

def create_air_conditioner_section(root):
    frame = ctk.CTkFrame(root, width=450, height=490)
    frame.place(x=960, y=60)

    ctk.CTkLabel(frame, text="Air Conditioner", font=("Arial", 24), text_color='#FDFEFE').place(x=20, y=20)
    ctk.CTkLabel(frame, text="Living room", font=("Arial", 14), text_color='#FDFEFE').place(x=20, y=45)

    switch_var = ctk.StringVar(value="On")
    ctk.CTkSwitch(
        frame, text="", variable=switch_var,
        onvalue="On", offvalue="Off",
        switch_height=20, switch_width=40,
        command=lambda: handle_air_conditioner_switch(switch_var.get())
    ).place(x=390, y=20)

    snow_icon = ctk.CTkImage(light_image=Image.open("images/snowflake.png"), size=(200, 200))
    ctk.CTkLabel(frame, image=snow_icon, text="").place(x=120, y=100)

    ctk.CTkLabel(frame, text="Cooling To ", font=("Arial", 24), text_color='#FDFEFE').place(x=160, y=345)

    temp_value = ctk.IntVar(value=20)
    cooling_label = ctk.CTkLabel(frame, text=f"{temp_value.get()}°c", font=("Arial", 32), text_color='#FDFEFE')
    cooling_label.place(x=185, y=400)

    def increase_temp():
        if temp_value.get() < 40:
            temp_value.set(temp_value.get() + 1)
            cooling_label.configure(text=f"{temp_value.get()}°C")

    def decrease_temp():
        if temp_value.get() > 16:
            temp_value.set(temp_value.get() - 1)
            cooling_label.configure(text=f"{temp_value.get()}°C")

    plus_icon = ctk.CTkImage(light_image=Image.open("images/add.png"), size=(60, 60))
    minus_icon = ctk.CTkImage(light_image=Image.open("images/minus.png"), size=(60, 60))

    ctk.CTkButton(frame, image=plus_icon, text="", fg_color='transparent', width=40, height=40, command=increase_temp).place(x=260, y=400)
    ctk.CTkButton(frame, image=minus_icon, text="", fg_color='transparent', width=40, height=40, command=decrease_temp).place(x=80, y=400)