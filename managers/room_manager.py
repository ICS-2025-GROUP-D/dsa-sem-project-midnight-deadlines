import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.linked_list import LinkedList
from utils.stack import Stack

class Device:
    """Represents a smart home device."""

    def __init__(self, name, image, position, default_state="On"):
        self.name = name
        self.image = image
        self.position = position  # {"x": int, "y": int}
        self.state = default_state
        self.is_connected = True
        self.power_source = "plug"  

    def toggle_state(self):
        """Toggle device state."""
        if self.name == "Curtains":
            self.state = "Closed" if self.state == "Open" else "Open"
        else:
            self.state = "Off" if self.state == "On" else "On"
        return self.state

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_connection_status(self, connected):
        self.is_connected = connected

    def __str__(self):
        return f"Device({self.name}, {self.state}, Connected: {self.is_connected})"


class Room:
    """Represents a room with devices."""

    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.devices = LinkedList()
        self.device_actions = Stack()  # For undo functionality
        self._initialize_default_devices()

    def _initialize_default_devices(self):
        """Initialize room with default devices."""
        default_devices = [
            Device("Lights", "lights.png", {"x": 470, "y": 0}, "On"),
            Device("Speakers", "speaker.png", {"x": 670, "y": 0}, "On"),
            Device("Curtains", "curtains.png", {"x": 470, "y": 155}, "Open"),
            Device("Humidifier", "humidifier.png", {"x": 670, "y": 155}, "On"),
        ]

        for device in default_devices:
            self.devices.append(device)

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_name):
        devices_list = self.devices.to_list()
        for i, device in enumerate(devices_list):
            if device.name == device_name:
                # Rebuild the linked list without the device
                new_devices = LinkedList()
                for j, d in enumerate(devices_list):
                    if j != i:
                        new_devices.append(d)
                self.devices = new_devices
                return True
        return False

    def get_device(self, device_name):
        current = self.devices.head
        while current:
            if current.data.name == device_name:
                return current.data
            current = current.next
        return None

    def get_all_devices(self):
        return self.devices.to_list()

    def toggle_device(self, device_name):
        device = self.get_device(device_name)
        if device:
            old_state = device.get_state()
            new_state = device.toggle_state()

            # Record action for undo
            action = {
                "device_name": device_name,
                "old_state": old_state,
                "new_state": new_state,
                "action": "toggle",
            }
            self.device_actions.push(action)

            return new_state
        return None

    def undo_last_action(self):
        if not self.device_actions.is_empty():
            action = self.device_actions.pop()
            device = self.get_device(action["device_name"])
            if device:
                device.set_state(action["old_state"])
                return action
        return None

    def get_device_count(self):
        return self.devices.size()

    def __str__(self):
        return f"Room({self.name}, {self.get_device_count()} devices)"


class RoomManager:
    """Manages all rooms in the smart home."""

    def __init__(self):
        self.rooms = LinkedList()
        self._initialize_default_rooms()

    def _initialize_default_rooms(self):
        """Initialize with default rooms."""
        default_rooms = [
            {"name": "Living Room", "image": "living-room.jpg"},
            {"name": "Dining Room", "image": "dining-room.jpg"},
            {"name": "Bed Room 1", "image": "bed-room1.jpg"},
            {"name": "Bed Room 2", "image": "bed-room2.jpg"},
            {"name": "Garage", "image": "garage.jpg"},
        ]

        for room_data in default_rooms:
            room = Room(room_data["name"], room_data["image"])
            self.rooms.append(room)

    def add_room(self, name, image):
        room = Room(name, image)
        self.rooms.append(room)
        return room

    def remove_room(self, room_name):
        rooms_list = self.rooms.to_list()
        for i, room in enumerate(rooms_list):
            if room.name == room_name:
                # Rebuild the linked list without the room
                new_rooms = LinkedList()
                for j, r in enumerate(rooms_list):
                    if j != i:
                        new_rooms.append(r)
                self.rooms = new_rooms
                return True
        return False

    def get_room(self, room_name):
        current = self.rooms.head
        while current:
            if current.data.name == room_name:
                return current.data
            current = current.next
        return None

    def get_all_rooms(self):
        return self.rooms.to_list()

    def toggle_room_device(self, room_name, device_name):
        room = self.get_room(room_name)
        if room:
            return room.toggle_device(device_name)
        return None

    def get_room_count(self):
        return self.rooms.size()

    def get_total_device_count(self):
        """Get the total number of devices across all rooms."""
        total = 0
        current = self.rooms.head
        while current:
            total += current.data.get_device_count()
            current = current.next
        return total
