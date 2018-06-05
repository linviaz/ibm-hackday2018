# Foxie Pi
> By Mihai Criveti and Lin Zhang
> Raspberry Pi - IoT and Cognitive Platform with Python Flask, Requests and Bokeh
> An educational tool and framework for monitoring and collecting IoT sensor data using the Raspberry Pi in a Client / Server model.

## Video Presentation:
- https://youtu.be/bcJ-k2CZtr0

## Documentation:
- Documentation: [docs/project/site/index.html](docs/project/site/index.html)
- API: [docs/api](docs/api)


![foxie.jpg](foxie.jpg)

## PI Rest API
> `pi_rest_api.py` collects data from sensors on the Raspberry Pi (sense_hat, Texas Instruments T1, USB temperature probe) and system libraries (pi version, cpu temperature, info) and publishes it using Flask as a REST API.
- [X] Displays data from SenseHat
- [X] Push data to pixel display
- [X] Displays more than 1 number on display (for temperature, etc)

## Server: Collects Data from Raspberry Pi and stores the results in a SQL Database
> `db_insert.py` and `db_read.py`. Uses SQLAlchemy ORM and can be configured with your database of choice. SQLite3 by default.
- [X] SQL Database (sqlite3)
- [X] Database model (SQLAlchemy)
- [X] Inserts data into the database
- [X] Reads data from the database

## Front-end: Display Plots / Charts / Interface
> `db_plot.py` - retrieves DATA from the REST API (rows in the database) and plots values using Bokeh.
- [X] Plots data from server database

# Reference:
- https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat
- http://yaab-arduino.blogspot.ie/2016/08/display-two-digits-numbers-on-raspberry.html

