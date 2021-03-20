from rest_framework import serializers


class WindSerializer(serializers.Serializer):
    speed = serializers.FloatField()
    deg = serializers.IntegerField()


class WeatherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    main = serializers.CharField()
    description = serializers.CharField()
    icon = serializers.CharField()


class MainSerializer(serializers.Serializer):
    temp = serializers.FloatField()
    feels_like = serializers.FloatField()
    temp_min = serializers.FloatField()
    temp_max = serializers.FloatField()
    pressure = serializers.IntegerField()
    humidity = serializers.IntegerField()


class SysSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.IntegerField()
    country = serializers.CharField()
    sunrise = serializers.IntegerField()
    sunset = serializers.IntegerField()


class WeatherInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    weather = WeatherSerializer(many=True)
    main = MainSerializer()
    wind = WindSerializer()
    sys = SysSerializer()
