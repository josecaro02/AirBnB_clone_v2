#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.citu import City
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """List of cities"""
        list = []
        cities = models.engine.all(City)
        for citie in cities.values():
            if citie.state_id == self.id:
                list.append(citie)
        return list
