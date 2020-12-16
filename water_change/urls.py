from django.urls import path
from . import views

urlpatterns = [
    path('water-change/', views.water_change_details),
    path('water-change/<int:pk>', views.update_status),
]
