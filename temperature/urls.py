from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('temperatures/', views.temperature_list),
    path('temperatures/<int:pk>/', views.temperature_detail),
    path('temperatures/range/', views.temperature_list_date_range,),
    path('temperatures/interval/', views.temperature_list_date_range_interval,),
]
