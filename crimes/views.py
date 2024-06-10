from django.shortcuts import render
from crimes.models import CrimeData  # crimes의 모델을 가져옴
from django.http import JsonResponse
import datetime

class CrimeDataSystem:
    @staticmethod
    def search_crime_data(region):
        return CrimeData.objects.filter(station__icontains=region)

    @staticmethod
    def add_crime_data(station, crime_type, year, count):
        return CrimeData.objects.create(
            station=station,
            crime_type=crime_type,
            year=year,
            count=count,
        )


def search_crime_data_view(request):
    if request.method == 'POST':
        region = request.POST.get('region')
        crime_data = CrimeDataSystem.search_crime_data(region)
        crime_data_json = list(crime_data.values())  # JSON 형태로 변환

        if not crime_data_json:
            return render(request, 'crimes/search_results.html',
                          {'message': 'No data found for the given region', 'region': region})

        current_year = datetime.datetime.now().year
        years = list(range(current_year, current_year - 20, -1))

        return render(request, 'crimes/search_results.html',
                      {'crime_data': crime_data_json, 'region': region, 'years': years})
    return render(request, 'crimes/search.html')

def add_crime_data_view(request):
    if request.method == 'POST':
        station = request.POST.get('station')
        crime_type = request.POST.get('crime_type')
        year = request.POST.get('year')
        count = request.POST.get('count')
        CrimeDataSystem.add_crime_data(station, crime_type, year, count)
        return render(request, 'crimes/add_success.html')
    return render(request, 'crimes/add_crime_data.html')

def get_crime_data_by_year(request, region, year):
    crime_data = CrimeData.objects.filter(station__icontains=region, year=year)
    crime_data_json = list(crime_data.values())  # JSON 형태로 변환
    return JsonResponse(crime_data_json, safe=False)