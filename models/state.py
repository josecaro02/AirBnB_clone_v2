#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from os import environ


class State(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    DBStorage = relationship("City", backref="state",
                             cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """ Return the list of the city """
        all_city = models.storage.all(City)
        states = []
        for cities in all_city.values():
            if cities.state_id == self.id:
                states.append(cities)
        return states
