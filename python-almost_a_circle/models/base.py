#!/usr/bin/python3
"""The first class"""
import json


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dict_list)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        list_objs = []
        if not json_string or len(json_string) == 0:
            return list_objs
        return json.loads(json_string)
