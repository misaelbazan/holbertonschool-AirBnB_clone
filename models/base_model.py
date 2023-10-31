#!/usr/bin/python3
<<<<<<< HEAD
"""
This module contains 01 classes:
    - BaseModel
"""

=======
>>>>>>> 6be8c6837f202a864134846e096d8eae4907dc31

import uuid
from datetime import datetime

<<<<<<< HEAD

=======
>>>>>>> 6be8c6837f202a864134846e096d8eae4907dc31
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
<<<<<<< HEAD
        """Returns a string in this format:
            <class name> (self.id) self.__dict__
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates the updated_at """ 
        self.updated_at = datetime.now()

=======
        class_name = self.__class__.__name
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
            
>>>>>>> 6be8c6837f202a864134846e096d8eae4907dc31
    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
<<<<<<< HEAD
        instance_dict['__class__'] = self.__class__.__name__
=======
        instance_dict['__class__'] = self.__class__.__name
>>>>>>> 6be8c6837f202a864134846e096d8eae4907dc31
        return instance_dict
