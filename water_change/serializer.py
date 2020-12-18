from rest_framework import serializers
from .models import WaterChange

class WaterChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterChange
        # fields = ('id',)
        fields = "__all__"
        # fields = ('id', 'water_change_date', 'water_change_interval', 'time_stamp', 'completed')
