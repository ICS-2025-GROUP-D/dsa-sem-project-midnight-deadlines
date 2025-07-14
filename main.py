# Step 1: Create a virtual environment
# python3 -m venv venv

# Step 2: Activate it
# source venv/bin/activate

# Step 3: Install requirements
# pip install -r requirements.txt

# Step 4: Launch Dashboard
# python3 main.py

# Step 5: To deactivate
# deactivate

import customtkinter as ctk # type: ignore
import sqlite3
from widgets.room_tabs import create_room_tabs
from utils.helpers import get_current_time
from widgets.device_section import create_device_controls
from widgets.camera_section import create_camera_section
from widgets.music_player import create_music_player
from widgets.air_conditioner_section import create_air_conditioner_section
from widgets.weather_section import create_weather_section
 
class SmartHomeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Home Dashboard")
        self.geometry("1200x650")
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy())

        # Title Label
        self.name_var = ctk.StringVar(value="Hello")
        self.setup_database()
        self.load_saved_name()
        self.title_label = ctk.CTkLabel(self, textvariable=self.name_var, font=("Arial", 24))
        self.title_label.place(x=20, y=20)


        # Title Label ( Displays the current title )
        # --- Dropdown & Entry ---
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter name", width=200)
        self.name_entry.place(x=200, y=20)

        self.user_dropdown = ctk.CTkOptionMenu(self, values=[], command=self.on_user_select)
        self.user_dropdown.place(x=410, y=20)

        self.add_button = ctk.CTkButton(self, text="Add", command=self.add_user, width=60)
        self.add_button.place(x=590, y=20)

        self.update_button = ctk.CTkButton(self, text="Update", command=self.update_user, width=60)
        self.update_button.place(x=660, y=20)

        self.delete_button = ctk.CTkButton(self, text="Delete", command=self.delete_user, width=60)
        self.delete_button.place(x=730, y=20)
        
        self.load_users()


        

    def setup_database(self):
     self.conn = sqlite3.connect("users.db")
     self.cursor = self.conn.cursor()
     self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
     self.conn.commit()
    def load_users(self):
     self.cursor.execute("SELECT name FROM user")
     users = [row[0] for row in self.cursor.fetchall()]
     self.user_dropdown.configure(values=users if users else ["No users"])
     if users:
        self.user_dropdown.set(users[0])
        self.name_var.set(f"Hello {users[0]}")
     else:
        self.user_dropdown.set("No users")
        self.name_var.set("Hello")

    def on_user_select(self, selected_name):
     self.name_var.set(f"Hello {selected_name}")
     self.name_entry.delete(0, "end")
     self.name_entry.insert(0, selected_name)

    def add_user(self):
     name = self.name_entry.get().strip()
     if not name:
        return
     self.cursor.execute("SELECT COUNT(*) FROM user")
     count = self.cursor.fetchone()[0]
     if count >= 5:
        print("Maximum of 3 users allowed.")
        return
     self.cursor.execute("INSERT INTO user (name) VALUES (?)", (name,))
     self.conn.commit()
     self.name_entry.delete(0, "end")
     self.load_users()
     

    def update_user(self):
     selected = self.user_dropdown.get()
     new_name = self.name_entry.get().strip()
     if selected and new_name:
        self.cursor.execute("UPDATE user SET name = ? WHERE name = ?", (new_name, selected))
        self.conn.commit()
        self.name_entry.delete(0, "end")
        self.load_users()

    def delete_user(self):
     selected = self.user_dropdown.get()
     if selected and selected != "No users":
        self.cursor.execute("DELETE FROM user WHERE name = ?", (selected,))
        self.conn.commit()
        self.load_users()

     
    def load_saved_name(self):
     self.cursor.execute("SELECT name FROM user ORDER BY id DESC LIMIT 1")
     row = self.cursor.fetchone()
     if row:
        self.name_var.set(f"Hello {row[0]}") 
        
        create_room_tabs(self)
        create_device_controls(self)
        create_camera_section(self)
        create_music_player(self)
        create_air_conditioner_section(self)
        create_weather_section(self)

if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
    