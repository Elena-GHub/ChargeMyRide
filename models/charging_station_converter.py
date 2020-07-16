from models.charging_station import ChargingStation


class ChargingStationConverter:
    def convert_charging_station(self, data):
        charging_station = ChargingStation(
            id=data['id'],
            access=data['access'],
            charging_speed=data['charging_speed'],
            connection_type=data['connection_type'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            name=data['name'],
            power=data['power'],
            power_type=data['power_type'],
            address=data['address'],
            province=data['province'],
            town=data['town'],
            parking_slots=data['parking_slots'],
            vehicle_type=data['vehicle_type'],
            geo_reference=data['geo_reference']
        )

        return charging_station

    def convert_charging_stations_list(self, data):
        charging_stations_list = []

        for charging_station_data in data:
            charging_station = self.convert_charging_station(charging_station_data)
            charging_stations_list.append(charging_station)

        return charging_stations_list
