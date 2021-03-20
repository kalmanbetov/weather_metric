SUCCESS_JSON_RESPONSE = {
    "id": 299900,
    "name": "Talas",
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04d"
        }
    ],
    "main": {
        "temp": 282.15,
        "feels_like": 279.8,
        "temp_min": 282.15,
        "temp_max": 282.15,
        "pressure": 1018,
        "humidity": 53
    },
    "wind": {
        "speed": 0.51,
        "deg": 0
    },
    "sys": {
        "id": 6963,
        "type": 1,
        "country": "TR",
        "sunrise": 1616211682,
        "sunset": 1616255347
    }
}

FAILURE_JSON_RESPONSE = {
    "cod": "404",
    "message": "city not found"
}
