import customtkinter as ctk
from PIL import Image
from collections import deque

def create_music_player(parent, x=0, y=0):
    frame = ctk.CTkFrame(parent, width=443, height=100, fg_color="#333333")
    frame.place(x=57, y=605)

    music_queue = deque([{"title":"Shape of You", "artist": "Ed Sheeran"},
                   {"title":"Blinding Lights","artist":"The Weeknd"},
                   {"title":"Uptown Funk", "artist": "Bruno Mars"}])
    current_index=[0]

    album_icon = ctk.CTkImage(light_image=Image.open("images/music.png"), size=(70,70))
    ctk.CTkLabel(frame, image=album_icon, text="").place(x=15, y=15)

    current_song=music_queue[0]
    title_var=ctk.StringVar(value=current_song["title"])
    artist_var=ctk.StringVar(value=current_song["artist"])

    title_label=ctk.CTkLabel(frame,textvariable=title_var,font=("Arial",14),text_color='#FDFEFE')
    title_label.place(x=140,y=5)

    artist_label=ctk.CTkLabel(frame,textvariable=artist_var,font=("Arial",12),text_color='#FDFEFE')
    artist_label.place(x=140,y=25)

    progress = ctk.CTkProgressBar(frame, orientation='horizontal')
    progress.set(0.3)
    progress.place(x=140, y=50)

    ctk.CTkLabel(frame, text="1:24", font=("Arial", 12), text_color='#FDFEFE').place(x=140, y=60)

    def update_song():
        song=music_queue[0]
        title_var.set(song["title"])
        artist_var.set(song["artist"])

    def play_previous():
        music_queue.appendleft(music_queue.pop())
        update_song()

    prev_btn=ctk.CTkButton(frame,text="⏮️",width=30,command=play_previous)
    prev_btn.place(x=260,y=60)

    def play_next():
        music_queue.append(music_queue.popleft())
        update_song()

    next_btn=ctk.CTkButton(frame,text="⏭️",width=30,command=play_next)
    next_btn.place(x=310,y=60)

    return frame
