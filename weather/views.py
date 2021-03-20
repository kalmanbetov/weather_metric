from rest_framework import generics
from rest_framework.response import Response

from weather.serializers import WeatherInfoSerializer
from weather.servises import WeatherService


class WeatherAPIView(generics.GenericAPIView):
    serializer_class = WeatherInfoSerializer

    def get(self, request, *args, **kwargs):
        city = kwargs.get('city')
        response_data, status_code = WeatherService.get_weather_info(city)

        return Response(response_data, status=status_code)
