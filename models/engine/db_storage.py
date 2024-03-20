#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import create_engine
from models.base_model import BaseModel, Base


class DBStorage:
    """class to manage db storage for hbnb clone"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """Return all objects depending of the class name (argument cls)
        this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object"""

        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            queryResults = self.__session.query(cls)
            for result in queryResults:
                key = "{}.{}".format(type(result).__name__, result.id)
                dic[key] = result

        else:
             classesList = [State, City, User, Place, Review, Amenity]
             for clas in classesList:
                queryResults = self.__session.query(clas)
                for result in queryResults:
                    key = "{}.{}".format(type(result).__name__, result.id)
                    dic[key] = result

        return dic

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
    
    def close(self):
        """vlose the seeion"""
        self.__session.close()
