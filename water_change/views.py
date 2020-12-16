from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import WaterChange
from .serializer import WaterChangeSerializer

# Create your views here.

