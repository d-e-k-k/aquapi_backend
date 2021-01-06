
from rest_framework import serializers
from .models import Temperature

class TemperatureSerializer(serializers.ModelSerializer):
    temperature = serializers.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        model = Temperature
        fields = ('id', 'date', 'temperature', 'time')


class AvgTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id', 'temperature')
