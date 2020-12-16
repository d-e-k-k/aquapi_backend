from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import WaterChange
from .serializer import WaterChangeSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def water_change_details(request):
    if request.method == 'GET':
        details = WaterChange.objects.all()
        serializer = WaterChangeSerializer(details, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WaterChangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_status(request, pk):
    try:
        details = WaterChange.objects.filter(pk=pk)
    except WaterChange.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        serializer = WaterChangeSerializer( data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
