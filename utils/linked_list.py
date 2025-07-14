class Node:
    """A node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A simple linked list implementation."""

    def __init__(self):
        self.head = None
        self.size_count = 0

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size_count += 1

    def prepend(self, data):
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size_count += 1

    def delete(self, data):
        """Delete the first node with the given data."""
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size_count -= 1
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size_count -= 1
                return True
            current = current.next
        return False

    def find(self, data):
        """Find and return the first node with the given data."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def get_at_index(self, index):
        """Get the data at the specified index."""
        if index < 0 or index >= self.size_count:
            raise IndexError("Index out of range")

        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def size(self):
        """Return the number of nodes in the list."""
        return self.size_count

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return f"LinkedList({self.to_list()})"
