#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # for DBStorage
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
    # for FileStorage

    @property
    def cities(self):
        """FileStorage relationship between State and City"""
        from models import storage
        list_city = []
        for key, value in storage.all(City).items():
            if value.state_id == self.id:
                list_city.append(value)
        return list_city
