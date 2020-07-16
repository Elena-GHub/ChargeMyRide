import json

import pytest

from models import charging_station, charging_station_converter
from models.charging_station_converter import ChargingStationConverter
from models.charging_station import ChargingStation


@pytest.fixture
def charging_stations():
    with open('data/charging_stations.json') as file:
        charging_stations = json.load(file)
    return charging_stations


# @pytest.fixture
# def data():
#     return data(
#     "id": 1,
#     "access": "Aparcament public",
#     "charging_speed": "NORMAL",
#     "connection_type": "Schuko",
#     "latitude": "41.401478",
#     "longitude": "2.156578",
#     "name": "B:SM 56 - Plaça del Sol",
#     "power": "",
#     "power_type": "",
#     "address": "Plaça del Sol, 5",
#     "province": "Barcelona",
#     "town": "Barcelona",
#     "parking_slots": 1,
#     "vehicle_type": "cotxe",
#     "geo_reference": "POINT (2.156578 41.401478)"
#     )


def test_charging_station_converter_turns_json_return_into_object():
    data = {
        "id": 1,
        "access": "Aparcament public",
        "charging_speed": "NORMAL",
        "connection_type": "Schuko",
        "latitude": "41.401478",
        "longitude": "2.156578",
        "name": "B:SM 56 - Plaça del Sol",
        "power": "",
        "power_type": "",
        "address": "Plaça del Sol, 5",
        "province": "Barcelona",
        "town": "Barcelona",
        "parking_slots": 1,
        "vehicle_type": "cotxe",
        "geo_reference": "POINT (2.156578 41.401478)"
        }
    charging_station = ChargingStationConverter().convert_charging_station(data)
    assert isinstance(charging_station, ChargingStation)


# def test_convert_charging_station_list():
#     charging_stations_list = []
#     data = {
#         [
#             {
#                 "id": 1,
#                 "access": "Aparcament public",
#                 "charging_speed": "NORMAL",
#                 "connection_type": "Schuko",
#                 "latitude": "41.401478",
#                 "longitude": "2.156578",
#                 "name": "B:SM 56 - Plaça del Sol",
#                 "power": "",
#                 "power_type": "",
#                 "address": "Plaça del Sol, 5",
#                 "province": "Barcelona",
#                 "town": "Barcelona",
#                 "parking_slots": 1,
#                 "vehicle_type": "cotxe",
#                 "geo_reference": "POINT (2.156578 41.401478)"
#             },
#             {
#                 "id": 2,
#                 "access": "",
#                 "charging_speed": "semiRAPID",
#                 "connection_type": "TESLA i MENNEKES",
#                 "latitude": "41.40548",
#                 "longitude": "2.19148",
#                 "name": "CC Glories (22kW)",
#                 "power": 22,
#                 "power_type": "AC",
#                 "address": "Avinguda Diagonal 208",
#                 "province": "Barcelona",
#                 "town": "Barcelona",
#                 "parking_slots": 14,
#                 "vehicle_type": "",
#                 "geo_reference": "POINT (2.19148 41.40548)"
#             }
#         ]
#     }

    # for charging_station in data:

    
    #     assert self.assertTrue(charging_stations_list)
