#!/bin/usr/python3
"""Base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        str_dict = json.dumps(list_dictionaries)
        return str_dict

    @classmethod
    def save_to_file(cls, list_objs):
        