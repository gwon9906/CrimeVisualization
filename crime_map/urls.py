from django.urls import path
from .views import index, crime_data, crime_details, get_crime_data
from .views import index, crime_data, crime_details

urlpatterns = [
    path('', index, name='index'),
    path('crime_data/<str:crime_type>/', crime_data, name='crime_data'),
    path('crime_data/<str:crime_type>/<int:year>/<str:station>/', crime_details, name='crime_details'),
    path('details/', crime_details, name='crime_details'),
    path('get_crime_data/<str:crime_type>/', get_crime_data, name='get_crime_data'),
]
