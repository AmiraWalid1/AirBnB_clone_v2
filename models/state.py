#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    from sqlalchemy.orm import relationship
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        citiesList = []
        from models.__init__ import storage
        for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == "City":
                     if v.state_id == self.id:
                          citiesList.append(v)
        return v
