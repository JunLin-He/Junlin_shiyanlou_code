""" Create a user table in the blog database
"""
# coding: utf-8

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

ENGINE = create_engine('mysql://root:931212emily@localhost:3306/blog')
Base = declarative_base()


class Article(Base):
    """ The mapping for table: article
    """
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    cate_id = Column(Integer, ForeignKey('categories.id'))
    tags = relationship('Tag', secondary='article_tag', backref='articles')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)


class Category(Base):
    """ The mapping for table: categories
        Relation: one category own multiple articles and multiple tags
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='category')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

    article_tag = Table(
        # The first parameter is the table's name, the second parameter is metadata
        # Both of them are mandatory
        'article_tag', Base.metadata,
        # For asistant table, it store the id of both two tables and set them as foreignkey
        Column('article_id', Integer, ForeignKey('articles.id')),
        Column('tag_id', Integer, ForeignKey('tags.id'))
    )

class Tag(Base):
    """ The mapping for table: tags
    """
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


Base.metadata.create_all(ENGINE)
