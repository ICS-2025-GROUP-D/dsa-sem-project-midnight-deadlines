import customtkinter as ctk
from PIL import Image
from utils.events import handle_camera_switch

def create_camera_section(root):
    frame = ctk.CTkFrame(root, width=450, height=280)
    frame.place(x=20, y=60)

    cctv_label = ctk.CTkLabel(frame, text="CCTV Camera", font=("Arial", 11), text_color='#FDFEFE')
    cctv_label.place(x=10, y=5)

    camera_switch_var = ctk.StringVar(value="on")
    switch = ctk.CTkSwitch(
        frame, text="", 
        command=lambda: handle_camera_switch(camera_switch_var.get()),
        variable=camera_switch_var, onvalue="on", offvalue="off"
    )
    switch.place(x=400, y=20)

    front_door_label = ctk.CTkLabel(frame, text="Front Door", font=("Arial", 16), text_color='#FDFEFE')
    front_door_label.place(x=10, y=24)

    image = ctk.CTkImage(light_image=Image.open("images/security.jpg"), size=(430, 210))
    img_label = ctk.CTkLabel(frame, image=image, text="", compound='center')
    img_label.place(x=10, y=55)