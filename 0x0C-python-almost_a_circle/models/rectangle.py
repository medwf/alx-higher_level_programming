#!/usr/bin/python3
"""import Base from models.base."""
from models.base import Base

"""module Rectangle """


class Rectangle(Base):
    """This class represent Rectangle module
            that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle Object.
        Args:
            width (int) : The width of The Rectangle
            height (int) : The height of The Rectangle
            x (int) : The x of The Rectangle
            y (int) : The y of The Rectangle
            id (int) : The id of The Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieve The width of Rectangle.
        Return: an integer of the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set new width for Rectangle

            Args:
                value (int): The new width for new Rectangle

            Raises:
                TypeError: width must be an integer
                ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieve The height of Rectangle.
        Return: an integer of the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set new height for Rectangle

            Args:
                value (int): The new height for new Rectangle

            Raises:
                TypeError: height must be an integer
                ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrieve The x of Rectangle.
        Return: an integer of the x."""
        return self.__x

    @x.setter
    def x(self, value):
        """ Set new x for Rectangle

            Args:
                value (int): The new x for new Rectangle

            Raises:
                TypeError: x must be an integer
                ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieve The x of Rectangle.
        Return: an integer of the y."""
        return self.__y

    @y.setter
    def y(self, value):
        """ Set new y for Rectangle

            Args:
                value (int): The new y for new Rectangle

            Raises:
                TypeError: y must be an integer
                ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """area : public method.
            Return: The Area value of The Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """display: public method
            print in stdout The Rectangle instance with
            the charcters #.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return string."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign value to attribute using *args"""
        OrdArgs = ['id', 'width', 'height', 'x', 'y']

        if args:
            for idx, value in enumerate(args):
                if idx is 0 and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                if value is not None and idx <= 4:
                    setattr(self, OrdArgs[idx], value)
        else:
            for key, value in kwargs.items():
                if value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return: a dictionary Representation of a object"""
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
