from rest_framework import generics
from rest_framework import serializers
from .models import Temperature
from .serializers import TemperatureSerializer

class Temperature_list(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializers_class = TemperatureSerializer
    
