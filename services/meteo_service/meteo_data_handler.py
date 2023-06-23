from dataclasses import dataclass


@dataclass
class MeteoDataHandler:

    @staticmethod
    def map_city_current_weather_data(json_data: dict):
        id_ = json_data['id']
        city_name = json_data['name']
        country_code = json_data['sys']['country']
        timezone = json_data['timezone']
        coord = json_data['coord']
        return id_, city_name, country_code, timezone, coord
