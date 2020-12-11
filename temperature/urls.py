from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('temperatures/', views.Temperature_list.as_view())
]