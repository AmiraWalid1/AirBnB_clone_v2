#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey ,Column, Integer, String
from sqlalchemy.orm import relationship
from models.user import User
from models.place import Place


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60),ForeignKey("places.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60),ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    text = Column(String(1024), nullable=False)
    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")