import customtkinter as ctk
from PIL import Image
from managers.music_manager import MusicManager

music_manager = MusicManager()


def create_music_player(parent, x=0, y=0):
    frame = ctk.CTkFrame(parent, width=443, height=100, fg_color="#333333")
    frame.place(x=57, y=600)

    # Album icon
    album_icon = ctk.CTkImage(light_image=Image.open("images/music.png"), size=(70, 70))
    ctk.CTkLabel(frame, image=album_icon, text="").place(x=15, y=15)

    # Get current song from manager
    current_song = music_manager.get_current_song()

    title_var = ctk.StringVar(
        value=current_song["title"] if current_song else "No Song"
    )
    artist_var = ctk.StringVar(
        value=current_song["artist"] if current_song else "No Artist"
    )

    title_label = ctk.CTkLabel(
        frame, textvariable=title_var, font=("Arial", 14), text_color="#FDFEFE"
    )
    title_label.place(x=140, y=5)

    artist_label = ctk.CTkLabel(
        frame, textvariable=artist_var, font=("Arial", 12), text_color="#FDFEFE"
    )
    artist_label.place(x=140, y=25)

    # Progress bar
    progress = ctk.CTkProgressBar(frame, orientation="horizontal")
    progress.set(music_manager.get_progress())
    progress.place(x=140, y=50)

    # Time label
    time_label = ctk.CTkLabel(
        frame,
        text=music_manager.get_current_time(),
        font=("Arial", 12),
        text_color="#FDFEFE",
    )
    time_label.place(x=140, y=60)

    def update_display():
        """Update the display with current song info."""
        song = music_manager.get_current_song()
        if song:
            title_var.set(song["title"])
            artist_var.set(song["artist"])
            progress.set(music_manager.get_progress())
            time_label.configure(text=music_manager.get_current_time())

    def play_previous():
        """Play the previous song."""
        music_manager.previous_song()
        update_display()

    def play_next():
        """Play the next song."""
        music_manager.next_song()
        update_display()

    def toggle_play_pause():
        """Toggle play/pause state."""
        is_playing = music_manager.play_pause()
        play_pause_btn.configure(text="⏸️" if is_playing else "▶️")

    # Control buttons
    prev_btn = ctk.CTkButton(frame, text="⏮️", width=30, command=play_previous)
    prev_btn.place(x=250, y=70)

    play_pause_btn = ctk.CTkButton(frame, text="▶️", width=30, command=toggle_play_pause)
    play_pause_btn.place(x=290, y=70)

    next_btn = ctk.CTkButton(frame, text="⏭️", width=30, command=play_next)
    next_btn.place(x=330, y=70)

    # Volume control (optional)
    volume_label = ctk.CTkLabel(
        frame, text="🔊", font=("Arial", 12), text_color="#FDFEFE"
    )
    volume_label.place(x=370, y=70)

    return frame


def add_song_to_queue(title, artist, duration="3:00"):
    music_manager.add_song(title, artist, duration)


def get_music_manager():
    return music_manager


def shuffle_music_queue():
    music_manager.shuffle_queue()


def clear_music_queue():
    music_manager.clear_queue()


def get_queue_info():
    """Get information about the current queue."""
    return {
        "current_song": music_manager.get_current_song(),
        "queue_size": music_manager.get_queue_size(),
        "all_songs": music_manager.get_all_songs(),
        "is_playing": music_manager.is_playing,
    }
