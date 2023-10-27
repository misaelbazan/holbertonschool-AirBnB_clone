#!/usr/bin/python3
"""
This module contains 01 Classes:
    1. BaseModel
"""


from uuid import uuid4
from datetime import datetime, timezone


class BaseModel:
    """
    This class is meant to inherit to the following classes:
        -
        -
    This class contains:
        Public instance attributes:
        - id: string - assign with an uuid when an instance is created
            + The goal is to have unique 'id' for each BaseModel
        - created_at: datetime - assign with the current datetime when an \
                instance is created
        - updated_at: datetime - assign with the current datetime when an \
                instance is created and it will be updated e/t
        Methods:
        - __str__: should print '[<class name>] (<self.id>) <self.__dict__>'
        Public instance methods:
        - save(self): updates the public instance attribute updated_at
                current datetime
        - to_dict(self): returns a dictionary containing all keys/values of \
                __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance from BaseModel Class
        Variables:
        - id: string - assign with an uuid when an instance is created:
        - created_at: datetime - assign with the current datetime when a
         instance is created
        - updated_at: datetime - assign with the current datetime when an
        instance is created and it will be updated e/t you change your object
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns [class name] (self.id) self.__dict__"""
        return(f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at attribute with the current d/t
        """
        if hasattr(self, "updated_at"):
            self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ \
                of the instance"""
        if hasattr(self, "created_at"):
            self.created_at = self.created_at.isoformat()
        if hasattr(self, "updated_at"):
            self.updated_at = self.updated_at.isoformat()
        if hasattr(self, "__class__"):
            self.__dict__["__class__"] = self.__class__.__name__
        return(self.__dict__)
