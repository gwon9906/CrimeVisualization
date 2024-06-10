import os
import pandas as pd
import django

# Django 설정 파일 경로를 지정합니다
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrimeVisualization.settings')

# Django를 초기화합니다
django.setup()

from crime_map.models import CrimeData

# CSV 파일 경로를 설정합니다
CSV_FILE_PATH = 'C:\\Users\\My\\Desktop\\소공1\\CrimeVisualization\\crime_map\\data\\crime_data.csv'
df = pd.read_csv(CSV_FILE_PATH)

# CrimeData 모델에 CSV 데이터를 추가합니다
for index, row in df.iterrows():
    CrimeData.objects.create(
        station=row['경찰서'],
        year=row['년도'],
        murder=row['살인'],
        robbery=row['강도'],
        sexual_crime=row['성범죄'],
        theft=row['절도'],
        violence=row['폭력']
    )
