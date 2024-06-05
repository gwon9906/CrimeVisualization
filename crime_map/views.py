from django.shortcuts import render
from django.http import JsonResponse
from .models import CrimeData

def crime_map_view(request):
    return render(request, 'crime_map/crime_map.html')

def get_crime_data(request, crime_type):
    data = CrimeData.objects.filter(crime_type=crime_type)
    data_dict = list(data.values())
    return JsonResponse(data_dict, safe=False)