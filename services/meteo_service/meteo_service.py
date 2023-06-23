from services.meteo_service.common_functions import load_config_file
from services.meteo_service.meteo_api import MeteoAPI
from services.meteo_service.meteo_data_handler import MeteoDataHandler
from services.meteo_service.meteo_sql import MeteoSQL


class MeteoService:

    def __init__(self, env):
        self.env = env
        configurations = load_config_file(f"config_{self.env}.json")
        self.meteo_api = MeteoAPI()
        self.meteo_sql = MeteoSQL()
        self.meteo_dh = MeteoDataHandler()
        self.open_weather_map_url = configurations['open_weather_map_url']
        self.open_weather_map_api_key = configurations['open_weather_map_api_key']
        self.tlv_coordinates = 'lat=32.0852997&lon=34.7818064'

    def get_current_weather_by_city(self, city_name: str):
        r = self.meteo_api.get(self.open_weather_map_url + '?' + self.tlv_coordinates + '&appid=' + self.open_weather_map_api_key)
        self.meteo_sql.insert_location_data(*self.meteo_dh.map_city_current_weather_data(r.json()))
        city_id = self.meteo_sql.select_city_id_by_city_name(city_name)
        current_weather = self.meteo_sql.select_current_weather_by_city_id(city_id)
        return current_weather

    def insert_weather_data_into_mysql_db(self):
        pass  # self.meteo_mysql_connector.insert_weather_data()

    def insert_weather_data_into_mogo_db(self):
        pass

    def insert_weather_data_into_redis_db(self):
        pass
