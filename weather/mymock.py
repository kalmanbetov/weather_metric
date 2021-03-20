from rest_framework import status

from weather import constants


class SuccessMockResponse:
    def __init__(self):
        self.status_code = status.HTTP_200_OK

    def json(self):
        return constants.SUCCESS_JSON_RESPONSE


class FailureMockResponse:
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND

    def json(self):
        return constants.FAILURE_JSON_RESPONSE
