import pytest
from flask import Flask
from web.index import app as flask_app

def test_app_initialization():
    """
    Verifies that the Flask application instance is correctly created
    and configured with the expected folder structures.
    """
    # 1. Verify it's a valid Flask instance
    assert isinstance(flask_app, Flask)
    
    # 2. Check that your template and static folder overrides are correct
    assert flask_app.template_folder.endswith('app/templates')
    assert flask_app.static_folder.endswith('app/static')


def test_blueprint_registration():
    """
    Ensures that the 'main' blueprint from routes.py is 
    successfully registered onto the core application.
    """
    assert 'main' in flask_app.blueprints


def test_client_environment_config(client):
    """
    Validates that the test environment configuration is active.
    The 'client' fixture is automatically injected by conftest.py.
    """
    assert flask_app.config['TESTING'] is True
    assert flask_app.config['DEBUG'] is False


def test_index_route_integration(client):
    """
    Integration test: Verifies that hitting the root URL via the 
    registered blueprint resolves correctly and returns a 200 OK status.
    """
    response = client.get('/')
    assert response.status_code == 200