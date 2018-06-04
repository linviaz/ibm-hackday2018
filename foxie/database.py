#!/usr/bin/env python3
"""
This module defines the database
"""

import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Declare the Foxie class:
class Foxie(Base):
    __tablename__ = 'foxie'
    id = Column(Integer, primary_key=True)
    corrected_temp = Column(Float, nullable = False)
    cpu_temp = Column(Float, nullable = False)
    engineers = Column(String(255))
    fqdn = Column(String(255))
    humidity = Column(Float, nullable = False)
    latitude = Column(Float, nullable = False)
    location = Column(String(255))
    longitude = Column(Float, nullable = False)
    pi_ver = Column(String(255))
    pressure = Column(Float, nullable = False)
    project = Column(String(255))
    sealevel = Column(Float, nullable = False)
    sensorid = Column(Integer, nullable = False)
    temperature = Column(Float, nullable = False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    tz = Column(String(255))
