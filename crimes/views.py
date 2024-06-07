from django.shortcuts import render
from crime_map.models import CrimeData  # crime_map의 모델을 가져옴

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

def search_crime_data_view(request):  # 검색 뷰
    if request.method == 'POST':  # POST 요청이 들어왔을 때
        region = request.POST.get('region')  # region을 POST로 받아옴
        crime_data = CrimeDataSystem.search_crime_data(region)  # CrimeDataSystem의 search_crime_data 메서드를 호출
        return render(request, 'crimes/search_results.html', {'crime_data': crime_data})  # 검색 결과를 search_results.html에 전달
    return render(request, 'crimes/search.html')  # GET 요청이 들어왔을 때는 search.html을 렌더링

def add_crime_data_view(request):
    if request.method == 'POST':
        station = request.POST.get('station')
        crime_type = request.POST.get('crime_type')
        year = request.POST.get('year')
        count = request.POST.get('count')
        CrimeDataSystem.add_crime_data(station, crime_type, year, count)
        return render(request, 'crimes/add_success.html')
    return render(request, 'crimes/add_crime_data.html')
