from typing import Optional

class ImageNode:
    def __init__(self, image_path: str, title: str):
        self.image_path: str = image_path
        self.title: str = title
        self.next: Optional["ImageNode"] = None
        self.prev: Optional["ImageNode"] = None
