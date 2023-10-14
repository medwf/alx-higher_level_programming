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
        OrdArgs = ['id', 'size', 'x', 'y']

        if args:
            for idx, value in enumerate(args):
                if value == None:
                    self.__init__(self.size, self.x, self.y)
                if value is not None and idx <= 3:
                    setattr(self, OrdArgs[idx], value)
        else:
            for key, value in kwargs.items():
                if value == None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return: a dictionary Representation of a object"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
