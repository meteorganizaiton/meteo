import requests


class MeteoAPI:

    @staticmethod
    def get(url: str, headers: dict = None):
        return requests.get(url)
