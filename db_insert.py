#!/usr/bin/env python3
""" Get the JSON data form the Raspberry Pi and insert it into the database """

# Argument parsing, requests for REST API client and variables from config.py
import argparse
import requests
from config import SENSOR_URL

# Database configuration (DATABASE is defined in config.py as sqlite:///foxie.db)
from config import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import database structure, as defined in foxie/database.py:
from foxie.database import Base, Foxie

# Retrieve remote sensor data as JSON from REST API using requests:
def get_pi(url):
    """Get JSON data from remote server running on Pi"""
    r = requests.get(url)
    return (r.json())

# Parse arguments (specify custom URL or use default SENSOR_URL from config.py)
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="url to raspberry pi", default=SENSOR_URL)
args = parser.parse_args()

# Retrieve the data from the sensor API
pi = get_pi(args.url)
print(pi)

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

# Prepare to insert data in the database:
new_reading = Foxie(
    corrected_temp = pi['corrected_temp'],
    cpu_temp = pi['cpu_temp'],
    engineers = pi['engineers'],
    fqdn = pi['fqdn'],
    humidity = pi['humidity'],
    latitude = pi['latitude'],
    location = pi['location'],
    longitude = pi['longitude'],
    pi_ver = pi['pi_ver'],
    pressure = pi['pressure'],
    project = pi['project'],
    sealevel = pi['sealevel'],
    sensorid = pi['sensorid'],
    temperature = pi['temperature'],
    tz = pi['tz']
    )

# Commit the reading to the database
session.add(new_reading)
session.commit()
