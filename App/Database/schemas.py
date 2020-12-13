# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, Index, Integer, SmallInteger, String, TIMESTAMP, Table, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, CHAR, ENUM, INTEGER, LONGTEXT, TEXT, TINYINT, TINYTEXT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT, primary_key=True)
    uuid = Column(VARCHAR(45), unique=True)
    email = Column(VARCHAR(255), nullable=False)
    first_name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    job_title = Column(VARCHAR(50), nullable=True)
    phone = Column(VARCHAR(50), nullable=True)
