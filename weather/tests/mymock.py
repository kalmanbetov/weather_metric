from rest_framework import status

from weather.tests import constants


class SuccessMockResponse:
    def __init__(self):
        self.status_code = status.HTTP_200_OK

    def json(self):
        return constants.WEATHER_SUCCESS_JSON_RESPONSE_ON_200


class FailureMockResponseOn404:
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND

    def json(self):
        return constants.WEATHER_FAILURE_JSON_RESPONSE_ON_404


class SuccessButNotWaitedMockResponse:
    def __init__(self):
        self.status_code = status.HTTP_200_OK

    def json(self):
        return constants.WEATHER_SUCCESS_JSON_RESPONSE_ON_200_BUT_NOT_WAITED


class FailureButNotWaitedMockResponseOn404:
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND

    def json(self):
        return constants.WEATHER_FAILURE_JSON_RESPONSE_ON_404_BUT_NOT_WAITED


class FailureMockResponse:
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
