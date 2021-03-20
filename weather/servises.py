import requests
from django.conf import settings

from weather.serializers import WeatherInfoSerializer


class WeatherService:
    @classmethod
    def get_weather_info(cls, city: str):
        url = f'{settings.WEATHER_API}?q={city}&appid={settings.WEATHER_API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            serializer = WeatherInfoSerializer(data=response.json())
            serializer.is_valid(raise_exception=True)
            return serializer.data, response.status_code
        else:
            return response.json(), response.status_code
