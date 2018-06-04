#!/usr/bin/env python3
""" Read data from the database and offer it as a REST API """

# Flask REST API:
from flask import Flask, jsonify
app = Flask(__name__)

# Database configuration (DATABASE is defined in config.py as sqlite:///foxie.db)
from config import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import database structure, as defined in foxie/database.py:
from foxie.database import Base, Foxie

# Database configuration (DATABASE is defined in config.py as sqlite:///foxie.db)
from config import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import database structure, as defined in foxie/database.py:
from foxie.database import Base, Foxie

# Create an engine that stores data in the local directory
engine = create_engine(DATABASE, encoding = 'latin1', echo = False)

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)

# Bind to the engine and create a session
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Query the temperature value from the database and save it to a list
def get_temp():
    temp_list = []
    for reading in session.query(Foxie.temperature).all():
        temp_list.append(reading.temperature)
    return { "data": temp_list }

# Output the data as JSON to a rest API:
@app.route('/')
def json():
    temp = jsonify(get_temp())
    return temp

# Run Flask
if __name__ == '__main__':
    app.run('0.0.0.0', port = 8001)
