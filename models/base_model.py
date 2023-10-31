#!/usr/bin/python3
"""
This module contains 01 classes:
    - BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """This class creates an object from scratch
    """

    def __init__(self):
        """Initialize an BaseModel instance
        Args:
            id - a string, id - unique assign
            created_at - datetime assign with the current time of creation
            updated_at - datetime with the current time of updating
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string in this format:
            <class name> (self.id) self.__dict__
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates the updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method retuns a copy of an instance dictionary"""
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
