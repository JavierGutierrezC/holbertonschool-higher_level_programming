#!/usr/bin/python3
"""module base.py"""
import json


class Base:
    """class base"""
    __nb_object = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Pass a string from python to json"""
        if list_dictionaries is None or list_dictionaries is "":
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save as json file"""
        list2 = []
        if list_objs is not None:
            for i in list_objs:
                list2.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as New_file:
            New_file.write(cls.to_json_string(list2))

    @staticmethod
    def from_json_string(json_string):
        """from json to python"""
        if json_string is None or json_string is "":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """temporal dummy creation"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)
