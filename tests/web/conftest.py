import sys
import os
import pytest

# Import the Flask app
from web.index import app as flask_app


@pytest.fixture
def client():
    """Flask test client fixture"""
    flask_app.config['TESTING'] = True
    flask_app.config['DEBUG'] = False

    with flask_app.test_client() as client:
        yield client