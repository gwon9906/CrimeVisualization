# crimes/views.py

from django.shortcuts import render
from .models import CrimeData

class CrimeDataSystem:
    @staticmethod
    def search_crime_data(region):
        return CrimeData.objects.filter(location__icontains=region)

    @staticmethod
    def add_crime_data(crime_type, date, location, frequency):
        return CrimeData.objects.create(
            crime_type=crime_type,
            date=date,
            location=location,
            frequency=frequency
        )

def search_crime_data_view(request):
    if request.method == 'POST':
        region = request.POST.get('region')
        crime_data = CrimeDataSystem.search_crime_data(region)
        return render(request, 'crimes/search_results.html', {'crime_data': crime_data})
    return render(request, 'crimes/search.html')

def add_crime_data_view(request):
    if request.method == 'POST':
        crime_type = request.POST.get('crime_type')
        date = request.POST.get('date')
        location = request.POST.get('location')
        frequency = request.POST.get('frequency')
        CrimeDataSystem.add_crime_data(crime_type, date, location, frequency)
        return render(request, 'crimes/add_success.html.html')
    return render(request, 'crimes/add_crime_data.html')
