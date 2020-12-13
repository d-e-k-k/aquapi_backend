from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Temperature
from .serializers import TemperatureSerializer


@api_view(['GET', 'POST'])
def temperature_list(request):
    if request.method == 'GET':
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def temperature_detail(request, pk):
    try:
        temperature = Temperature.objects.get(pk=pk)
    except Temperature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def temperature_detail(request, pk):
    try:
        temperature = Temperature.objects.get(pk=pk)
    except Temperature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
       temperature.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
# from rest_framework import generics
# from rest_framework import serializers
# from rest_framework.permissions import IsAdminUser
# from .models import Temperature
# from .serializers import TemperatureSerializer

# # class Temperature_list(generics.ListCreateAPIView):
# #     queryset = Temperature.objects.all()
# #     serializer_class = TemperatureSerializer
