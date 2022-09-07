#!/usr/bin/python3
""" Place Module for HBNB project """
from importlib.metadata import metadata
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models.city import City
from models.user import User
import models
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'),
                             nullable=False, primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secundary=place_amenity, viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        if getenv('HBNB_TYPE_STORAGE') != 'db':

            @property
            def reviews(self):
                """Reviewis
                """
                my_dict = models.storage.all('Review')
                my_list = []
                for review in my_dict.values():
                    if review.place_id == self.id:
                        my_list.append(review)

                return my_list

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on the
            attribute amenity_ids
            """
            my_dict = models.storage.all('Amenity')
            for amenity in my_dict.values():
                if amenity.place_id == self.id:
                    amenities_ids.append(amenity)
            return self.amenities_ids

        @amenities.setter
        def amenities(self, obj=None):
            """
            handles append method for adding an Amenity.id to the
            attribute amenity_ids
            """
            if type(obj) == 'Amenity':
                self.amenities_ids.append(obj.id)