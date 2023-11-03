#!/usr/bin/python3
"""
This module contains 01 classes:
    - BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This class creates an object from scratch
    """

    def __init__(self, *args, **kwargs):
        """Initialize an BaseModel instance
        Args:
            *args: Any positional arguments.
            **kwargs: Any keyword arguments.
            id - a string, id - unique assign
            created_at - datetime assign with the current time of creation
            updated_at - datetime with the current time of updating
        """
        if bool(kwargs):
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string in this format:
            BaseModel (uuid4 type id) self.__dict__
        """
        return f"[{self.__class__.__name__}] ({self.id}) "\
                + str({k: v for k, v in self.__dict__.items() if k != '__class__'})

    def save(self):
        """This method updates the updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method retuns a copy of an instance dictionary"""
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
