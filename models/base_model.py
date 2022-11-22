#!/usr/bin/python3
"""
BaseModel class that defines all common
attributes/methods for other classes
"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if len(kwargs) > 0:
            for k in kwargs.keys():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k, datetime.fromisoformat(kwargs[k]))
                    else:
                        setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """prints representation of instance"""
        print("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dictionary = self.__dict__
        update = self.updated_at.isoformat()
        create = self.created_at.isoformat()
        dictionary.pop("created_at")
        dictionary.pop("updated_at")
        cls_dict = {"__class__": self.__class__, "updated_at": update,
                    "created_at": create}
        dictionary.update(cls_dict)
        return dictionary
