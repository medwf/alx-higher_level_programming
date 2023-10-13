#!/usr/bin/python3
from models.rectangle import Rectangle

"""module Square"""


class Square(Rectangle):
    """This class represent Square module
        that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize new Square Object
        Args:
            size (int) : The width of The Square
            x (int) : The x of The Square
            y (int) : The y of The Square
            id (int) : The id of The Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return interger size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """set value to The size of Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """return string"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign value to attribute using *args"""

        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
                super().__init__(self.id)
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
                super().__init__(self.id)
            if key == 'size':
                self.width = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
