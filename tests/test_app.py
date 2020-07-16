import pytest
import json


@pytest.fixture
def json_return():
    with open('data/charging_stations.json') as data:
        json_return = json.load(data)
    return json_return


def test_returned_data_type_is_dictionary(json_return):
    assert isinstance(json_return, dict)


def test_returned_string_contains_data_key(json_return):
    assert 'data' in json_return


def test_returned_string_contains_latitude_key(json_return):
    assert json_return['data'][0]['latitude'] == '41.401478'