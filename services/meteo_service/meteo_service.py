from services.meteo_service.common_functions import load_config_file
from services.meteo_service.meteo_api import MeteoAPI


class MeteoService:

    def __init__(self, env):
        self.env = env
        self.meteo_api = MeteoAPI()
        configurations = load_config_file(f"config_{self.env}.json")
        self.open_weather_map_url = configurations['open_weather_map_url']
        self.open_weather_map_api_key = configurations['open_weather_map_api_key']
        self.tlv_coordinates = 'lat=32.0852997&lon=34.7818064'

    def get_current_weather_by_city(self):
        r = self.meteo_api.get(self.open_weather_map_url + '?' + self.tlv_coordinates + '&appid=' + self.open_weather_map_api_key)
        return r

    def insert_weather_data_into_mysql_db(self):
        pass  # self.meteo_mysql_connector.insert_weather_data()

    def insert_weather_data_into_mogo_db(self):
        pass

    def insert_weather_data_into_redis_db(self):
        pass
