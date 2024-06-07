import json
from django.core.management.base import BaseCommand
from crimes.models import CrimeData
import os

class Command(BaseCommand):
    help = 'Load crime data from JSON file into the database'

    def handle(self, *args, **kwargs):
        # 프로젝트 루트 디렉토리 경로 확인
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        json_file_path = os.path.join(project_root, 'crime_map', 'data', 'crime_data_converted.json')

        # JSON 파일 열기
        try:
            with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                for row in data:
                    CrimeData.objects.create(
                        station=row['station'],
                        crime_type=row['crime_type'],
                        year=int(row['year']) if row['year'] else 0,
                        murder=int(row['murder']) if row['murder'] else 0,
                        robbery=int(row['robbery']) if row['robbery'] else 0,
                        sexual_crime=int(row['sexual_crime']) if row['sexual_crime'] else 0,
                        theft=int(row['theft']) if row['theft'] else 0,
                        violence=int(row['violence']) if row['violence'] else 0
                    )
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
        except TypeError as e:
            self.stdout.write(self.style.ERROR(f'TypeError: {e}'))
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'ValueError: {e}'))
