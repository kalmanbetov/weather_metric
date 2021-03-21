import requests
from django.conf import settings
from rest_framework import status

from weather.serializers import WeatherInfoSerializer, Weather404Serializer


class WeatherService:
    @classmethod
    def get_weather_info(cls, city: str):
        url = f'{settings.WEATHER_API}?q={city}&appid={settings.WEATHER_API_KEY}'
        response = requests.get(url)
        bad_json_response = {'message': 'Weather service not send expected_data'}
        if response.status_code == status.HTTP_200_OK:
            serializer = WeatherInfoSerializer(data=response.json())
            if serializer.is_valid():
                return serializer.data, status.HTTP_200_OK
            else:
                return bad_json_response, status.HTTP_400_BAD_REQUEST
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            serializer = Weather404Serializer(data=response.json())
            if serializer.is_valid():
                return serializer.data, status.HTTP_404_NOT_FOUND
            else:
                return bad_json_response, status.HTTP_400_BAD_REQUEST
        else:
            response = {
                'message': 'something get wrong when getting data from weather server',
            }
            return response, status.HTTP_500_INTERNAL_SERVER_ERROR
