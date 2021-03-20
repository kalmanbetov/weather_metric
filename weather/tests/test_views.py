from django.test import TestCase, Client
from unittest import mock

from rest_framework import status

from weather import constants
from weather.mymock import SuccessMockResponse, FailureMockResponse


class TestWeatherAPIView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    @mock.patch('requests.get', return_value=SuccessMockResponse())
    def test_weather_success(self, mocked):
        response = self.client.get('/weather/Bishkek/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, constants.SUCCESS_JSON_RESPONSE)

    @mock.patch('requests.get', return_value=FailureMockResponse())
    def test_weather_failure(self, mocked):
        response = self.client.get('/weather/test/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, constants.FAILURE_JSON_RESPONSE)
