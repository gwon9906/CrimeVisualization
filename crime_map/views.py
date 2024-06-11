from django.shortcuts import render
from django.http import JsonResponse
from .models import CrimesCrimedata

# 경찰서의 위치 정보를 사전으로 정의합니다
police_station_locations = {
    '중부': {'lat': 35.1065, 'lng': 129.0350},
    '동래': {'lat': 35.2050, 'lng': 129.0841},
    '영도': {'lat': 35.0861, 'lng': 129.0683},
    '동부': {'lat': 35.1423, 'lng': 129.1111},
    '부산진': {'lat': 35.1608, 'lng': 129.0478},
    '서부': {'lat': 35.0934, 'lng': 128.9836},
    '남부': {'lat': 35.0984, 'lng': 129.0321},
    '해운대': {'lat': 35.1636, 'lng': 129.1630},
    '사상': {'lat': 35.1507, 'lng': 128.9907},
    '금정': {'lat': 35.2420, 'lng': 129.0928},
    '사하': {'lat': 35.1048, 'lng': 128.9748},
    '연제': {'lat': 35.1761, 'lng': 129.0850},
    '강서': {'lat': 35.2124, 'lng': 128.9806},
    '북부': {'lat': 35.2108, 'lng': 129.0139},
    '기장': {'lat': 35.2445, 'lng': 129.2240},
}

def get_crime_data(crime_type):
    crimes = CrimesCrimedata.objects.all()
    crime_dict = []
    for crime in crimes:
        if crime.station in police_station_locations:
            crime_dict.append({
                'station': crime.station,
                'count': getattr(crime, crime_type),
                'year': crime.year,
                'lat': police_station_locations[crime.station]['lat'],
                'lng': police_station_locations[crime.station]['lng']
            })
    return crime_dict

def get_crime_details(crime_type, year, station):
    crime = CrimesCrimedata.objects.filter(year=year, station=station).first()
    if crime:
        crime_count = getattr(crime, crime_type)
        position = police_station_locations.get(station, {'lat': 0, 'lng': 0})
        return {'count': crime_count, 'position': position}
    else:
        return {'count': 0, 'position': None}

def index(request):
    return render(request, 'crime_map/crime_map.html')

def crime_data(request, crime_type):
    crime_type_mapping = {
        "폭력": "violence",
        "성범죄": "sexual_crime",
        "절도": "theft",
        "살인": "murder",
        "강도": "robbery"
    }
    data = get_crime_data(crime_type_mapping[crime_type])
    return JsonResponse(data, safe=False)

def crime_details(request, crime_type, year, station):
    crime_type_mapping = {
        "폭력": "violence",
        "성범죄": "sexual_crime",
        "절도": "theft",
        "살인": "murder",
        "강도": "robbery"
    }
    data = get_crime_details(crime_type_mapping[crime_type], year, station)
    return JsonResponse(data)