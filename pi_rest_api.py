#!/usr/bin/env python3
"""
Displays Raspberry PI sensor data and platform information as a REST API.
"""
from flask import Flask, jsonify
from foxie.pimock import get_pi_info

app = Flask(__name__)

@app.route('/')
def summary():
    pi = get_pi_info()
    return jsonify(pi)

if __name__ == '__main__':
        app.run('0.0.0.0', port=5000)
