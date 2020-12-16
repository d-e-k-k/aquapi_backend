from django.urls import path
from . import views

urlpatterns = [
    path('water-change/', views.water_change_details),
]
