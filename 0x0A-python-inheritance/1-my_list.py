#!/usr/bin/python3
"""
Mylist is a class inherits_ list
"""


class MyList(list):
    """subclass of list"""

    def __init__(self):
        """initisalizes the object"""
        super().__init__()

    def print_sorted(self):
        """public methods print sorted list"""
        print(sorted(self))
