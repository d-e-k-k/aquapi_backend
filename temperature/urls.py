from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('temperatures/', views.temperature_list),
    path('temperatures/<int:pk>/', views.temperature_detail),
    path('temperatures/today/', views.temperature_list_date_range),
]
# path('temperatures/', views.Temperature_list.as_view())
