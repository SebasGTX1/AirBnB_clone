#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE'):
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secundary=place_amenity)
    else:
        name = ""