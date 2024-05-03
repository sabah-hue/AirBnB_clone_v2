#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float, ForeignKey, Table
from models.amenity import Amenity
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    reviews = relationship('Review', cascade='all,delete', backref='place')
    amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='places', viewonly=False)

    @property
    def reviews(self):
        """FileStorage relationship between State and City"""
        from models import storage
        list_review = []
        for key, value in storage.all(Review).items():
            if value.place_id == self.id:
                list_review.append(value)
        return list_review

    @property
    def amenities(self):
        """Getter attribute amenities"""
        list_amenty = []
        for key, value in storage.all(Amenity).items():
            if value.id in self.amenity_ids:
                list_amenty.append(value)
        return list_amenty

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute amenities"""
        if (type(obj) == Amenity):
            self.amenity_ids.append(obj.id)
