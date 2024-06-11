from django.urls import path
from .views import search_crime_data_view, get_crime_data_by_year

urlpatterns = [
    path('search/', search_crime_data_view, name='search_crime_data'),
    path('search/<str:region>/<int:year>/', get_crime_data_by_year, name='get_crime_data_by_year'),
]
