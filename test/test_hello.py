# import unittest 
"""
Tests flask app
"""
import pytest
from hello import app

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello World!'
    