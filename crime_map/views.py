from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import os

# CSV 파일 경로 설정
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'crime_data.csv')
df = pd.read_csv(CSV_FILE_PATH)

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
    crime_type = crime_type.strip()
    filtered_data = df[['경찰서', crime_type, '년도']]
    crime_dict = []
    for index, row in filtered_data.iterrows():
        if row['경찰서'] in police_station_locations:
            crime_dict.append({
                'station': row['경찰서'],
                'count': row[crime_type],
                'year': row['년도'],
                'lat': police_station_locations[row['경찰서']]['lat'],
                'lng': police_station_locations[row['경찰서']]['lng']
            })
    return crime_dict

def get_crime_details(crime_type, year, station):
    filtered_data = df[(df['년도'] == int(year)) & (df['경찰서'] == station)]
    if not filtered_data.empty:
        crime_count = filtered_data.iloc[0][crime_type]
        position = police_station_locations.get(station, {'lat': 0, 'lng': 0})
        return {'count': crime_count, 'position': position}
    else:
        return {'count': 0, 'position': None}

def index(request):
    return render(request, 'crime_map/crime_map.html')

def crime_data(request, crime_type):
    data = get_crime_data(crime_type)
    return JsonResponse(data, safe=False)

def crime_details(request, crime_type, year, station):
    data = get_crime_details(crime_type, year, station)
    return JsonResponse(data)
