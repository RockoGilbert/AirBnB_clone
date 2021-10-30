#!/usr/bin/python3
"""Serializes instances to JSON and deserialized JSON files to instances"""


import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import state 
from models.user import User

class FileStorage:
    """Serializes instances to JSON file"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns object attribute"""     
        return FileStorage.__objects
    
    def new(self, obj):
        """Set __object as value and obj class name + .id as key"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj
        
    def save(self):
        """Serializes objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
                json.dump(d, f)
       
        
            
    def reload(self):
        """Loads objects from a JSON file"""
        
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass