import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.queue import Queue

class MusicManager:
    """Manages music queue and playback using Queue data structure."""

    def __init__(self):
        self.music_queue = Queue()
        self.current_index = 0
        self.is_playing = False
        self.progress = 0.0
        self.current_time = "0:00"
        self._initialize_default_songs()

    def _initialize_default_songs(self):
        """Initialize with default songs."""
        default_songs = [
            {"title": "Shape of You", "artist": "Ed Sheeran", "duration": "3:45"},
            {"title": "Blinding Lights", "artist": "The Weeknd", "duration": "3:20"},
            {"title": "Uptown Funk", "artist": "Bruno Mars", "duration": "4:30"},
            {"title": "Perfect", "artist": "Ed Sheeran", "duration": "4:23"},
            {"title": "Starboy", "artist": "The Weeknd", "duration": "3:50"},
        ]

        for song in default_songs:
            self.music_queue.enqueue(song)

    def add_song(self, title, artist, duration="3:00"):
        song = {"title": title, "artist": artist, "duration": duration}
        self.music_queue.enqueue(song)

    def get_current_song(self):
        if self.music_queue.is_empty():
            return None
        return self.music_queue.get_item_at(self.current_index)

    def next_song(self):
        if not self.music_queue.is_empty():
            self.current_index = (self.current_index + 1) % self.music_queue.size()
            self.progress = 0.0
            self.current_time = "0:00"
            return self.get_current_song()
        return None

    def previous_song(self):
        if not self.music_queue.is_empty():
            self.current_index = (self.current_index - 1) % self.music_queue.size()
            self.progress = 0.0
            self.current_time = "0:00"
            return self.get_current_song()
        return None

    def play_pause(self):
        self.is_playing = not self.is_playing
        return self.is_playing

    def set_progress(self, progress):
        self.progress = max(0.0, min(1.0, progress))

    def get_progress(self):
        return self.progress

    def set_current_time(self, time_str):
        self.current_time = time_str

    def get_current_time(self):
        return self.current_time

    def get_queue_size(self):
        return self.music_queue.size()

    def get_all_songs(self):
        return self.music_queue.get_all()

    def clear_queue(self):
        self.music_queue = Queue()
        self.current_index = 0
        self.progress = 0.0
        self.current_time = "0:00"

    def shuffle_queue(self):
        import random

        songs = self.music_queue.get_all()
        random.shuffle(songs)
        self.music_queue = Queue()
        for song in songs:
            self.music_queue.enqueue(song)
        self.current_index = 0
