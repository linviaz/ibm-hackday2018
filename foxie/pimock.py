#!/usr/bin/env python3
"""
This module emulates system information, hostname, and sensor data
from a Raspberry Pi with sensehat.
"""

from datetime import datetime
from random import random

def get_pi_info():
    variance = random()
    mockup = {
        "corrected_temp": 22 + variance,
        "cpu_temp": 47.2 + variance,
        "engineers": "Lin Zhang; Mihai Criveti",
        "fqdn": "raspberrypi",
        "humidity": 41.667564392089844 + variance,
        "latitude": 53.3931987 + variance,
        "location": "Dublin",
        "longitude": -6.3771932,
        "pi_ver": "Raspberry Pi 3 Model B Rev 1.2",
        "pressure": 992.492431640625 + variance,
        "project": "foxie",
        "sealevel": 62,
        "sensorid": 1,
        "temperature": 30.502558708190918 + variance,
        "timestamp": str(datetime.utcnow()),
        "tz": "Etc/UTC"
    }

    return mockup

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS)
    print(get_pi_info())
