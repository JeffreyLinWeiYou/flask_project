# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Float, BigInteger
from sqlalchemy import create_engine
from blueprints.setting import DB_URI
from flask import Blueprint


recognition_model = Blueprint('recognition', __name__)


engine = create_engine(DB_URI, max_overflow=5)

Base = declarative_base()

class Recognition(Base):
    __tablename__ = 'recognition'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    resultIdx = Column(Text)
    time = Column(BigInteger)
    dbId = Column(Text)
    score = Column(Float)
    user_idx = Column(Text)

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

init_db()