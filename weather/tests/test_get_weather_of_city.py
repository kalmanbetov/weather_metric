from django.test import TestCase, Client
from unittest import mock

from rest_framework import status

from weather.tests.mymock import (
    SuccessMockResponse, FailureMockResponse, SuccessButNotWaitedMockResponse,
    FailureButNotWaitedMockResponseOn404, FailureMockResponseOn404,
)


class TestWeatherAPIView(TestCase):
    # maxDiff = None

    def setUp(self) -> None:
        self.client = Client()

    @mock.patch('requests.get', return_value=SuccessMockResponse())
    def test_weather_success_200(self, mocked):
        response = self.client.get('/weather/Bishkek/')
        expected_data = {
            "id": 1528675,
            "name": "Bishkek",
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "main": {
                "temp": 279.15,
                "feels_like": 275.73,
                "temp_min": 279.15,
                "temp_max": 279.15,
                "pressure": 1018,
                "humidity": 87
            },
            "wind": {
                "speed": 3,
                "deg": 100
            },
            "sys": {
                "id": 8871,
                "type": 1,
                "country": "KG",
                "sunrise": 1616288605,
                "sunset": 1616332454
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    @mock.patch('requests.get', return_value=FailureMockResponseOn404())
    def test_weather_failure_on_404(self, mocked):
        response = self.client.get('/weather/test/')
        expected_data = {
            "message": "city not found",
        }
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_data)

    @mock.patch('requests.get', return_value=SuccessButNotWaitedMockResponse())
    def test_weather_status_200_but_coming_not_waiting_data(self, mocked):
        response = self.client.get('/weather/Talas/')
        expected_data = {'message': 'Weather service not send expected_data'}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_data)

    @mock.patch('requests.get', return_value=FailureButNotWaitedMockResponseOn404())
    def test_weather_failure_on_404_but_coming_not_waiting_data(self, mocked):
        response = self.client.get('/weather/tests/')
        expected_data = {'message': 'Weather service not send expected_data'}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_data)

    @mock.patch('requests.get', return_value=FailureMockResponse())
    def test_weather_failure(self, mocked):
        response = self.client.get('/weather/tests/')
        expected_data = {'message': 'something get wrong when getting data from weather server',}
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data, expected_data)
