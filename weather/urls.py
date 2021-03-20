from django.urls import path

from weather.views import WeatherAPIView

urlpatterns = [
    path('<str:city>/', WeatherAPIView.as_view())
]
