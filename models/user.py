#!/usr/bin/python3
"""This module contains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class - inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    CLS_ARGS = ['email', 'password', 'first_name', 'last_name']

    BaseModel(*CLS_ARGS)
