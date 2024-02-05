#!/usr/bin/python3

"""
script to create a variable app, instance of Flask
to start our web app
"""

from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(error):
    """a function to call storage.close()"""
    return storage.close()


@app.errorhandler(404)
def not_found(error):
    """a function to handle default 404 HTML response
    with a JSON response"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    hbnb_api_host = getenv('HBNB_API_H', '0.0.0.0')
    hbnb_api_port = getenv('HBNB_API_PORT', 5000)
    app.run(host=hbnb_api_host, port=int(hbnb_api_port), threaded=True)
