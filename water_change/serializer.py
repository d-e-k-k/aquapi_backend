from rest_framework import serializers
from .models import WaterChange

class WaterChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterChange
        fields = ('water_change_date', 'water_change_interval')
