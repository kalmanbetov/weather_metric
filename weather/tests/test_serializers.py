from django.test import TestCase, Client
from unittest import mock

from rest_framework import status

from weather import constants
from weather.mymock import SuccessMockResponse, FailureMockResponse
from weather.serializers import WeatherInfoSerializer


class TestWeatherInfoSerializer(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    @mock.patch('requests.get', return_value=SuccessMockResponse())
    def test_weather_serializer(self, mocked):
        serializer = WeatherInfoSerializer(data=constants.SUCCESS_JSON_RESPONSE)
        serializer.is_valid()
        response = self.client.get('/weather/Bishkek/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
