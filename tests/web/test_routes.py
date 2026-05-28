import sys, os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.web.app.routes import main

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_endpoint(client):
    response = client.post('/', data={
        'team1': ' Australia ',
        'team2': ' India ',
        'innings_t1': 1,
        'venue_t1': 1,
        'ground': ' Chennai ',
        'choice': 1
    })
    assert response.status_code == 200
    assert b'result' in response.data