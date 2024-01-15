# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square instance"""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

