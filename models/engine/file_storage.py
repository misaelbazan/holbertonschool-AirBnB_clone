#!/usr/bin/python3
"""
This module defines the FileStorage class
"""

import json
from os import path


class FileStorage:
    """This class serializes instances to a JSON file and deserealizes
    JSON file to instances
    Attributes:
        __file_path (str) - path to the JSON file
        __objects (dict) - stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}  # Initializes as an empty dictionary, content will be added

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __object the <obj> with the key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects dictionary to the JSON file"""
        new_dict = {}

        for k, obj in FileStorage.__objects.items():
            new_dict[k] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserealizes the JSON file to __objects (only if the JSON file
        exists, otherwise do nothing
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as json_file:
                objs = json.load(json_file)
            for k, v in objs.items():
                from models.base_model import BaseModel
                bs = BaseModel(**v)
                FileStorage.__objects[k] = bs
