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

# Gets average of all existing temps
# @api_view(['GET'])
# def temperature_list_date_range_interval(request):
#     if request.method == 'GET':
#         temp_avg = Temperature.objects.aggregate(Avg('temperature'))
#         print(temp_avg)
#         return Response(temp_avg)

# gets average from queryset
# @api_view(['GET'])
# def temperature_list_date_range_interval(request):
#     if request.method == 'GET':
#         start = request.GET.get('start')
#         end = request.GET.get('end')
#         temps_qs = Temperature.objects.filter(date__range = [start, end])
#         avg_temp = temps_qs.aggregate(Avg('temperature'))
#         print(avg_temp)
#         return Response(avg_temp)

# gets average for each day in a range days


@api_view(['GET'])
def temperature_list_date_range_interval(request):
    if request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        start_list = start.split("-")
        startDateObj = date(int(start_list[2]), int(start_list[1]), int(start_list[0]))
        end_list = end.split("-")
        endDateObj = date(int(end_list[2]), int(end_list[1]), int(end_list[0]))
        dif_days = (endDateObj - startDateObj).days
        daily_temps=[]
        for x in range(0, dif_days):
            xdate =(f"{str(int(start_list[0]) + x)}-12-2020")
            temps = Temperature.objects.filter(date=xdate)
            avg_temp = temps.aggregate(Avg('temperature'))
            if avg_temp["temperature__avg"]:
                daily_temps.append(
                    {"date": xdate, "avg_temp": '{0:.2f}'.format(avg_temp["temperature__avg"])})
        print(daily_temps)
        return Response(daily_temps)


# Grab each individaul date
# Do a filter query for each individual date
# de
