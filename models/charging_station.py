# from flask_sqlalchemy import SQLAlchemy


class ChargingStation:   # o con   db.Model  entre paréntesis

    def __init__(self, id: int, access: str, charging_speed: str, connection_type: str, latitude: str, longitude: str, name: str, power: str, power_type: str, address: str, province: str, town: str, parking_slots: int, vehicle_type: str, geo_reference: str):
        self.id = id
        self.access = access
        self.charging_speed = charging_speed
        self.connection_type = connection_type
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.power = power
        self.power_type = power_type
        self.address = address
        self.province = province
        self.town = town
        self.parking_slots = parking_slots
        self.vehicle_type = vehicle_type
        self.geo_reference = geo_reference

    def to_json(self):
        return {
            'id': self.id,
            'access': self.access,
            'charging_speed': self.charging_speed,
            'connection_type': self.connection_type,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'name': self.name,
            'power': self.power,
            'power_type': self.power_type,
            'address': self.address,
            'province': self.province,
            'town': self.town,
            'parking_slots': self.parking_slots,
            'vehicle_type': self.vehicle_type,
            'geo_reference': self.geo_reference
        }
