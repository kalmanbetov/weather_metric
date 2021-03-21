WEATHER_SUCCESS_JSON_RESPONSE_ON_200 = {
    "coord": {
        "lon": 74.59,
        "lat": 42.87
    },
    "weather": [
        {
            "id": 804,
            "main": "Clouds",
            "description": "overcast clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 279.15,
        "feels_like": 275.73,
        "temp_min": 279.15,
        "temp_max": 279.15,
        "pressure": 1018,
        "humidity": 87
    },
    "visibility": 10000,
    "wind": {
        "speed": 3,
        "deg": 100
    },
    "clouds": {
        "all": 90
    },
    "dt": 1616313311,
    "sys": {
        "type": 1,
        "id": 8871,
        "country": "KG",
        "sunrise": 1616288605,
        "sunset": 1616332454
    },
    "timezone": 21600,
    "id": 1528675,
    "name": "Bishkek",
    "cod": 200
}

WEATHER_FAILURE_JSON_RESPONSE_ON_404 = {
    "cod": "404",
    "message": "city not found"
}


WEATHER_SUCCESS_JSON_RESPONSE_ON_200_BUT_NOT_WAITED = {
    "weather": [
        {
            "id": 804,
            "main": "Clouds",
            "description": "overcast clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 279.15,
        "feels_like": 275.73,
        "temp_min": 279.15,
        "temp_max": 279.15,
        "pressure": 1018,
        "humidity": 87
    },
    "visibility": 10000,
    "wind": {
        "speed": 3,
        "deg": 100
    },
    "clouds": {
        "all": 90
    },
    "dt": 1616313311,
    "sys": {
        "type": 1,
        "id": 8871,
        "country": "KG",
        "sunrise": 1616288605,
        "sunset": 1616332454
    },
    "timezone": 21600,
    "id": 1528675,
    "cod": 200
}

WEATHER_FAILURE_JSON_RESPONSE_ON_404_BUT_NOT_WAITED = {
    "cod": "404",
}

