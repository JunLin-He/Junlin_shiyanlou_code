""" Create a user table in the blog database
"""
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

ENGINE = create_engine('mysql://root:931212emily@localhost:3306/blog')
Base = declarative_base()

class User(Base):
    """ The mapping for table: user
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


class Article(Base):
    """ The mapping for table: article
        Relation: one user own multiple article
    """ 
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

Base.metadata.create_all(ENGINE)
