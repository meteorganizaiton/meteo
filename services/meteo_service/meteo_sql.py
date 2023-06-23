from datetime import datetime

import mysql.connector


class MeteoSQL:

    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="meteo_db"
        )
        self.cursor = self.cnx.cursor()

    def insert_location_data(self, city_id: int, city_name: str, country_code: str, timezone: int, coord: str,
                             request_time: datetime):
        self.cursor.execute(
            f"""INSERT INTO meteo_db.locations(id,city_name,country_code,timezone,coord,created_at,updated_at) 
                VALUES ({city_id},'{city_name}','{country_code}',{timezone},'{coord}','{request_time}','{request_time}');""")
        self.cnx.commit()

    def select_city_id_by_city_name(self, name: str):
        pass

    def select_current_weather_by_city_id(self, id_: int):
        pass


if __name__ == '__main__':
    meteo_sql = MeteoSQL()
    meteo_sql.insert_location_data()
