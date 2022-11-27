#!/usr/bin/python3
"""This module contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    text = ""
    user_id = ""
    place_id = ""
