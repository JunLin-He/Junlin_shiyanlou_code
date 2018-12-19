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
    articles = relationship('Article', backref='author')
    userinfo = relationship('UserInfo', backref='user', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


class UserInfo(Base):
    """ The mapping for table: userinfo
        Relation: one user own one userinfo
    """
    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    link = Column(String(64))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

Base.metadata.create_all(ENGINE)
