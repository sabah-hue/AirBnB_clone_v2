#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float, ForeignKey, Table, DateTime
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from datetime import datetime


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', ondelete='CASCADE'),
                             onupdate='CASCADE', primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', ondelete='CASCADE'),
                             onupdate='CASCADE', primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
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
    amenities = relationship('Amenity', backref='place_amenities',
                             cascade='all, delete',
                             secondary=place_amenity,
                             viewonly=False,
                             passive_deletes=True)


    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """FileStorage relationship between State and City"""
        from models import storage
        list_review = []
        for key, value in models.storage.all(Review).items():
            if value.place_id == self.id:
                list_review.append(value)
        return list_review

    @property
    def amenities(self):
        """Getter attribute amenities"""
        list_amenty = []
        for amenity in models.storage.all(Amenity).values():
            # if amenity.place_id == self.id:
                list_amenty.append(amenity)
        return list_amenty


    @amenities.setter
    def amenities(self, obj):
        """Setter attribute amenities"""
        if not isinstance(obj, Amenity):
            return
        self.amenity_ids.append(obj.id)
