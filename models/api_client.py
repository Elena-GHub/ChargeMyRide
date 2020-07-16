import requests
from requests.exceptions import HTTPError
import json


class ChargingStation():
    def get_station_data(self):
        url = 'https://datos.gob.es/apidata/catalog/dataset/a09002970-estacions-de-recarrega-per-a-vehicle-electric-a-catalunya.json'
        response = requests.get(url)

        data = response.json()

        return data['response']