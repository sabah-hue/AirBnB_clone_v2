#!/usr/bin/python3
"""storage engine module"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {'State': State, 'City': City, 'User': User}


class DBStorage:
    """Data Base Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """constractur of class"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(
                        getenv('HBNB_MYSQL_USER'),
                        getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'),
                        getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dictionary = {}
        for my_class in classes:
            if cls is None or cls is classes[my_class] or cls is my_class:
                for inst in self.__session.query(classes[my_class]).all():
                    key = inst.__class__.__name__ + '.' + inst.id
                    dictionary[key] = inst
        return dictionary

    def new(self, obj):
        """ add the object to the current DB session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current DB session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current DB session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the DB"""
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
