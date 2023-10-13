#!/bin/usr/python3
"""Base module"""


class Base:
    """This class represent a Base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base Object.
        Args:
            id (int): The ident of The Base
        """
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
