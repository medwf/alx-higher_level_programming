#!/usr/bin/python3
""" This is Class squere """


class Square:
    """  This class allows you to create and manipulate square objects """

    def __init__(self, size=0):
        """ Initialize a new Square
            args:
                size (int): The size for new Saquare
            size should be an integer and greate than -1
        """
        self._Square__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if self._Square__size < 0:
            raise ValueError('size must be >= 0')
