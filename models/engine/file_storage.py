#!/usr/bin/python3
"""This module is for a class that serializes and deserializes JSON file"""
import json
from os.path import exists


class FileStorage:
    """class definition"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for k in self.__objects.keys():
            json_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_dict = json.load(file)
                for k in json_dict.keys():
                    self.__objects[k] = BaseModel(**json_dict[k])
        except FileNotFoundError:
            pass
