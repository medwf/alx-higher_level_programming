#!/usr/bin/python3
"""
This module contains a class that defines a rectangle.
"""


class BaseGeometry:
    """Defines a BaseGeometry"""

    def area(self):
        """Method: raises an Exception with the message
            area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validation value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
