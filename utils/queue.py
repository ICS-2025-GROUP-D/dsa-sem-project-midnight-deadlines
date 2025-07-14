class Queue:
    """A simple queue implementation for managing ordered collections."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def rear(self):
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def get_all(self):
        """Return all items in the queue."""
        return self.items.copy()

    def get_item_at(self, index):
        """Get item at specific index."""
        if 0 <= index < len(self.items):
            return self.items[index]
        raise IndexError("Index out of range")

    def __str__(self):
        return f"Queue({self.items})"
