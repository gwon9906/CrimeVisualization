from django.urls import path
from .views import search_crime_data_view, add_crime_data_view

urlpatterns = [
    path('search/', search_crime_data_view, name='search_crime_data'),
    path('add/', add_crime_data_view, name='add_crime_data'),
]