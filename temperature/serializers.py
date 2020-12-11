
from rest_framework import serializers
from .models import Temperature

class TemperatureSerializer(serializers.ModelField):
    class Meta:
        model: Temperature
        fields = ('id', 'temperature', 'date', 'time')