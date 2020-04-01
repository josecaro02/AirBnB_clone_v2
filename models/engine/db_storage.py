#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import environ


class DBStorage:
    """ Storage for DB
    """
    __engine = None
    __session = None

    def __init__(self):
        """Init"""
        DUser = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        hots = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        dbEnv = environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(DUser, pwd, hots, db),
                                      pool_pre_ping=True)
        if dbEnv == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query on the DB"""
        session = self.__session
        cons = {}
        if not cls:
            tables = [User, State, City, Place]
        else:
            if type(cls) == str:
                cls = eval(cls)
            tables = [cls]
        for row in tables:
            query = session.query(row).all()
            for field in query:
                key = "{}.{}".format(type(field).__name__, field.id)
                cons[key] = field
        return cons

    def new(self, obj):
        """ Add the new object to the session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes sessision"""
        self.__session.close()
