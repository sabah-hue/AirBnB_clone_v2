#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', secondary='place_amenity')

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
