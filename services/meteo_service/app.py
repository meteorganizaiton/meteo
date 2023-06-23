import os
from services.meteo_service.meteo_service import MeteoService
import requests
from flask import Flask, jsonify

app = Flask(__name__)
ms = MeteoService(os.getenv('ENV'))


@app.route('/weather', methods=['GET'])
def get_weather():
    city_weather_data = ms.get_current_weather_by_city()
    return jsonify(city_weather_data.json())


if __name__ == '__main__':
    app.run()
