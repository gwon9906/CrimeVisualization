from django.urls import path
from .views import search_crime_data_view, add_crime_data_view, get_crime_data_by_year

urlpatterns = [
    path('search/', search_crime_data_view, name='search_crime_data'),
    path('add/', add_crime_data_view, name='add_crime_data'),
    path('add/success/', add_crime_data_view, name='add_success'),
    path('search/<str:region>/<int:year>/', get_crime_data_by_year, name='get_crime_data_by_year'),
]
