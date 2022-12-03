#!/usr/bin/python3
"""This module is for a class that serializes and deserializes JSON file"""
import json
from os.path import exists
from models.base_model import BaseModel


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
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dct_json = json.dumps(json_dict)
            f.write(dct_json)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                str_obj = f.read()
                json_dict = json.loads(str_obj)
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
