import sys, os
import pytest

from web.app.routes import main

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


def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    
    # Verify it returns the correct JSON keys
    json_data = response.get_json()
    assert json_data["status"] == "healthy"
    assert "CricAI" in json_data["message"]