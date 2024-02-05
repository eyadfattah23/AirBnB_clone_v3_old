#!/usr/bin/python3
"""tests for flask app"""
import unittest
from flask import jsonify
from api.v1.app import app


class TestFlask(unittest.TestCase):

    def setUp(self):
        """ Set up the Flask testing client"""
        self.client = app.test_client()
        # Create a Flask application context
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        """ Clean up any resources"""
        self.app_context.pop()

    def test_status_endpoint(self):
        """ Make a request to the '/status' endpoint"""
        response = self.client.get('/api/v1/status')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the response content is as expected
        expected_response = jsonify({"status": "OK"}).json
        self.assertEqual(response.json, expected_response)

    def test_404_endpoint(self):
        """ Make a request to the "not found" endpoint"""
        response = self.client.get('/api/v1/nop')

        self.assertEqual(response.status_code, 404)

        expected_response = jsonify({"error": "Not found"}).json
        self.assertEqual(response.json, expected_response)
