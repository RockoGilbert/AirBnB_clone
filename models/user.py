#!/usr/bin/python3
"""User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines a User and inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""