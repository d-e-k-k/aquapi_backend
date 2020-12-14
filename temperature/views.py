from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Temperature
from .serializers import TemperatureSerializer
from datetime import datetime


@api_view(['GET', 'POST'])
def temperature_list(request):
    if request.method == 'GET':
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.is_superuser:
            serializer = TemperatureSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif not request.user.is_superuser:
            return Response("Unauthorized Request", status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['GET', 'DELETE'])
def temperature_detail(request, pk):
    try:
        temperature = Temperature.objects.get(pk=pk)
    except Temperature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)
    elif request.method == 'DELETE' and request.user.is_superuser:
            temperature.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response("Unauthorized Request", status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def temperature_detail(request, pk):
#     try:
#         temperature = Temperature.objects.get(pk=pk)
#     except Temperature.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#        temperature.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def temperature_list_date_range(request):
    if request.method == 'GET':
        temperatures = Temperature.objects.filter(
            date__range=["12-12-2020", "13-12-2020"])
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

# from rest_framework import generics
# from rest_framework import serializers
# from rest_framework.permissions import IsAdminUser
# from .models import Temperature
# from .serializers import TemperatureSerializer

# # class Temperature_list(generics.ListCreateAPIView):
# #     queryset = Temperature.objects.all()
# #     serializer_class = TemperatureSerializer
