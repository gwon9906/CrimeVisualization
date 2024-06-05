from django.urls import path
from .views import crime_map_view, get_crime_data

urlpatterns = [
    path('', crime_map_view, name='crime_map'),
    path('crime_data/<str:crime_type>/', get_crime_data, name='get_crime_data'),
]
