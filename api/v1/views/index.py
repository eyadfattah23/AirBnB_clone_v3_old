#!/usr/bin/python3
""" check status of the app
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ returns a JSON: "status": '"OK"'"""
    return jsonify({"status": "OK"})
