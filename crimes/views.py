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

    @staticmethod
    def additional_data(region, year):
        return CrimeData.objects.filter(station__icontains=region, year=year)


def search_crime_data_view(request):
    if request.method == 'POST':
        region = request.POST.get('region')
        crime_data = CrimeDataSystem.search_crime_data(region)
        crime_data_json = list(crime_data.values())  # JSON 형태로 변환

        if not crime_data_json:
            return render(request, 'crimes/search_results.html',
                          {'message': 'No data found for the given region', 'region': region})

        # 범죄 유형별 합산 데이터를 계산합니다.
        total_data = {
            'murder': sum(crime['murder'] for crime in crime_data_json),
            'robbery': sum(crime['robbery'] for crime in crime_data_json),
            'sexual_crime': sum(crime['sexual_crime'] for crime in crime_data_json),
            'theft': sum(crime['theft'] for crime in crime_data_json),
            'violence': sum(crime['violence'] for crime in crime_data_json)
        }

        # 범죄 유형별 연도별 데이터를 준비합니다.
        yearly_data = {year: {'murder': 0, 'robbery': 0, 'sexual_crime': 0, 'theft': 0, 'violence': 0} for year in
                       range(2018, 2024)}
        for crime in crime_data_json:
            yearly_data[crime['year']]['murder'] += crime['murder']
            yearly_data[crime['year']]['robbery'] += crime['robbery']
            yearly_data[crime['year']]['sexual_crime'] += crime['sexual_crime']
            yearly_data[crime['year']]['theft'] += crime['theft']
            yearly_data[crime['year']]['violence'] += crime['violence']

        years = list(range(2023, 2017, -1))

        return render(request, 'crimes/search_results.html',
                      {'total_data': total_data, 'region': region, 'years': years, 'crime_data': crime_data_json,
                       'yearly_data': yearly_data})
    return render(request, 'crimes/search.html')

def add_crime_data_view(request):
    if request.method == 'POST':
        station = request.POST.get('station')
        crime_type = request.POST.get('crime_type')
        year = request.POST.get('year')
        count = request.POST.get('count')
        CrimeDataSystem.add_crime_data(station, crime_type, year, count)
        if not station or not crime_type or not year or not count:
            return render(request, 'crimes/add_crime_data.html', {
                'message': 'All fields are required. Please provide all the necessary information.',
            })
        return render(request, 'crimes/add_success.html')
    return render(request, 'crimes/add_crime_data.html')

def get_crime_data_by_year(request, region, year):
    crime_data = CrimeData.objects.filter(station__icontains=region, year=year)
    crime_data_json = list(crime_data.values())  # JSON 형태로 변환
    return JsonResponse(crime_data_json, safe=False)