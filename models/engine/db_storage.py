#!/usr/bin/python3
"""SQLAlchemy will be your best friend!"""
from os import getenv
from sqlalchemy import (create_engine)
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Private class attributes"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pw = getenv("HBNB_MYSQL_PWD")
        ht = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        environment = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user, pw, ht, db),
                                      pool_pre_ping=True)
        if environment == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from obj from the session"""
        self.__session.delete(obj)

    def close(self):
        """Close session"""
        self.__session.close()

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)()
        Session = scoped_session(session)
        self.__Session = Session()

    def all(self, cls=None):
        """Return a Dict"""
        dt = {}
        if cls:
            cls = eval(cls)
            for instance in self.__session.query(cls):
                dt["{}.{}"
                   .format(type(instance).__name__, instance.id)] = instance
        else:
            instances = ['User', 'Place', 'Review', 'City', 'Amenity', 'State']
            for elem in instances:
                for i in self.__session.query(elem):
                    dt["{}.{}"
                        .format(type(instance).__name__, instance.id)] = i
        return dt
