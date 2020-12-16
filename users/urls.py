from django.urls import path
from django.conf.urls import include
from django.contrib import admin



urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # path('', include('temperature.urls')),
    
]
