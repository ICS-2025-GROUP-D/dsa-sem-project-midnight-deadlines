import customtkinter as ctk  # type: ignore
from PIL import Image
from managers.room_manager import RoomManager

room_manager = RoomManager()


def create_room_tabs(root):
    frame = ctk.CTkFrame(root, width=920, height=420)
    frame.place(x=20, y=360)

    ctk.CTkLabel(
        frame, text="My Rooms", font=("Arial", 26), text_color="#FDFEFE"
    ).place(x=20, y=10)
    tabview = ctk.CTkTabview(frame, width=880, height=365, fg_color="transparent")
    tabview.place(x=20, y=40)

    # Get all rooms from the room manager
    rooms = room_manager.get_all_rooms()

    for room in rooms:
        tab = tabview.add(room.name)

        # Room image
        room_img = ctk.CTkImage(
            light_image=Image.open(f"images/{room.image}"), size=(440, 160)
        )
        ctk.CTkLabel(tab, image=room_img, text="").place(x=10, y=0)

        devices = room.get_all_devices()

        for device in devices:
            f = ctk.CTkFrame(tab, width=190, height=145, fg_color="#333333")
            f.place(x=device.position["x"], y=device.position["y"])

            icon = ctk.CTkImage(
                light_image=Image.open(f"images/{device.image}"), size=(80, 80)
            )
            ctk.CTkLabel(f, image=icon, text="").place(x=10, y=10)

            # Device state variable
            state_var = ctk.StringVar(value=device.get_state())

            # Create switch with proper on/off values
            onvalue = "Open" if device.name == "Curtains" else "On"
            offvalue = "Closed" if device.name == "Curtains" else "Off"

            def create_toggle_command(room_name, device_name, state_variable):
                def toggle_command():
                    new_state = room_manager.toggle_room_device(room_name, device_name)
                    if new_state:
                        state_variable.set(new_state)
                        print(f"{room_name} {device_name} toggled to {new_state}")

                return toggle_command

            switch = ctk.CTkSwitch(
                f,
                text="",
                variable=state_var,
                onvalue=onvalue,
                offvalue=offvalue,
                command=create_toggle_command(room.name, device.name, state_var),
            )
            switch.place(x=145, y=10)

            wifi_icon = ctk.CTkImage(
                light_image=Image.open("images/wifi.png"), size=(15, 15)
            )
            plug_icon = ctk.CTkImage(
                light_image=Image.open("images/power-plug.png"), size=(15, 15)
            )

            if device.is_connected:
                ctk.CTkLabel(f, image=wifi_icon, text="").place(x=160, y=40)

            if device.power_source == "plug":
                ctk.CTkLabel(f, image=plug_icon, text="").place(x=160, y=60)

            ctk.CTkLabel(
                f, text=device.name, font=("Arial", 18), text_color="#FDFEFE"
            ).place(x=15, y=98)
            ctk.CTkLabel(
                f, textvariable=state_var, font=("Arial", 12), text_color="#FDFEFE"
            ).place(x=15, y=120)

    return frame


def add_room_to_manager(name, image):
    return room_manager.add_room(name, image)


def remove_room_from_manager(room_name):
    return room_manager.remove_room(room_name)


def get_room_manager():
    return room_manager


def undo_last_device_action(room_name):
    room = room_manager.get_room(room_name)
    if room:
        return room.undo_last_action()
    return None
