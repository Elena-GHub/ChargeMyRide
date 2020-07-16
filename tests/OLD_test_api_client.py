# from models.api_client import ChargingStation
import pytest
import json
import requests


def test_true_is_true():
    assert True is True


def test_api_client_responding():
    client = api_client.test_client()
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == 'response'
