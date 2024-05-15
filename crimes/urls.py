from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.crime_chart),
]