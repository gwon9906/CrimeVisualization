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
`
def search_crime_data_view(request): # 검색 뷰
    if request.method == 'POST':    # POST 요청이 들어왔을 때
        region = request.POST.get('region') # region을 POST로 받아옴
        crime_data = CrimeDataSystem.search_crime_data(region)  # CrimeDataSystem의 search_crime_data 메서드를 호출
        return render(request, 'crimes/search_results.html', {'crime_data': crime_data})    # 검색 결과를 search_results.html에 전달
    return render(request, 'crimes/search.html')    # GET 요청이 들어왔을 때는 search.html을 렌더링

def add_crime_data_view(request):
    if request.method == 'POST':
        crime_type = request.POST.get('crime_type')
        date = request.POST.get('date')
        location = request.POST.get('location')
        frequency = request.POST.get('frequency')
        CrimeDataSystem.add_crime_data(crime_type, date, location, frequency)
        return render(request, 'crimes/add_success.html.html')
    return render(request, 'crimes/add_crime_data.html')
