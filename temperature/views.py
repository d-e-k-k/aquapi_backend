from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from .models import Temperature
from .serializers import TemperatureSerializer

class Temperature_list(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
