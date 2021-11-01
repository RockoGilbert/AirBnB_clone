#!/usr/bin/python3
"""The base class for models"""

import models
import uuid
from datetime import datetime


class BaseModel():
    """Base model from which future instances are derived"""

    def __init__(self, *args, **kwargs):
        """Initializing the base model"""

        if kwargs:
            for key, value in kwargs.items():

                if key == "created at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel Class"""

        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Method to return the dictionary representation of the object."""

        x_dict = self.__dict__.copy()
        x_dict["__class__"] = self.__class__.__name__
        x_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        x_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return x_dict
