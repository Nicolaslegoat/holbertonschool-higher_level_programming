#!/usr/bin/python3
"""
This module defines the rectangle and square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        That retrieves the size of the square sides
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Method to defines the size of the square sides
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        That return a representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionnary(self):
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
