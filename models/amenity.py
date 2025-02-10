#!/usr/bin/python
"""This module defines a Amenity class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'
    
    if models.storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

