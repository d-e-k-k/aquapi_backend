from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Temperature
from .serializers import TemperatureSerializer, AvgTemperatureSerializer
from datetime import datetime, date
from django.db.models import Avg


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


@api_view(['GET'])
def temperature_list_date_range(request):
    if request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        temperatures = Temperature.objects.filter(
            date__range=[start, end])
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def temperature_list_date_range_interval(request):
    if request.method == 'GET':
        start = request.GET.get('start').split("-")
        end = request.GET.get('end').split("-")
        startDateObj = date(int(start[0]), int(start[1]), int(start[2]))
        endDateObj = date(int(end[0]), int(end[1]), int(end[2]))
        dif_days = (endDateObj - startDateObj).days
        print(dif_days)
        daily_temps = []
        for x in range(0, dif_days):
            xdate = (f"{start[0]}-{start[1]}-{str(int(start[2]) + x)}")
            temps = Temperature.objects.filter(date=xdate)
            avg_temp = temps.aggregate(Avg('temperature'))
            if avg_temp["temperature__avg"]:
                daily_temps.append(
                    {"Date": xdate, "Avg Daily Temperature (F)": '{0:.2f}'.format(avg_temp["temperature__avg"])})
        print(daily_temps)
        return Response(daily_temps)
