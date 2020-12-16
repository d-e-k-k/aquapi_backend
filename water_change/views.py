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
